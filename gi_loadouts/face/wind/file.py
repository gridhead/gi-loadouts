from datetime import datetime
from uuid import uuid4

import yaml
from PySide6.QtWidgets import QFileDialog, QMessageBox

from gi_loadouts.data.arti import ArtiList
from gi_loadouts.face.wind.talk import Dialog
from gi_loadouts.type.arti import ArtiLevl
from gi_loadouts.type.file.arti import ArtiArea, ArtiFile, make_artifile
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import ATTR, STAT, __revmap__


class FileHandling(Dialog):
    def __init__(self):
        super().__init__()

    def open_explorer_load(self, part: str) -> None:
        explorer = QFileDialog()
        loadfile = explorer.getOpenFileName(self, "Select location", "", "All Files (*)")[0]

        try:
            if loadfile.strip() == "":
                raise FileNotFoundError

            with open(loadfile) as fileobjc:
                temp = fileobjc.read()

            if temp.strip() == "":
                raise ValueError

            objc = yaml.safe_load(temp)
            arti = make_artifile(objc)
            if arti.area.value != part.upper():
                raise ValueError

            droptype = getattr(self, f"arti_{part}_type")
            droptype.setCurrentText(arti.type.value.name)
            droprare = getattr(self, f"arti_{part}_rare")
            droprare.setCurrentText(f"Star {arti.rare.value}")
            """
            Changing the main stat of the artifact (i.e. arti_{part}_name_main) results in the 
            resetting of level but changing the level of the artifact (i.e. arti_{part}_levl) 
            does not result in the resetting of the main stat of the artifact. Hence, after 
            everything has been set. We will change the level.
            """
            droplevl = getattr(self, f"arti_{part}_levl")
            droplevl.setCurrentText(arti.levl.value.name)

            for indx in ["main", "a", "b", "c", "d"]:
                dropname = getattr(self, f"arti_{part}_name_{indx}")
                dropdata = getattr(self, f"arti_{part}_data_{indx}")
                namelist = [dropname.itemText(roll) for roll in range(dropname.count())]
                if getattr(arti, f"stat_{indx}").stat_name.value in namelist:
                    dropname.setCurrentText(getattr(arti, f"stat_{indx}").stat_name.value)
                    dropdata.setText(str(getattr(arti, f"stat_{indx}").stat_data))
                else:
                    raise ValueError

            self.statarea.showMessage("Artifact data has been successfully loaded.")

        except Exception:
            self.show_dialog(
                QMessageBox.Critical,
                "Load failed",
                "Please confirm that the artifact file follows the valid format before loading it from a location that is accessible."
            )

    def open_explorer_save(self, part: str) -> None:
        try:
            if getattr(self, f"arti_{part}_type").currentText().strip() == "":
                raise ValueError

            objc = ArtiFile(
                type=getattr(ArtiList, getattr(self, f"arti_{part}_type").currentText().strip().replace(" ", "_").replace("'", "").replace("-", "_")),
                levl=getattr(ArtiLevl, getattr(self, f"arti_{part}_levl").currentText().strip().replace(" ", "_")),
                area=getattr(ArtiArea, part),
                name=getattr(self, f"arti_{part}_type_name").text().strip(),
                rare=getattr(Rare, getattr(self, f"arti_{part}_rare").currentText().strip().replace(" ", "_")),
            )

            for indx in ["main", "a", "b", "c", "d"]:
                if getattr(self, f"arti_{part}_name_{indx}").currentText().strip() != "":
                    if getattr(self, f"arti_{part}_name_{indx}").currentText().strip() == "None":
                        setattr(
                            objc,
                            f"stat_{indx}",
                            ATTR(
                                stat_name=STAT.none,
                                stat_data=0.0
                            )
                        )
                    else:
                        setattr(
                            objc,
                            f"stat_{indx}",
                            ATTR(
                                stat_name=__revmap__[getattr(self, f"arti_{part}_name_{indx}").currentText().strip()],
                                stat_data=float(getattr(self, f"arti_{part}_data_{indx}").text().strip())
                            )
                        )

            text = yaml.dump(objc.easydict)
            explorer = QFileDialog()
            filename = f"{getattr(self, f"arti_{part}_type").currentText().strip().replace(" ", "").replace("'", "").replace("-", "")}_{uuid4().hex[0:8].upper()}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.{part}.yaml"
            savefile = explorer.getSaveFileName(self, "Select location", filename, "All Files (*)")[0]

            if savefile.strip() == "":
                raise FileNotFoundError

            with open(savefile, "w") as fileobjc:
                fileobjc.write(text)

            self.statarea.showMessage("Artifact data has been successfully saved.")

        except Exception:
            self.show_dialog(
                QMessageBox.Information,
                "Save failed",
                "Please confirm that the input is valid (eg. 69, 42.0 etc.) before saving the artifact data in a location that is accessible."
            )
