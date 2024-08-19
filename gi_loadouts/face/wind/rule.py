from PySide6.QtWidgets import QComboBox, QLabel, QLineEdit, QMainWindow, QMessageBox

from gi_loadouts.data.arti import ArtiList
from gi_loadouts.data.char import __charmaps__
from gi_loadouts.data.weap import Family
from gi_loadouts.face.util import truncate_text
from gi_loadouts.face.wind.wind import Ui_mainwind
from gi_loadouts.type import arti
from gi_loadouts.type.arti import ArtiLevl, Collection, __artistat__
from gi_loadouts.type.arti.base import (
    MainStatType_CCOL,
    MainStatType_FWOL,
    MainStatType_GBOE,
    MainStatType_PMOD,
    MainStatType_SDOE,
    SecoStatType,
)
from gi_loadouts.type.calc import CHAR, TEAM, WEAP
from gi_loadouts.type.char import CharName
from gi_loadouts.type.char.cons import Cons
from gi_loadouts.type.levl import Level
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import WeaponStatType, WeaponType
from gi_loadouts.type.calc import CHAR, TEAM, WEAP
from gi_loadouts.type.stat import ATTR, STAT, __revmap__
from gi_loadouts.type.vson import __visioncolour__


class Rule(QMainWindow, Ui_mainwind):
    def __init__(self):
        super().__init__()
        self.collection = Collection()
        self.otptobjc = None
        self.c_team = TEAM()
        self.c_char = CHAR()
        self.c_weap = WEAP()
        self.c_tyvt = CHAR()
        self.dialog = None

    def populate_dropdown(self):
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

    def handle_char_data(self, _):
        if self.head_char_name.currentText().strip() != "" and self.head_char_levl.currentText().strip() != "":
            char = __charmaps__[self.head_char_name.currentText()]()
            char.levl = getattr(Level, self.head_char_levl.currentText().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
            self.head_char_data_vson.setText(char.vision.value)
            self.head_char_data_attk.setText(f"{round(char.attack)}")
            self.head_char_data_dfns.setText(f"{round(char.defense)}")
            self.head_char_data_hlpt.setText(f"{round(char.health_points)}")
            self.head_char_icon_subs.setToolTip(f"{char.seco.stat_name.value}")
            self.head_char_data_subs.setText(f"{round(char.seco.stat_data, 1)}")
            self.head_area.setStyleSheet(f"#head_area {{background-color: {__visioncolour__[char.vision]};}}")
            self.weap_area_type.clear()
            self.weap_area_type.addItem(f"{char.weapon.value}")

    def convey_weapon_type_change(self, _):
        if self.weap_area_type.currentText().strip() != "":
            self.weap_area_name.clear()
            self.weap_area_name.addItems([item for item in Family[self.weap_area_type.currentText()]])

    def convey_weapon_name_change(self, _):
        if self.weap_area_name.currentText().strip() != "" and self.weap_area_type.currentText().strip() != "":
            kind = self.weap_area_type.currentText().strip()
            name = self.weap_area_name.currentText()
            self.weap_area_levl.clear()
            self.weap_area_refn.clear()
            self.weap_area_refn_head.setText("No refinements available.")
            self.weap_area_refn_body.setText("No refinements available.")
            self.weap_area_stat.setText("No substats.")
            weap = Family[kind][name]
            self.weap_area_levl.addItems([item.value.name for item in weap.levl_bind])
            self.weap_area_refn.addItems([f"Refinement {indx + 1}" for indx in range(len(weap.refi_list))])

    def convey_weapon_levl_change(self, _):
        if self.weap_area_type.currentText().strip() != "" and self.weap_area_name.currentText().strip() != "" and self.weap_area_levl.currentText().strip() != "":
            name = self.weap_area_name.currentText()
            kind = self.weap_area_type.currentText().strip()
            weap = Family[kind][name]
            weap.levl = getattr(Level, self.weap_area_levl.currentText().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
            self.weap_area_batk.setText(f"ATK {round(weap.main_stat.stat_data)}")
            if weap.seco_stat.stat_name != WeaponStatType.none:
                self.weap_area_stat.setText(f"{weap.seco_stat_calc.stat_name.value.value} {round(weap.seco_stat_calc.stat_data, 1)}")

    def convey_refinement_change(self, _):
        if self.weap_area_type.currentText().strip() != "" and self.weap_area_name.currentText().strip() != "" and self.weap_area_refn.currentText().strip() != "":
            name = self.weap_area_name.currentText()
            kind = self.weap_area_type.currentText().strip()
            weap = Family[kind][name]
            refn = self.weap_area_refn.currentIndex()
            self.weap_area_refn_head.setText(f"<b>{weap.refi_name}</b>")
            self.weap_area_refn_body.setText(f"{weap.refi_list[refn]}")

    def change_rarity_by_changing_type(self, droptype: QComboBox, droprare: QComboBox, artiname: QLabel, part: str) -> None:
        if droptype.currentText().strip() != "":
            kind = getattr(ArtiList, droptype.currentText().replace(" ", "_").replace("'", "").replace("-", "_"))
            droprare.clear()
            droprare.addItems([f"Star {indx.value}" for indx in kind.value.rare])
            artiname.setText(truncate_text(getattr(kind.value, part).__name__))

    def change_data_by_changing_level_or_stat(self, droplevl: QComboBox, droptype: QComboBox, droprare: QComboBox, dropstat: QComboBox, statdata: QLineEdit, part: str) -> None:
        if droplevl.currentText().strip() != "" and droptype.currentText().strip() != "" and droprare.currentText().strip() != "" and dropstat.currentText().strip() != "":
            """
            Checking if no artifact is selected
            """
            if droptype.currentText().strip() != "None" and dropstat.currentText().strip() != "None":
                levl = getattr(ArtiLevl, droplevl.currentText().replace(" ", "_"))
                team = getattr(ArtiList, droptype.currentText().replace(" ", "_").replace("'", "").replace("-", "_"))
                rare = getattr(Rare, droprare.currentText().replace(" ", "_"))
                stat = getattr(arti, f"revmap_{part}")[dropstat.currentText()]
                item = getattr(team.value, part)
                item.levl, item.rare, item.stat_name = levl.value.levl, rare.value, stat
                statdata.setText(f"{round(item.stat_data, 1)}")

    def change_artifact_team_by_changing_type(self, droptype: QComboBox, part: str) -> None:
        if droptype.currentText().strip() != "":
            kind = getattr(ArtiList, droptype.currentText().replace(" ", "_").replace("'", "").replace("-", "_"))
            item = getattr(kind.value, part)
            setattr(self.collection, part, item)
            _ = [indx.setText("No artifact set.") for indx in [self.pair_area_head, self.quad_area_head]]
            _ = [indx.setText("No artifact set bonus.") for indx in [self.pair_area_desc, self.quad_area_desc]]
            if self.collection.quad != "":
                pack = getattr(ArtiList, self.collection.quad.replace(" ", "_").replace("'", "").replace("-", "_"))
                self.pair_area_head.setText(f"<b>{truncate_text(pack.value.name, 32)}</b> (2)")
                self.pair_area_desc.setText(f"{pack.value.pairtext}")
                self.quad_area_head.setText(f"<b>{truncate_text(pack.value.name, 32)}</b> (4)")
                self.quad_area_desc.setText(f"{pack.value.quadtext}")
            elif self.collection.pair != []:
                if len(self.collection.pair) == 1:
                    pair_a = getattr(ArtiList, self.collection.pair[0].replace(" ", "_").replace("'", "").replace("-", "_"))
                    self.pair_area_head.setText(f"<b>{truncate_text(pair_a.value.name, 32)}</b> (2)")
                    self.pair_area_desc.setText(f"{pair_a.value.pairtext}")
                elif len(self.collection.pair) == 2:
                    pair_a = getattr(ArtiList, self.collection.pair[0].replace(" ", "_").replace("'", "").replace("-", "_"))
                    self.pair_area_head.setText(f"<b>{truncate_text(pair_a.value.name, 32)}</b> (2)")
                    self.pair_area_desc.setText(f"{pair_a.value.pairtext}")
                    pair_b = getattr(ArtiList, self.collection.pair[1].replace(" ", "_").replace("'", "").replace("-", "_"))
                    self.quad_area_head.setText(f"<b>{truncate_text(pair_b.value.name, 32)}</b> (2)")
                    self.quad_area_desc.setText(f"{pair_b.value.pairtext}")

    def remove_artifact(self, droptype: QComboBox, part: str) -> None:
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

    def change_artifact_substats_by_changing_rarity_or_mainstat(self, droplevl: QComboBox, droprare: QComboBox, dropstat: QComboBox, part: str) -> None:
        if droprare.currentText().strip() != "" and dropstat.currentText().strip() != "":
            rare = getattr(Rare, droprare.currentText().replace(" ", "_"))
            stat = dropstat.currentText().strip()
            droplevl.clear()
            droplevl.addItems([item.value.name for item in ArtiLevl if rare in item.value.rare])
            for indx in __artistat__[rare.value]["active"]:
                getattr(self, f"arti_{part}_name_{indx}").clear()
                getattr(self, f"arti_{part}_name_{indx}").addItems([item.value.value for item in SecoStatType if item.value.value != stat])
            for alfa in __artistat__[rare.value]["inactive"]:
                getattr(self, f"arti_{part}_name_{alfa}").clear()
                getattr(self, f"arti_{part}_name_{alfa}").addItems(["None"])

    def change_levels_by_changing_rarity(self, droplevl: QComboBox, droprare: QComboBox) -> None:
        if droprare.currentText().strip() != "":
            rare = getattr(Rare, droprare.currentText().replace(" ", "_"))
            droplevl.clear()
            droplevl.addItems([item.value.name for item in ArtiLevl if rare in item.value.rare])

    def render_lineedit_readonly_when_none(self, dropstat: QComboBox, lineedit: QLineEdit) -> None:
        if dropstat.currentText().strip() == "None":
            lineedit.clear()
            lineedit.setDisabled(True)
        else:
            lineedit.clear()
            lineedit.setDisabled(False)

    def show_output_window(self):
        """
        TODO: Make into a separate function
        """
        if self.head_char_name.currentText().strip() != "" and self.head_char_levl.currentText().strip() != "":
            #self.otptobjc = OtptWindow(self.head_char_name.currentText())
            #self.otptobjc.show()
            char = __charmaps__[self.head_char_name.currentText()]()
            char.levl = getattr(Level, self.head_char_levl.currentText().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
            self.c_char.attack = ATTR(stat_name=STAT.attack, stat_data=char.attack)
            self.c_char.defense = ATTR(stat_name=STAT.defense, stat_data=char.defense)
            self.c_char.health_points = ATTR(stat_name=STAT.health_points, stat_data=char.health_points)
            prev_stat_data = getattr(self.c_char, self.c_char.revmap[char.seco.stat_name]).stat_data
            curt_stat_data = char.seco.stat_data
            # 100 + 26.8
            setattr(self.c_char, self.c_char.revmap[char.seco.stat_name], ATTR(stat_name=char.seco.stat_name, stat_data=prev_stat_data + curt_stat_data))
        """
        TODO: Make into a separate function
        """
        if self.weap_area_type.currentText().strip() != "" and self.weap_area_name.currentText().strip() != "" and self.weap_area_refn.currentText().strip() != "" and self.weap_area_levl.currentText().strip() != "":
            kind = self.weap_area_type.currentText().strip()
            name = self.weap_area_name.currentText()
            weap = Family[kind][name]
            refn = self.weap_area_refn.currentIndex()
            weap.levl = getattr(Level, self.weap_area_levl.currentText().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
            self.c_weap.base = ATTR(stat_name=WeaponStatType.attack.value, stat_data=weap.main_stat.stat_data)
            if weap.seco_stat.stat_name != WeaponStatType.none:
                self.c_weap.seco = ATTR(stat_name=weap.seco_stat_calc.stat_name.value, stat_data=weap.seco_stat_calc.stat_data)
            if len(weap.refi_stat) != 0:
                self.c_weap.refn = weap.refi_stat[refn]
        """
        TODO: Make into a separate function
        """
        for part in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
            if getattr(self, f"arti_{part}_type").currentText().strip() != "":
                for indx in ["main", "a", "b", "c", "d"]:
                    if getattr(self, f"arti_{part}_name_{indx}").currentText().strip() != "":
                        if getattr(self, f"arti_{part}_name_{indx}").currentText().strip() == "None":
                            setattr(self.c_team, f"{part}_{indx}", ATTR(stat_name=STAT.none, stat_data=0.0))
                        else:
                            try:
                                setattr(self.c_team, f"{part}_{indx}", ATTR(stat_name=__revmap__[getattr(self, f"arti_{part}_name_{indx}").currentText().strip()], stat_data=float(getattr(self, f"arti_{part}_data_{indx}").text().strip())))
                            except ValueError:
                                self.show_dialog(QMessageBox.Information, "Invalid input detected", "Please enter a valid input (eg. 69, 42.0 etc.)")
        if self.collection.quad != "":
            pack = getattr(ArtiList, self.collection.quad.replace(" ", "_").replace("'", "").replace("-", "_"))
            self.c_team.pairdata_a = pack.value.pairdata
            self.c_team.quaddata = pack.value.quaddata
        elif self.collection.pair != []:
            if len(self.collection.pair) == 1:
                pack_a = getattr(ArtiList, self.collection.pair[0].replace(" ", "_").replace("'", "").replace("-", "_"))
                self.c_team.pairdata_a = pack_a.value.pairdata
            elif len(self.collection.pair) == 2:
                pack_a = getattr(ArtiList, self.collection.pair[0].replace(" ", "_").replace("'", "").replace("-", "_"))
                self.c_team.pairdata_a = pack_a.value.pairdata
                pack_b = getattr(ArtiList, self.collection.pair[1].replace(" ", "_").replace("'", "").replace("-", "_"))
                self.c_team.pairdata_b = pack_b.value.pairdata
        print(self.c_team, "\n\n\n")
        """
        TODO: Make into a separate function
        """
        """
        self.c_tyvt.attack = 0
        self.c_tyvt.defense = 0
        self.c_tyvt.health_points = 0
        """
        """
        ARTIFACT
        """
        char_substats_data = getattr(self.c_char, self.c_char.revmap[char.seco.stat_name]).stat_data
        setattr(self.c_tyvt, self.c_tyvt.revmap[char.seco.stat_name], ATTR(stat_name=char.seco.stat_name, stat_data=char_substats_data))
        # c_tyvt = 126.8
        for item in self.c_tyvt.revmap:
            for kind in ["fwol", "pmod", "sdoe", "gboe", "ccol"]:
                for indx in ["main", "a", "b", "c", "d"]:
                    if getattr(self.c_team, f"{kind}_{indx}").stat_name == item:
                        prev = getattr(self.c_tyvt, self.c_tyvt.revmap[item]).stat_data
                        curt = getattr(self.c_team, f"{kind}_{indx}").stat_data
                        setattr(self.c_tyvt, self.c_tyvt.revmap[item], ATTR(stat_name=item, stat_data=prev+curt))
        """
        SET BONUSES
        """
        for item in self.c_tyvt.revmap:
            for indx in ["pairdata_a", "pairdata_b", "quaddata"]:
                lict = getattr(self.c_team, indx)
                if len(indx) != 0:
                    for advn in lict:
                        if advn.stat_name == item:
                            prev = getattr(self.c_tyvt, self.c_tyvt.revmap[item]).stat_data
                            curt = advn.stat_data
                            setattr(self.c_tyvt, self.c_tyvt.revmap[item], ATTR(stat_name=item, stat_data=prev + curt))
        """
        WEAPON SUBSTAT
        """
        prev = getattr(self.c_tyvt, self.c_tyvt.revmap[self.c_weap.seco.stat_name]).stat_data
        curt = self.c_weap.seco.stat_data
        setattr(self.c_tyvt, self.c_tyvt.revmap[self.c_weap.seco.stat_name], ATTR(stat_name=self.c_weap.seco.stat_name, stat_data=prev + curt))
        """
        WEAPON REFINEMENT BONUSES
        """
        for item in self.c_tyvt.revmap:
            for indx in self.c_weap.refn:
                if item == indx.stat_name.value:
                    prev = getattr(self.c_tyvt, self.c_tyvt.revmap[item]).stat_data
                    curt = indx.stat_data
                    setattr(self.c_tyvt, self.c_tyvt.revmap[item], ATTR(stat_name=item, stat_data=prev + curt))

        self.c_tyvt.attack = ATTR(
            stat_name=STAT.attack,
            stat_data=(self.c_char.attack.stat_data + self.c_weap.base.stat_data) * (100 + self.c_tyvt.attack_perc.stat_data) / 100.0 + self.c_tyvt.attack.stat_data
        )
        self.c_tyvt.health_points = ATTR(
            stat_name=STAT.health_points,
            stat_data=self.c_char.health_points.stat_data * (100 + self.c_tyvt.health_points_perc.stat_data) / 100.0 + self.c_tyvt.health_points.stat_data
        )
        self.c_tyvt.defense = ATTR(
            stat_name=STAT.defense,
            stat_data=self.c_char.defense.stat_data * (100 + self.c_tyvt.defense_perc.stat_data) / 100.0 + self.c_tyvt.defense.stat_data
        )

        print(self.c_tyvt)

    def validate_lineedit_userdata(self, text):
        try:
            data = float(text)
            self.statarea.clearMessage()
        except ValueError:
            self.statarea.showMessage("Please enter a valid input (eg. 69, 42.0 etc.)")

    def show_dialog(self, icon, head, text):
        if self.dialog is None:
            self.dialog = QMessageBox(parent=self)
            self.dialog.setIcon(icon)
            self.dialog.setWindowTitle(f"{self.headtext} - {head}")
            self.dialog.setText(text)
            self.dialog.setFont("IBM Plex Sans")
            self.dialog.show()
        else:
            self.dialog.show()
