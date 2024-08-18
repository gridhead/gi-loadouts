from PySide6.QtWidgets import QMainWindow

from gi_loadouts.data.arti import ArtiList
from gi_loadouts.data.char import __charmaps__
from gi_loadouts.data.weap import Family
from gi_loadouts.face.util import truncate_text
from gi_loadouts.face.wind.wind import Ui_mainwind
from gi_loadouts.type import arti
from gi_loadouts.type.arti import ArtiLevl, Collection
from gi_loadouts.type.arti.base import (
    MainStatType_CCOL,
    MainStatType_FWOL,
    MainStatType_GBOE,
    MainStatType_PMOD,
    MainStatType_SDOE,
)
from gi_loadouts.type.char import CharName
from gi_loadouts.type.char.cons import Cons
from gi_loadouts.type.levl import Level
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import WeaponStatType, WeaponType
from gi_loadouts.face.otpt.main import OtptWindow


class Rule(QMainWindow, Ui_mainwind):
    def __init__(self):
        super().__init__()
        self.collection = Collection()
        self.otptobjc = None

    def populate_dropdown(self):
        self.head_char_name.addItems([item.value for item in CharName])
        self.head_char_cons.addItems([item.value.name for item in Cons])
        self.head_char_levl.addItems([item.value.name for item in Level])
        self.arti_fwol_main_name.addItems([item.value.value for item in MainStatType_FWOL if item != MainStatType_FWOL.none])
        self.arti_pmod_main_name.addItems([item.value.value for item in MainStatType_PMOD if item != MainStatType_PMOD.none])
        self.arti_sdoe_main_name.addItems([item.value.value for item in MainStatType_SDOE if item != MainStatType_SDOE.none])
        self.arti_gboe_main_name.addItems([item.value.value for item in MainStatType_GBOE if item != MainStatType_GBOE.none])
        self.arti_ccol_main_name.addItems([item.value.value for item in MainStatType_CCOL if item != MainStatType_CCOL.none])
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

    def change_rarity_by_changing_type(self, droptype, droprare, artiname, part):
        if droptype.currentText().strip() != "":
            kind = getattr(ArtiList, droptype.currentText().replace(" ", "_").replace("'", "").replace("-", "_"))
            droprare.clear()
            droprare.addItems([f"Star {indx.value}" for indx in kind.value.rare])
            artiname.setText(truncate_text(getattr(kind.value, part).__name__))

    def change_levels_by_changing_rarity(self, droprare, droplevl):
        if droprare.currentText().strip() != "":
            rare = getattr(Rare, droprare.currentText().replace(" ", "_"))
            droplevl.clear()
            droplevl.addItems([item.value.name for item in ArtiLevl if rare in item.value.rare])

    def change_data_by_changing_level_or_stat(self, droplevl, droptype, droprare, dropstat, statdata, part):
        if droplevl.currentText().strip() != "" and droptype.currentText().strip() != "" and droprare.currentText().strip() != "" and dropstat.currentText().strip() != "":
            levl = getattr(ArtiLevl, droplevl.currentText().replace(" ", "_"))
            team = getattr(ArtiList, droptype.currentText().replace(" ", "_").replace("'", "").replace("-", "_"))
            rare = getattr(Rare, droprare.currentText().replace(" ", "_"))
            stat = getattr(arti, f"revmap_{part}")[dropstat.currentText()]
            item = getattr(team.value, part)
            item.levl, item.rare, item.stat_name = levl.value.levl, rare.value, stat
            statdata.setText(f"{round(item.stat_data, 1)}")

    def change_artifact_team_by_changing_type(self, droptype, part):
        if droptype.currentText().strip() != "":
            kind = getattr(ArtiList, droptype.currentText().replace(" ", "_").replace("'", "").replace("-", "_"))
            item = getattr(kind.value, part)
            setattr(self.collection, part, item)
            _ = [indx.setText("No artifact set.") for indx in [self.pair_area_head, self.quad_area_head]]
            _ = [indx.setText("No artifact set bonus.") for indx in [self.pair_area_desc, self.quad_area_desc]]
            if self.collection.quad != "":
                print("QUAD", self.collection.quad)
                pack = getattr(ArtiList, self.collection.quad.replace(" ", "_").replace("'", "").replace("-", "_"))
                self.pair_area_head.setText(f"<b>{truncate_text(pack.value.name, 32)}</b> (2)")
                self.pair_area_desc.setText(f"{pack.value.pairtext}")
                self.quad_area_head.setText(f"<b>{truncate_text(pack.value.name, 32)}</b> (4)")
                self.quad_area_desc.setText(f"{pack.value.quadtext}")
            elif self.collection.pair != []:
                print("PAIR", self.collection.pair)
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

    def show_output_window(self):
        if self.head_char_name.currentText().strip() != "" and self.head_char_levl.currentText().strip() != "":
            self.otptobjc = OtptWindow(self.head_char_name.currentText())
            self.otptobjc.show()
