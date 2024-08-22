from datetime import datetime
from uuid import uuid4

import yaml
from PySide6.QtWidgets import QMessageBox

from gi_loadouts.data.arti import ArtiList
from gi_loadouts.face.wind.file import file
from gi_loadouts.face.wind.talk import Dialog
from gi_loadouts.type.arti import ArtiLevl
from gi_loadouts.type.file.arti import ArtiArea, ArtiFile, make_artifile
from gi_loadouts.type.file.team import make_teamfile
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import ATTR, STAT, __revmap__


class Facility(Dialog):
    def __init__(self):
        super().__init__()

    def arti_save(self, part: str) -> None:
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
            file.save(
                self,
                "Select location to save artifact data",
                f"{getattr(self, f"arti_{part}_type").currentText().strip().replace(" ", "").replace("'", "").replace("-", "")}_{uuid4().hex[0:8].upper()}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.{part}.yaml",
                text,
            )
            self.statarea.showMessage("Artifact data has been successfully saved.")

        except Exception:
            self.show_dialog(
                QMessageBox.Information,
                "Save failed",
                "Please confirm that the input is valid (eg. 69, 42.0 etc.) before saving the artifact data in a location that is accessible.",
            )

    def team_save(self) -> None:
        try:
            data = {"fwol": dict(), "pmod": dict(), "sdoe": dict(), "gboe": dict(), "ccol": dict()}
            for part in data:
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
                data[part] = objc.easydict
            text = yaml.dump(data)
            file.save(
                self,
                "Select location to save artifact data",
                f"{uuid4().hex[0:8].upper()}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.yaml",
                text,
            )
            self.statarea.showMessage("Artifact team has been successfully saved.")
        except Exception:
            self.show_dialog(
                QMessageBox.Information,
                "Save failed",
                "Please confirm that the input is valid (eg. 69, 42.0 etc.) before saving the artifact team in a location that is accessible.",
            )

    def arti_load(self, part: str) -> None:
        try:
            data = file.load(
                self,
                "Select location to load artifact data"
            )

            if data.strip() == "":
                raise ValueError

            objc = yaml.safe_load(data)
            arti = make_artifile(objc)
            if arti.area.value != part.upper():
                raise ValueError

            droptype = getattr(self, f"arti_{part}_type")
            droptype.setCurrentText(arti.type.value.name)
            droprare = getattr(self, f"arti_{part}_rare")
            droprare.setCurrentText(f"Star {arti.rare.value}")
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
                "Please confirm that the artifact data follows the valid format before loading it from a location that is accessible."
            )

    def team_load(self) -> None:
        try:
            data = file.load(
                self,
                "Select location to load artifact team"
            )

            if data.strip == "":
                raise ValueError

            objc = yaml.safe_load(data)
            team = make_teamfile(objc)

            for part in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
                arti = getattr(team, part)
                if arti.area.value != part.upper():
                    raise ValueError

                droptype = getattr(self, f"arti_{part}_type")
                droptype.setCurrentText(arti.type.value.name)
                droprare = getattr(self, f"arti_{part}_rare")
                droprare.setCurrentText(f"Star {arti.rare.value}")
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

            self.statarea.showMessage("Artifact team has been successfully loaded.")
        except Exception:
            self.show_dialog(
                QMessageBox.Critical,
                "Load failed",
                "Please confirm that the artifact team follows the valid format before loading it from a location that is accessible."
            )
