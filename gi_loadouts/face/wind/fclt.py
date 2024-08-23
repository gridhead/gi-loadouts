from datetime import datetime
from uuid import uuid4

import yaml
from PySide6.QtWidgets import QMessageBox

from gi_loadouts.data.arti import ArtiList
from gi_loadouts.face.wind.file import file
from gi_loadouts.face.wind.talk import Dialog
from gi_loadouts.type.arti import ArtiLevl
from gi_loadouts.type.file.arti import ArtiArea, ArtiFile, make_artifile
from gi_loadouts.type.file.team import TeamFile, make_teamfile
from gi_loadouts.type.file.weap import WeapFile, make_weapfile
from gi_loadouts.type.levl import Level
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import ATTR, STAT, __revmap__
from gi_loadouts.type.weap import WeaponType


class Facility(Dialog):
    def __init__(self):
        super().__init__()

    def arti_save(self, part: str) -> None:
        try:
            if getattr(self, f"arti_{part}_type").currentText().strip() == "":
                raise ValueError("Artifact type cannot be identified.")

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

        except Exception as expt:
            self.show_dialog(
                QMessageBox.Information,
                "Save failed",
                f"Please confirm that the input is valid (eg. 69, 42.0 etc.) before saving the artifact data in a location that is accessible.\n\n{expt}",
            )

    def team_save(self) -> None:
        try:
            data = TeamFile()
            arealist = ["fwol", "pmod", "sdoe", "gboe", "ccol"]
            for part in arealist:
                if getattr(self, f"arti_{part}_type").currentText().strip() == "":
                    raise ValueError("Artifact type cannot be identified.")
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
                setattr(data, part, objc)
            text = yaml.dump(data.easydict)
            file.save(
                self,
                "Select location to save artifact data",
                f"{uuid4().hex[0:8].upper()}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.yaml",
                text,
            )
            self.statarea.showMessage("Artifact team has been successfully saved.")
        except Exception as expt:
            self.show_dialog(
                QMessageBox.Information,
                "Save failed",
                f"Please confirm that the input is valid (eg. 69, 42.0 etc.) before saving the artifact team in a location that is accessible.\n\n{expt}",
            )

    def weap_save(self) -> None:
        try:
            if self.weap_area_type.currentText() != "" and self.weap_area_name.currentText() != "" and self.weap_area_refn.currentText() != "" and self.weap_area_levl.currentText() != "":
                objc = WeapFile(
                    name=self.weap_area_name.currentText(),
                    type=getattr(WeaponType, self.weap_area_type.currentText().lower()),
                    levl=getattr(Level, self.weap_area_levl.currentText().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")),
                    refn=self.weap_area_refn.currentText(),
                )
                text = yaml.dump(objc.easydict)
                file.save(
                    self,
                    "Select location to save weapon data",
                    f"{objc.name.strip().replace(" ", "").replace("\"", "").replace("-", "").replace("'", "")}_{uuid4().hex[0:8].upper()}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.yaml",
                    text,
                )
                self.statarea.showMessage("Weapon data has been successfully saved.")
        except Exception as expt:
            self.show_dialog(
                QMessageBox.Information,
                "Save failed",
                f"Please confirm that the location that is accessible before saving the weapon data.\n\n{expt}",
            )

    def arti_load(self, part: str) -> None:
        try:
            data = file.load(
                self,
                "Select location to load artifact data"
            )

            if data.strip() == "":
                raise ValueError("Selected file cannot be read.")

            objc = yaml.safe_load(data)
            arti = make_artifile(objc)
            if arti.area.value != part.upper():
                raise ValueError("Artifact area cannot be identified.")

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
                    raise ValueError("Artifact stat cannot be identified.")

            self.statarea.showMessage("Artifact data has been successfully loaded.")

        except Exception as expt:
            self.show_dialog(
                QMessageBox.Information,
                "Load failed",
                f"Please confirm that the artifact data follows the valid format before loading it from a location that is accessible.\n\n{expt}"
            )

    def team_load(self) -> None:
        try:
            data = file.load(
                self,
                "Select location to load artifact team"
            )

            if data.strip() == "":
                raise ValueError("Selected file cannot be read.")

            objc = yaml.safe_load(data)
            team = make_teamfile(objc)

            for part in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
                arti = getattr(team, part)
                if arti.area.value != part.upper():
                    raise ValueError("Artifact area cannot be identified.")

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
                        raise ValueError("Artifact stat cannot be identified.")

            self.statarea.showMessage("Artifact team has been successfully loaded.")
        except Exception as expt:
            self.show_dialog(
                QMessageBox.Information,
                "Load failed",
                f"Please confirm that the artifact team follows the valid format before loading it from a location that is accessible.\n\n{expt}"
            )

    def weap_load(self) -> None:
        try:
            if self.weap_area_type.currentText() != "" and self.weap_area_name.currentText() != "" and self.weap_area_refn.currentText() != "" and self.weap_area_levl.currentText() != "":
                data = file.load(
                    self,
                    "Select location to load weapon data"
                )

                if data.strip() == "":
                    raise ValueError("Selected file cannot be read.")

                objc = yaml.safe_load(data)
                weap = make_weapfile(objc)

                typelist = [self.weap_area_type.itemText(indx) for indx in range(self.weap_area_type.count())]
                if weap.type.value not in typelist:
                    raise ValueError("Weapon type cannot be identified.")
                self.weap_area_type.setCurrentText(weap.type.value)

                weaplist = [self.weap_area_name.itemText(indx) for indx in range(self.weap_area_name.count())]
                if weap.name not in weaplist:
                    raise ValueError("Weapon name cannot be identified.")
                self.weap_area_name.setCurrentText(weap.name)

                levllist = [self.weap_area_levl.itemText(indx) for indx in range(self.weap_area_levl.count())]
                if weap.levl.value.name not in levllist:
                    raise ValueError("Weapon level cannot be parsed.")
                self.weap_area_levl.setCurrentText(weap.levl.value.name)

                refnlist = [self.weap_area_refn.itemText(indx) for indx in range(self.weap_area_refn.count())]
                if weap.refn not in refnlist:
                    raise ValueError("Weapon refinement cannot be parsed.")
                self.weap_area_refn.setCurrentText(weap.refn)

                self.statarea.showMessage("Weapon data has been successfully loaded.")
        except Exception as expt:
            self.show_dialog(
                QMessageBox.Information,
                "Load failed",
                f"Please confirm that the location that is accessible before loading the weapon data.\n\n{expt}",
            )
