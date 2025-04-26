from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices, QPixmap
from PySide6.QtWidgets import QComboBox, QDialog, QLabel, QLineEdit, QMainWindow, QMessageBox

from ...data.arti import ArtiList
from ...data.char import __charmaps__
from ...data.weap import Family
from ...type import arti
from ...type.arti import ArtiLevl, Collection, __artistat__
from ...type.arti.base import (
    MainStatType_CCOL,
    MainStatType_FWOL,
    MainStatType_GBOE,
    MainStatType_PMOD,
    MainStatType_SDOE,
    SecoStatType,
)
from ...type.char import CharName
from ...type.char.cons import Cons
from ...type.levl import Level
from ...type.rare import Rare
from ...type.vson import Vision
from ...type.weap import WeaponStatType, WeaponType
from ..info.main import InfoDialog
from ..lcns.main import LcnsDialog
from ..otpt.main import OtptWindow
from ..scan.main import ScanDialog
from ..util import modify_graphics_resource, truncate_text
from . import tab_order_wind
from .calc import Assess
from .fclt import Facility
from .util import show_status
from .wind import Ui_mainwind


class Rule(QMainWindow, Ui_mainwind, Facility, Assess):
    def __init__(self) -> None:
        super().__init__()
        self.collection = Collection()
        self.otptobjc = None
        self.infoobjc = None
        self.lcnsobjc = None
        self.scanobjc = None
        self.c_team = None
        self.c_weap = None
        self.c_tyvt = None
        self.c_char = None

    def populate_dropdown(self) -> None:
        """
        Populate the various comboboxes present on the user interface with the default collection of character names and artifact types

        :return:
        """
        self.head_char_elem.addItems(["All"] + [item.value.name for item in Vision])
        self.head_char_name.addItems([item.value for item in CharName])
        self.head_char_cons.addItems([item.value.name for item in Cons])
        self.head_char_levl.addItems([item.value.name for item in Level])
        self.arti_fwol_name_main.addItems([item.value.value for item in MainStatType_FWOL if item != MainStatType_FWOL.none])
        self.arti_pmod_name_main.addItems([item.value.value for item in MainStatType_PMOD if item != MainStatType_PMOD.none])
        self.arti_sdoe_name_main.addItems([item.value.value for item in MainStatType_SDOE if item != MainStatType_SDOE.none])
        self.arti_gboe_name_main.addItems([item.value.value for item in MainStatType_GBOE if item != MainStatType_GBOE.none])
        self.arti_ccol_name_main.addItems([item.value.value for item in MainStatType_CCOL if item != MainStatType_CCOL.none])
        self.weap_area_type.addItems([item.value for item in WeaponType if item != WeaponType.none])
        for item in [self.arti_fwol_type, self.arti_pmod_type, self.arti_sdoe_type, self.arti_gboe_type, self.arti_ccol_type]:
            item.addItems([item.value.name for item in ArtiList])

    def handle_elem_data(self, _: str = "") -> None:
        """
        Populate the characters belonging to the selected elemental vision class

        :param _: Element selected from the combobox to compute selected element
        :return:
        """
        if self.head_char_elem.currentText().strip() != "":
            self.head_char_name.clear()
            if self.head_char_elem.currentText().strip() != "All":
                self.head_char_name.addItems([item for item, data in __charmaps__.items() if data().vision.value.name == self.head_char_elem.currentText().strip()])
            else:
                self.head_char_name.addItems([item for item, data in __charmaps__.items()])

    def manage_changing_appearance(self, colour: str) -> None:
        """
        Theme the user interface elements based on the associated vision colour after a certain character is selected from the combobox

        :param colour: Colour intended for theming associated with the character vision
        :return:
        """
        self.side_back.setStyleSheet(f"#side_back {{border: 1px solid {colour}; border-radius: 5px; background-color: rgba(128, 128, 128, 64);}}")
        self.head_back.setStyleSheet(f"#head_back {{border: 1px solid {colour}; border-radius: 5px;}}")
        self.head_area.setStyleSheet(f"#head_area {{border: 1px solid {colour}; border-top-left-radius: 5px; border-bottom-left-radius: 5px; border-top-right-radius: 110px; border-bottom-right-radius: 110px; background-color: rgba(128, 128, 128, 64);}}")
        self.bone_area.setStyleSheet(f"#bone_area {{border: 1px solid {colour}; border-radius: 5px;}}")
        self.arti_area.setStyleSheet(f"#arti_area {{border: 1px solid {colour}; border-radius: 5px;}}")
        self.weap_area.setStyleSheet(f"#weap_area {{border: 1px solid {colour}; border-radius: 5px;}}")
        self.defn_area.setStyleSheet(f"#defn_area {{border: 1px solid {colour}; border-radius: 5px;}}")

    def handle_char_data(self, _: str = "") -> None:
        """
        Change the user interface elements and associated statistics after a certain character is selected from the combobox

        :param _: Element selected from the combobox to compute selected character
        :return:
        """
        if self.head_char_name.currentText().strip() != "" and self.head_char_levl.currentText().strip() != "":
            char = __charmaps__[self.head_char_name.currentText()]()
            char.levl = getattr(Level, self.head_char_levl.currentText().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
            self.head_vson.setPixmap(QPixmap(f":vson/imgs/vson/{char.vision.value.name.lower()}.webp"))
            self.head_area_back.setPixmap(modify_graphics_resource(f":name/imgs/char/name/{self.head_char_name.currentText().replace(" ", "_").lower()}.webp", 1.0, 0.75))
            self.char_inpt_icon.setPixmap(QPixmap(f":face/imgs/char/face/{self.head_char_name.currentText().replace(" ", "_").lower()}.webp"))
            self.char_inpt_area.setPixmap(QPixmap(char.rare.value.back))
            self.char_area_rare.setText(" ".join(["STAR"] * char.rare.value.qant))
            self.head_char_data_attk.setText(f"{round(char.attack.stat_data)}")
            self.head_char_data_dfns.setText(f"{round(char.defense.stat_data)}")
            self.head_char_data_hlpt.setText(f"{round(char.health_points.stat_data)}")
            self.head_char_icon_subs.setToolTip(f"{char.seco.stat_name.value}")
            self.head_char_data_subs.setText(f"{round(char.seco.stat_data, 1)}")
            self.head_area_line_prim.setText(f"{char.name.value}")
            self.head_area_line_seco.setText(f"{char.cons_name}")
            self.head_area_line_tert.setText(f"{char.weapon.value}")
            self.head_area_line_quat.setText(f"<i>{char.name.value} is a {char.weapon.value.lower()}-wielding{f" {char.vision.value.name} " if char.vision != Vision.none else " "}character of {char.rare.value.qant}-star quality.</i>")
            self.head_area_line_quin.setText(f"<i>{char.name.value} is affiliated with {char.afln}.</i>" if char.afln != "" else f"<i>{char.name.value} is not affiliated with any association.</i>")
            self.manage_changing_appearance(char.vision.value.colour)

    def format_weapon_by_char_change(self, _: str = "") -> None:
        """
        Change the combobox showing the supported weapon types based on the compatibility of the currently selected character

        :param _: Element selected from the combobox to compute selected character
        :return:
        """
        if self.head_char_name.currentText().strip() != "" and self.head_char_levl.currentText().strip() != "":
            char = __charmaps__[self.head_char_name.currentText()]()
            char.levl = getattr(Level, self.head_char_levl.currentText().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
            self.weap_area_type.clear()
            self.weap_area_type.addItem(f"{char.weapon.value}")

    def convey_weapon_type_change(self, _: str = "") -> None:
        """
        Change the user interface elements and associated statistics after a certain weapon type is selected from the combobox

        :param _: Element selected from the combobox to compute selected weapon type
        :return:
        """
        if self.weap_area_type.currentText().strip() != "":
            self.weap_area_name.clear()
            self.weap_area_name.addItems([item for item in Family[self.weap_area_type.currentText()]])

    def convey_weapon_name_change(self, _: str = "") -> None:
        """
        Change the user interface elements and associated statistics after a certain weapon is selected from the combobox

        :param _: Element selected from the combobox to compute selected weapon
        :return:
        """
        if self.weap_area_name.currentText().strip() != "" and self.weap_area_type.currentText().strip() != "":
            kind = self.weap_area_type.currentText().strip()
            name = self.weap_area_name.currentText().strip()
            self.weap_area_levl.clear()
            self.weap_area_refn.clear()
            self.weap_area_refn_head.setText("No refinements available.")
            self.weap_area_refn_body.setText("No refinements available.")
            self.weap_area_stat.setText("No substats")
            weap = Family[kind][name]()
            self.weap_area_levl.addItems([item.value.name for item in weap.levl_bind])
            self.weap_area_refn.addItems(item for item in weap.refinement.keys())
            self.weap_port_area.setPixmap(QPixmap(weap.rare.value.back))
            self.weap_area_rare.setText(" ".join(["STAR"] * weap.rare.value.qant))

    def convey_weapon_levl_change(self, _: str = "") -> None:
        """
        Change the user interface elements and associated statistics after a certain weapon level is selected from the combobox

        :param _: Element selected from the combobox to compute selected weapon level
        :return:
        """
        if self.weap_area_type.currentText().strip() != "" and self.weap_area_name.currentText().strip() != "" and self.weap_area_levl.currentText().strip() != "":
            name = self.weap_area_name.currentText()
            kind = self.weap_area_type.currentText().strip()
            weap = Family[kind][name]()
            weap.levl = getattr(Level, self.weap_area_levl.currentText().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
            self.weap_area_batk.setText(f"ATK {round(weap.main_stat.stat_data)}")
            if weap.levl.value.rank.value <= 1:
                self.weap_port_icon.setPixmap(QPixmap(f":weap/imgs/weap/{kind.lower()}s/{weap.file}_a.webp"))
            else:
                self.weap_port_icon.setPixmap(QPixmap(f":weap/imgs/weap/{kind.lower()}s/{weap.file}_b.webp"))
            if weap.seco_stat.stat_name != WeaponStatType.none:
                self.weap_area_stat.setText(f"{weap.seco_stat_calc.stat_name.value.value} {round(weap.seco_stat_calc.stat_data, 1)}")

    def convey_refinement_change(self, _: str = "") -> None:
        """
        Change the user interface elements and associated statistics after a certain weapon refinement is selected from the combobox

        :param _: Element selected from the combobox to compute selected weapon refinement
        :return:
        """
        if self.weap_area_type.currentText().strip() != "" and self.weap_area_name.currentText().strip() != "" and self.weap_area_refn.currentText().strip() != "":
            name = self.weap_area_name.currentText()
            kind = self.weap_area_type.currentText().strip()
            weap = Family[kind][name]()
            self.weap_area_refn_head.setText(f"<b>{weap.refi_name}</b>")
            self.weap_area_refn_body.setText(f"{weap.refinement[self.weap_area_refn.currentText().strip()].data}")

    def change_rarity_backdrop_by_changing_type(self, droptype: QComboBox, droprare: QComboBox, artiname: QLabel, headicon: QLabel, part: str) -> None:
        """
        Change the artifact qualities, artifact name, artifact icon based on the compatibility of the currently selected artifact type

        :param droptype: Combobox used for selecting artifact types
        :param droprare: Combobox used for selecting artifact qualities
        :param artiname: Label used for displaying the artifact name
        :param headicon: Label used for displaying the artifact icon as a pixmap
        :param part: Kind of artifact fixtures (i.e. ``FWOL``, ``PMOD``, ``SDOE``, ``GBOE`` or ``CCOL``)
        :return:
        """
        if droptype.currentText().strip() != "":
            kind = getattr(ArtiList, droptype.currentText().replace(" ", "_").replace("'", "").replace("-", "_"))
            droprare.clear()
            droprare.addItems([indx.value.name for indx in kind.value.rare])
            artiname.setText(truncate_text(getattr(kind.value, part).__name__, 32))
            headicon.setPixmap(QPixmap(f":arti/imgs/arti/{kind.value.file}/{part}.webp"))
            if droptype.currentText().strip() == "None":
                headicon.setPixmap(QPixmap(f":arti/imgs/arti/main/{part}.webp"))

    def change_data_by_changing_level_or_stat(self, droplevl: QComboBox, droptype: QComboBox, droprare: QComboBox, dropstat: QComboBox, statdata: QLineEdit, part: str) -> None:
        """
        Change the associated statistics of the mainstat after a certain artifact level or artifact mainstat is selected from the combobox

        :param droplevl: Combobox used for selecting artifact levels
        :param droptype: Combobox used for selecting artifact types
        :param droprare: Combobox used for selecting artifact qualities
        :param dropstat: Combobox used for selecting artifact mainstats
        :param statdata: Lineedit used for displaying the statistics of the artifact mainstat
        :param part: Kind of artifact fixtures (i.e. ``FWOL``, ``PMOD``, ``SDOE``, ``GBOE`` or ``CCOL``)
        :return:
        """
        if droplevl.currentText().strip() != "" and droptype.currentText().strip() != "" and droprare.currentText().strip() != "" and dropstat.currentText().strip() != "":
            """
            Checking if no artifact is selected
            """
            if droptype.currentText().strip() != "None" and dropstat.currentText().strip() != "None":
                levl = getattr(ArtiLevl, droplevl.currentText().replace(" ", "_"))
                team = getattr(ArtiList, droptype.currentText().replace(" ", "_").replace("'", "").replace("-", "_"))
                rare = getattr(Rare, droprare.currentText().replace(" ", "_"))
                stat = getattr(arti, f"revmap_{part}")[dropstat.currentText().strip()]
                item = getattr(team.value, part)
                item.rare, item.levl, item.stat_name = rare.value.qant, levl.value.levl, stat
                statdata.setText(f"{round(item.stat_data, 1)}")

    def change_artifact_team_by_changing_type(self, droptype: QComboBox, part: str) -> None:
        """
        Compute and exhibit the artifact structures (pairs or quads) forming from changing artifact collections as a result of changing artifact types

        :param droptype: Combobox used for selecting artifact types
        :param part: Kind of artifact fixtures (i.e. ``FWOL``, ``PMOD``, ``SDOE``, ``GBOE`` or ``CCOL``)
        :return:
        """
        if droptype.currentText().strip() != "":
            kind = getattr(ArtiList, droptype.currentText().replace(" ", "_").replace("'", "").replace("-", "_"))
            item = getattr(kind.value, part)
            setattr(self.collection, part, item)
            _ = [indx.setText("No artifact set.") for indx in [self.pair_area_head, self.quad_area_head]]
            _ = [indx.setText("No artifact set bonus.") for indx in [self.pair_area_desc, self.quad_area_desc]]
            if self.collection.quad != "":
                pack = getattr(ArtiList, self.collection.quad.replace(" ", "_").replace("'", "").replace("-", "_"))
                self.pair_area_head.setText(f"<b>{truncate_text(pack.value.name, 26)}</b> (2)")
                self.pair_area_desc.setText(f"{pack.value.pairtext}")
                self.quad_area_head.setText(f"<b>{truncate_text(pack.value.name, 26)}</b> (4)")
                self.quad_area_desc.setText(f"{pack.value.quadtext}")
            elif self.collection.pair != []:
                if len(self.collection.pair) == 1:
                    pair_a = getattr(ArtiList, self.collection.pair[0].replace(" ", "_").replace("'", "").replace("-", "_"))
                    self.pair_area_head.setText(f"<b>{truncate_text(pair_a.value.name, 26)}</b> (2)")
                    self.pair_area_desc.setText(f"{pair_a.value.pairtext}")
                elif len(self.collection.pair) == 2:
                    pair_a = getattr(ArtiList, self.collection.pair[0].replace(" ", "_").replace("'", "").replace("-", "_"))
                    self.pair_area_head.setText(f"<b>{truncate_text(pair_a.value.name, 26)}</b> (2)")
                    self.pair_area_desc.setText(f"{pair_a.value.pairtext}")
                    pair_b = getattr(ArtiList, self.collection.pair[1].replace(" ", "_").replace("'", "").replace("-", "_"))
                    self.quad_area_head.setText(f"<b>{truncate_text(pair_b.value.name, 26)}</b> (2)")
                    self.quad_area_desc.setText(f"{pair_b.value.pairtext}")

    def remove_artifact(self, droptype: QComboBox, part: str) -> None:
        """
        Exhibit removal of the selected artifact on the user interface from the loadout of the selected type

        This handles both application and reversal of the removal action

        :param droptype: Combobox used for selecting artifact types
        :param part: Kind of artifact fixtures (i.e. ``FWOL``, ``PMOD``, ``SDOE``, ``GBOE`` or ``CCOL``)
        :return:
        """
        if droptype.currentText().strip() != "":
            if droptype.currentText().strip() == "None":
                getattr(self, f"arti_{part}_name_main").clear()
                getattr(self, f"arti_{part}_name_main").addItems(["None"])
                getattr(self, f"arti_{part}_data_main").clear()
                getattr(self, f"arti_{part}_name_main").setDisabled(True)
                for indx in ["a", "b", "c", "d"]:
                    getattr(self, f"arti_{part}_name_{indx}").clear()
                    getattr(self, f"arti_{part}_name_{indx}").addItems(["None"])
            else:
                getattr(self, f"arti_{part}_data_main").clear()
                getattr(self, f"arti_{part}_name_main").setDisabled(False)
                if part == "fwol":
                    self.arti_fwol_name_main.clear()
                    self.arti_fwol_name_main.addItems([item.value.value for item in MainStatType_FWOL if item != MainStatType_FWOL.none])
                elif part == "pmod":
                    self.arti_pmod_name_main.clear()
                    self.arti_pmod_name_main.addItems([item.value.value for item in MainStatType_PMOD if item != MainStatType_PMOD.none])
                elif part == "sdoe":
                    self.arti_sdoe_name_main.clear()
                    self.arti_sdoe_name_main.addItems([item.value.value for item in MainStatType_SDOE if item != MainStatType_SDOE.none])
                elif part == "gboe":
                    self.arti_gboe_name_main.clear()
                    self.arti_gboe_name_main.addItems([item.value.value for item in MainStatType_GBOE if item != MainStatType_GBOE.none])
                elif part == "ccol":
                    self.arti_ccol_name_main.clear()
                    self.arti_ccol_name_main.addItems([item.value.value for item in MainStatType_CCOL if item != MainStatType_CCOL.none])

    def change_artifact_substats_by_changing_rarity_or_mainstat(self, droprare: QComboBox, dropstat: QComboBox, part: str) -> None:
        """
        Change the associated substats of the selected artifact after the artifact qualities or artifact mainstat is selected from the combobox

        :param droprare: Combobox used for selecting artifact qualities
        :param dropstat: Combobox used for selecting artifact mainstats
        :param part: Kind of artifact fixtures (i.e. ``FWOL``, ``PMOD``, ``SDOE``, ``GBOE`` or ``CCOL``)
        :return:
        """
        if droprare.currentText().strip() != "" and dropstat.currentText().strip() != "":
            rare = getattr(Rare, droprare.currentText().replace(" ", "_"))
            stat = dropstat.currentText().strip()
            for indx in __artistat__[rare.value.qant]["active"]:
                getattr(self, f"arti_{part}_name_{indx}").clear()
                getattr(self, f"arti_{part}_name_{indx}").addItems([item.value.value for item in SecoStatType if item.value.value != stat])
            for alfa in __artistat__[rare.value.qant]["inactive"]:
                getattr(self, f"arti_{part}_name_{alfa}").clear()
                getattr(self, f"arti_{part}_name_{alfa}").addItems(["None"])

    def change_levels_backdrop_by_changing_rarity(self, droplevl: QComboBox, backdrop: QLabel, droprare: QComboBox) -> None:
        """
        Change the associated levels and qualities backdrop of the selected artifact after the artifact qualities is selected from the combobox

        :param droplevl: Combobox used for selecting artifact levels
        :param backdrop: Label used for displaying the qualities backdrop as a pixmap
        :param droprare: Combobox used for selecting artifact qualities
        :return:
        """
        if droprare.currentText().strip() != "":
            rare = getattr(Rare, droprare.currentText().replace(" ", "_"))
            droplevl.clear()
            droplevl.addItems([item.value.name for item in ArtiLevl if rare in item.value.rare])
            backdrop.setPixmap(QPixmap(rare.value.back))

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

    def show_output_window(self):
        """
        Facilitate the calculation of statistics from the gathered data and exhibit on the newly-spawned dedicated user interface

        :return:
        """
        try:
            self.calc_stat()
            self.otptobjc = OtptWindow(
                {
                    "char": __charmaps__[self.head_char_name.currentText()](),
                    "levl": self.head_char_levl.currentText().strip(),
                    "cons": self.head_char_cons.currentText().strip(),
                },
                {
                    "name": self.weap_area_name.currentText().strip(),
                    "levl": self.weap_area_levl.currentText().strip(),
                    "refn": self.weap_area_refn.currentText().strip(),
                },
                {
                    "quad": self.collection.quad,
                    "pair": self.collection.pair,
                },
                self.c_tyvt,
            )
            self.otptobjc.show()
        except Exception as expt:
            self.show_dialog(
                QMessageBox.Information,
                "Inaccuracy detected",
                f"Please consider checking your input.\n\n{expt}"
            )

    def validate_lineedit_userdata(self, text: str) -> None:
        """
        Confirm if the entry made in the field associated with the artifact substats can be converted to ``float``

        :param text: Text derived from the lineedit used for displaying the statistics of the artifact substats
        :return:
        """
        try:
            _ = float(text)
            self.statarea.clearMessage()
        except ValueError:
            show_status(self.statarea, "Please enter a valid input (eg. 69, 42.0 etc.).")

    def wipe_artifact(self, part: str) -> None:
        """
        Exhibit removal of the selected artifact on the user interface from the loadout of the selected type

        This handles the removal when the button associated with the wipe action is triggered

        :param part: Kind of artifact fixtures (i.e. ``FWOL``, ``PMOD``, ``SDOE``, ``GBOE`` or ``CCOL``)
        :return:
        """
        droptype = getattr(self, f"arti_{part}_type")
        droptype.setCurrentText("None")

    def wipe_team(self):
        """
        Exhibit removal of the selected collection of artifact on the user interface from the loadout

        This handles the removal when the button associated with the wipe action is triggered

        :return:
        """
        for item in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
            droptype = getattr(self, f"arti_{item}_type")
            droptype.setCurrentText("None")

    def select_char_from_dropdown(self, char: CharName) -> None:
        """
        Quickly select the male traveler or female traveler from the character selector

        :return:
        """
        self.head_char_elem.setCurrentText(Vision.none.value.name)
        self.head_char_name.setCurrentText(char.value)

    def show_info_dialog(self) -> None:
        """
        Initialize and exhibit the information dialog on a button click

        :return:
        """
        self.infoobjc = InfoDialog()
        self.infoobjc.show()

    def show_lcns_dialog(self) -> None:
        """
        Initialize and exhibit the licensing dialog on a button click

        :return:
        """
        self.lcnsobjc = LcnsDialog()
        self.lcnsobjc.show()

    def show_scan_dialog(self, part: str) -> None:
        """
        Initialize and exhibit the scanning dialog on a button click

        :return:
        """
        self.scanobjc = ScanDialog(part)
        if self.scanobjc.exec() == QDialog.Accepted:
            info = self.scanobjc.keep_info()

            droptype = getattr(self, f"arti_{info["part"]}_type")
            if info["team"] in [droptype.itemText(indx) for indx in range(droptype.count())]:
                droptype.setCurrentText(info["team"])

            droprare = getattr(self, f"arti_{info["part"]}_rare")
            if info["rare"] in [droprare.itemText(indx) for indx in range(droprare.count())]:
                droprare.setCurrentText(info["rare"])

            droplevl = getattr(self, f"arti_{info["part"]}_levl")
            if info["levl"] in [droplevl.itemText(indx) for indx in range(droplevl.count())]:
                droplevl.setCurrentText(info["levl"])

            dropmain = getattr(self, f"arti_{info["part"]}_name_main")
            datamain = getattr(self, f"arti_{info["part"]}_data_main")
            if info["stat"]["main"].stat_name in [dropmain.itemText(indx) for indx in range(dropmain.count())]:
                dropmain.setCurrentText(info["stat"]["main"].stat_name)
                datamain.setText(str(info["stat"]["main"].stat_data))

            for alfa, item in info["stat"]["seco"].items():
                dropseco = getattr(self, f"arti_{info["part"]}_name_{alfa}")
                dataseco = getattr(self, f"arti_{info["part"]}_data_{alfa}")
                if item.stat_name in [dropseco.itemText(indx) for indx in range(dropseco.count())]:
                    dropseco.setCurrentText(item.stat_name)
                    dataseco.setText(str(item.stat_data))

    def open_link(self, link: str) -> None:
        """
        Open link in the default browser on a button click

        :return:
        """
        QDesktopServices.openUrl(QUrl(link))

    def regulate_taborder(self) -> None:
        """
        Set the tab order

        :return:
        """
        for current_widget, next_widget in zip(tab_order_wind, tab_order_wind[1:]):
             self.setTabOrder(getattr(self, current_widget), getattr(self, next_widget))
