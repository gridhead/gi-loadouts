import io

from PIL import Image
from PIL.ImageQt import QBuffer
from PySide6.QtCore import QByteArray, QMimeData, QThread
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QPixmap
from PySide6.QtWidgets import QApplication, QComboBox, QDialog, QLineEdit, QMessageBox

from ... import conf
from ...data.arti import ArtiList
from ...type import arti
from ...type.arti import ArtiLevl, __artistat__
from ...type.arti.base import (
    MainStatType_CCOL,
    MainStatType_FWOL,
    MainStatType_GBOE,
    MainStatType_PMOD,
    MainStatType_SDOE,
    SecoStatType,
)
from ...type.rare import Rare
from ...type.stat import ATTR, __revmap__
from ..util import modify_datatype_to_transfer, truncate_text
from ..wind.talk import Dialog
from . import areaiden, tab_order_scan
from .file import file
from .scan import Ui_scan
from .work import ScanWorker


class Rule(QDialog, Ui_scan, Dialog):
    def __init__(self) -> None:
        super().__init__()
        self.shot = None
        self.snap = None
        self.part = ""
        self.thread = None
        self.worker = None
        self.dialog = QMessageBox()
        self.dist = {
            "Flower of Life": {"list": MainStatType_FWOL, "part": "fwol"},
            "Plume of Death": {"list": MainStatType_PMOD, "part": "pmod"},
            "Sands of Eon": {"list": MainStatType_SDOE, "part": "sdoe"},
            "Goblet of Eonothem": {"list": MainStatType_GBOE, "part": "gboe"},
            "Circlet of Logos": {"list": MainStatType_CCOL, "part": "ccol"},
        }

    def __del__(self):
        """
        TODO: Fix `QThread: Destroyed while thread is still running`

        This is not as much of a problem on faster CPUs but on slower ones, if an image is selected
        for scanning and immediately after that the scanning dialog is dismissed and the application
        is quit while the image is being processed in the optical character recognition section, the
        application will not be happy if it is has to destroy the thread while it is still running.

        This is not likely to cause major problems but still, this is not the right approach and
        should be rectified at the earliest, no matter how small of a use-case this might be.
        """
        try:
            if isinstance(self.thread, QThread):
                self.thread.terminate()
        except RuntimeError:
            return

    def populate_dropdown(self) -> None:
        """
        Populate the various comboboxes present on the user interface

        :return:
        """
        self.arti_dist.addItems(self.dist.keys())
        self.arti_dist.setCurrentText(areaiden[getattr(arti, self.part.upper())])
        self.arti_type.addItems([item.value.name for item in ArtiList])

    def change_mainstat_by_changing_artifact_area(self) -> None:
        """
        Change the mainstat possible with the selected artifact distribution area

        :return:
        """
        if self.arti_dist.currentText().strip() != "":
            self.arti_name_main.clear()
            self.arti_name_main.addItems(
                [item.value.value for item in self.dist[self.arti_dist.currentText().strip()]["list"] if item != self.dist[self.arti_dist.currentText().strip()]["list"].none]
            )

    def change_artifact_name_by_changing_artifact_area_or_type(self) -> None:
        """
        Change the artifact qualities, artifact name and artifact icon based on the compatibility of the currently selected artifact type

        :return:
        """
        if self.arti_dist.currentText().strip() != "" and self.arti_type.currentText().strip() != "":
            kind = getattr(ArtiList, self.arti_type.currentText().replace(" ", "_").replace("'", "").replace("-", "_"))
            self.arti_rare.clear()
            self.arti_rare.addItems([indx.value.name for indx in kind.value.rare])
            self.arti_type_name.setText(truncate_text(getattr(kind.value, self.dist[self.arti_dist.currentText().strip()]["part"]).__name__, 34))
            self.arti_head_icon.setPixmap(QPixmap(f":arti/imgs/arti/{kind.value.file}/{self.dist[self.arti_dist.currentText().strip()]["part"]}.webp"))
            if self.arti_type.currentText().strip() == "None":
                self.arti_head_icon.setPixmap(QPixmap(f":arti/imgs/arti/main/{self.dist[self.arti_dist.currentText().strip()]["part"]}.webp"))

    def change_levels_backdrop_by_changing_rarity(self) -> None:
        """
        Change the associated levels and qualities backdrop of the selected artifact after the artifact qualities is selected from the combobox

        :return:
        """
        if self.arti_rare.currentText().strip() != "":
            rare = getattr(Rare, self.arti_rare.currentText().replace(" ", "_"))
            self.arti_levl.clear()
            self.arti_levl.addItems([item.value.name for item in ArtiLevl if rare in item.value.rare])
            self.arti_head_area.setPixmap(QPixmap(rare.value.back))

    def change_artifact_substats_by_changing_rarity_or_mainstat(self) -> None:
        """
        Change the associated substats of the selected artifact after the artifact qualities or artifact mainstat is selected from the combobox

        :return:
        """
        if self.arti_rare.currentText().strip() != "" and self.arti_name_main.currentText().strip() != "" and self.arti_type.currentText().strip() != "":
            rare = getattr(Rare, self.arti_rare.currentText().replace(" ", "_"))
            stat = self.arti_name_main.currentText().strip()
            for indx in __artistat__[rare.value.qant]["active"]:
                getattr(self, f"arti_name_{indx}").clear()
                getattr(self, f"arti_name_{indx}").addItems([item.value.value for item in SecoStatType if item.value.value != stat])
            for alfa in __artistat__[rare.value.qant]["inactive"]:
                getattr(self, f"arti_name_{alfa}").clear()
                getattr(self, f"arti_name_{alfa}").addItems(["None"])

    def render_lineedit_readonly_when_none(self, dropstat: QComboBox, lineedit: QLineEdit) -> None:
        """
        Render the artifact statistics text field read-only when the associated artifact substats combobox has ``None`` selected

        :param dropstat: Combobox used for selecting artifact substats
        :param lineedit: Lineedit used for displaying the statistics of the artifact substats
        :return:
        """
        if dropstat.currentText().strip() == "None":
            lineedit.clear()
            lineedit.setDisabled(True)
        else:
            lineedit.clear()
            lineedit.setDisabled(False)

    def remove_artifact(self) -> None:
        """
        Exhibit removal of the selected artifact on the user interface from the loadout of the selected type

        This handles both application and reversal of the removal action

        :return:
        """
        if self.arti_type.currentText().strip() != "" and self.arti_dist.currentText().strip() != "":
            if self.arti_type.currentText().strip() == "None":
                self.arti_name_main.clear()
                self.arti_name_main.addItems(["None"])
                self.arti_data_main.clear()
                self.arti_name_main.setDisabled(True)
            else:
                self.arti_data_main.clear()
                self.arti_name_main.setDisabled(False)
                self.arti_name_main.clear()
                self.arti_name_main.addItems([item.value.value for item in self.dist[self.arti_dist.currentText().strip()]["list"] if item != self.dist[self.arti_dist.currentText().strip()]["list"].none])

    def wipe_artifact(self) -> None:
        """
        Exhibit removal of the selected artifact on the user interface from the loadout of the selected type

        This handles the removal when the button associated with the wipe action is triggered

        :return:
        """
        self.arti_type.setCurrentText("None")

    def change_data_by_changing_level_or_stat(self) -> None:
        """
        Change the associated statistics of the mainstat after a certain artifact level or artifact mainstat is selected from the combobox

        :return:
        """
        if self.arti_dist.currentText().strip() != "" and self.arti_levl.currentText().strip() != "" and self.arti_type.currentText().strip() != "" and self.arti_rare.currentText().strip() and self.arti_name_main.currentText().strip() != "":
            """
            Checking if no artifact is selected
            """
            if self.arti_type.currentText().strip() != "None" and self.arti_name_main.currentText().strip() != "None":

                levl = getattr(ArtiLevl, self.arti_levl.currentText().replace(" ", "_"))
                team = getattr(ArtiList, self.arti_type.currentText().replace(" ", "_").replace("'", "").replace("-", "_"))
                rare = getattr(Rare, self.arti_rare.currentText().replace(" ", "_"))
                stat = getattr(arti, f"revmap_{self.dist[self.arti_dist.currentText().strip()]["part"]}")[self.arti_name_main.currentText().strip()]
                item = getattr(team.value, self.dist[self.arti_dist.currentText().strip()]["part"])
                item.levl, item.rare, item.stat_name = levl.value.levl, rare.value.qant, stat
                self.arti_data_main.setText(f"{round(item.stat_data, 1)}")

    def initiate_thread(self) -> None:
        """
        Kick things up after the thread has achieved its purpose

        :return:
        """
        self.arti_text.setText("Inspecting screenshot...")

    def complete_thread(self) -> None:
        """
        Wipe things up after the thread has achieved its purpose

        :return:
        """
        self.arti_text.setText("Browse your local storage to load a high quality screenshot of your artifact and the statistics will automatically be computed from there.")
        if isinstance(self.thread, QThread):
            self.thread.quit()
            self.thread.wait()

    def register_return_from_scanning(self, rslt: tuple) -> None:
        """
        Place the selected screenshot and the detected attributes on the user interface

        :return:
        """
        area, main, seco, team, levl, rare, duration, expt = rslt

        if expt:
            self.show_dialog(
                QMessageBox.Information,
                "Faulty scanning",
                f"Please consider checking your input after ensuring that the proper Tesseract OCR executable has been selected.\n\n{expt}"
            )
            return

        self.arti_shot.setPixmap(self.shot)

        if area in [self.arti_dist.itemText(indx) for indx in range(self.arti_dist.count())]:
            self.arti_dist.setCurrentText(area)
        if team in [self.arti_type.itemText(indx) for indx in range(self.arti_type.count())]:
            self.arti_type.setCurrentText(team)
        if rare in [self.arti_rare.itemText(indx) for indx in range(self.arti_rare.count())]:
            self.arti_rare.setCurrentText(rare)
        if levl in [self.arti_levl.itemText(indx) for indx in range(self.arti_levl.count())]:
            self.arti_levl.setCurrentText(levl)
        if main.stat_name.value in [self.arti_name_main.itemText(indx) for indx in range(self.arti_name_main.count())]:
            self.arti_name_main.setCurrentText(main.stat_name.value)
        for alfa, item in seco.items():
            if item.stat_name.value in [getattr(self, f"arti_name_{alfa}").itemText(indx) for indx in range(getattr(self, f"arti_name_{alfa}").count())]:
                getattr(self, f"arti_name_{alfa}").setCurrentText(item.stat_name.value)
                getattr(self, f"arti_data_{alfa}").setText(str(item.stat_data))

    def load_reader(self) -> None:
        """
        Facilitate the loading of data and calculation of statistics

        :return:
        """
        try:
            self.thread, self.worker = QThread(parent=self), ScanWorker(self.snap)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.initiate_thread)
            self.thread.started.connect(self.worker.scan_artifact)
            self.worker.result.connect(self.register_return_from_scanning)
            self.worker.result.connect(self.complete_thread)
            self.thread.start()
        except Exception as expt:
            self.show_dialog(
                QMessageBox.Information,
                "Faulty scanning",
                f"Please consider checking your input after ensuring that the proper Tesseract OCR executable has been selected.\n\n{expt}"
            )

    def insert_data_from_file(self) -> None:
        """
        Kick off the image loading and scanning from the file

        :return:
        """
        try:
            status, self.shot, self.snap = file.load_screenshot_with_picker(self, "Select location to load artifact screenshot")
            if not status:
                return
            self.load_reader()
        except Exception as expt:
            self.show_dialog(
                QMessageBox.Information,
                "Faulty scanning",
                f"Please consider checking your input after ensuring that the proper Tesseract OCR executable has been selected.\n\n{expt}"
            )

    def transfer_to_processing(self, data: QMimeData) -> None:
        """
        Preprocess the data either from the keyboard shortcut or from the drag-and-drop action

        :return:
        """
        try:
            if data.hasImage():
                """
                If the item selected from the clipboard are file contents
                """
                shot = QPixmap.fromImage(data.imageData())
                btls = QByteArray()
                buff = QBuffer(btls)
                buff.open(QBuffer.WriteOnly)
                data.imageData().save(buff, "PNG")
                buff.close()
                snap = Image.open(io.BytesIO(btls.data()))
                self.shot, self.snap = shot, snap
                """
                Initialize scanning after the shot and snap objects are populated
                """
                self.load_reader()
            elif data.hasUrls():
                """
                If the item selected from the clipboard are file paths
                """
                urls = data.urls()
                path = urls[0].toLocalFile()
                try:
                    self.shot, self.snap = file.load_mask_from_file(path)
                    """
                    Initialize scanning after the shot and snap objects are populated
                    """
                    self.load_reader()
                except Exception as expt:
                    raise ValueError("Please select an accurate screenshot.") from expt
            else:
                """
                If the item selected from the clipboard are not supported
                """
                raise ValueError("Please select an accurate screenshot.")
        except Exception as expt:
            self.show_dialog(
                QMessageBox.Information,
                "Faulty scanning",
                f"Please consider checking your input after ensuring that the proper Tesseract OCR executable has been selected.\n\n{expt}"
            )

    def insert_data_from_shortcut(self) -> None:
        """
        Kick off the image loading and scanning from the keyboard shortcut

        :return:
        """
        self.transfer_to_processing(QApplication.clipboard().mimeData())


    def dragEnterEvent(self, incident: QDragEnterEvent) -> None:  # pragma: no cover
        """
        Method override for QWidget to ensure that the said event is properly handled

        Used on the QLabel item arti_shot for the drag-and-drop action

        :return:
        """
        incident.acceptProposedAction()

    def dragMoveEvent(self, incident: QDragEnterEvent) -> None:  # pragma: no cover
        """
        Method override for QWidget to ensure that the said event is properly handled

        Used on the QLabel item arti_shot for the drag-and-drop action

        :return:
        """
        incident.acceptProposedAction()

    def dropEvent(self, incident: QDropEvent) -> None:
        """
        Kick off the image loading and scanning from the drag-and-drop action

        Method override for QWidget to ensure that the said event is properly handled

        Used on the QLabel item arti_shot for the drag-and-drop action

        :return:
        """
        self.transfer_to_processing(incident.mimeData())

    def load_tessexec(self) -> None:
        """
        Locate the Tesseract OCR executable from the storage device

        :return:
        """
        try:
            status, tessexec = file.load_tessexec_with_picker(self, "Select location of the Tesseract OCR executable")
            if status:
                conf.tessexec = tessexec
        except Exception as expt:
            self.show_dialog(
                QMessageBox.Information,
                "Faulty scanning",
                f"Please consider checking your input after ensuring that the proper Tesseract OCR executable has been selected.\n\n{expt}"
            )

    def keep_info(self) -> dict:
        """
        Store information from the user interface to pass on to the main user interface

        :return:
        """
        rtrn = {
            "part": self.dist[self.arti_dist.currentText().strip()]["part"],
            "team": self.arti_type.currentText().strip(),
            "rare": self.arti_rare.currentText().strip(),
            "levl": self.arti_levl.currentText().strip(),
            "stat": {
                "main": ATTR(
                    stat_name=__revmap__[self.arti_name_main.currentText().strip()],
                    stat_data=modify_datatype_to_transfer(self.arti_data_main.text())
                ),
                "seco": {
                    "a": ATTR(
                        stat_name=__revmap__[self.arti_name_a.currentText().strip()],
                        stat_data=modify_datatype_to_transfer(self.arti_data_a.text())
                    ),
                    "b": ATTR(
                        stat_name=__revmap__[self.arti_name_b.currentText().strip()],
                        stat_data=modify_datatype_to_transfer(self.arti_data_b.text())
                    ),
                    "c": ATTR(
                        stat_name=__revmap__[self.arti_name_c.currentText().strip()],
                        stat_data=modify_datatype_to_transfer(self.arti_data_c.text())
                    ),
                    "d": ATTR(
                        stat_name=__revmap__[self.arti_name_d.currentText().strip()],
                        stat_data=modify_datatype_to_transfer(self.arti_data_d.text())
                    )
                }
            }
        }
        return rtrn

    def wipe_snapshot(self) -> None:
        """
        Reset the snapshot preview section to clear out the previously selected image

        :return:
        """
        self.arti_shot.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">YOUR ARTIFACT SCREENSHOT WILL SHOW UP HERE</span></p><p align=\"center\">INSERT AN ARTIFACT SCREENSHOT HERE BY EITHER PRESSING<span style=\" font-weight:700;\"> CTRL + V</span> OR USING <span style=\" font-weight:700;\">DRAG AND DROP</span></p></body></html>")

    def regulate_taborder(self) -> None:
        """
        Set the tab order

        :return:
        """
        for current_widget, next_widget in zip(tab_order_scan, tab_order_scan[1:]):
             self.setTabOrder(getattr(self, current_widget), getattr(self, next_widget))
