from PySide6.QtCore import Qt

from gi_loadouts.face.otpt.rule import Rule
from gi_loadouts.type.calc.char import CHAR


class OtptWindow(Rule):
    def __init__(self, name: str, tint: str, tyvt: CHAR):
        super().__init__()
        self.headtext = f"Loadouts for Genshin Impact - {name}"
        self.setupUi(self)
        self.setWindowTitle(self.headtext)
        self.setWindowModality(Qt.ApplicationModal)
        self.tyvt = tyvt
        self.tint = tint
        self.populate_blanks()

    def populate_blanks(self):
        self.head_area.setStyleSheet(f"#head_area {{background-color: {self.tint};}}")
        assignment = {
            self.area_hlpt_data: str(round(self.tyvt.health_points.stat_data, 1)),
            self.area_hlpt_calc: f"{round(self.tyvt.addendum_base_health_points.stat_data, 1)} + {round(self.tyvt.addendum_plus_health_points.stat_data, 1)}",
            self.area_attk_data: str(round(self.tyvt.attack.stat_data, 1)),
            self.area_attk_calc: f"{round(self.tyvt.addendum_base_attack.stat_data, 1)} + {round(self.tyvt.addendum_plus_attack.stat_data, 1)}",
            self.area_dfns_data: str(round(self.tyvt.defense.stat_data, 1)),
            self.area_dfns_calc: f"{round(self.tyvt.addendum_base_defense.stat_data, 1)} + {round(self.tyvt.addendum_plus_defense.stat_data, 1)}",
            self.area_elma_data: str(round(self.tyvt.elemental_mastery.stat_data, 1)),
            self.area_crit_rate_data: f"{str(round(self.tyvt.critical_rate_perc.stat_data, 1))}%",
            self.area_crit_dmge_data: f"{str(round(self.tyvt.critical_damage_perc.stat_data, 1))}%",
            self.area_heal_perc_data: f"{str(round(self.tyvt.healing_bonus_perc.stat_data, 1))}%",
            self.area_heal_incm_data: f"{str(round(self.tyvt.incoming_healing_bonus_perc.stat_data, 1))}%",
            self.area_enrc_data: f"{str(round(self.tyvt.energy_recharge_perc.stat_data, 1))}%",
            self.area_cldn_data: f"{str(round(self.tyvt.cooldown_reduction_perc.stat_data, 1))}%",
            self.area_sdsh_data: f"{str(round(self.tyvt.shield_strength_perc.stat_data, 1))}%",
            self.area_pyro_perc_data: f"{str(round(self.tyvt.damage_bonus_pyro_perc.stat_data, 1))}%",
            self.area_pyro_resi_data: f"{str(round(self.tyvt.resistance_pyro_perc.stat_data, 1))}%",
            self.area_hydo_perc_data: f"{str(round(self.tyvt.damage_bonus_hydro_perc.stat_data, 1))}%",
            self.area_hydo_resi_data: f"{str(round(self.tyvt.resistance_hydro_perc.stat_data, 1))}%",
            self.area_dend_perc_data: f"{str(round(self.tyvt.damage_bonus_dendro_perc.stat_data, 1))}%",
            self.area_dend_resi_data: f"{str(round(self.tyvt.resistance_dendro_perc.stat_data, 1))}%",
            self.area_elec_perc_data: f"{str(round(self.tyvt.damage_bonus_electro_perc.stat_data, 1))}%",
            self.area_elec_resi_data: f"{str(round(self.tyvt.resistance_electro_perc.stat_data, 1))}%",
            self.area_anem_perc_data: f"{str(round(self.tyvt.damage_bonus_anemo_perc.stat_data, 1))}%",
            self.area_anem_resi_data: f"{str(round(self.tyvt.resistance_anemo_perc.stat_data, 1))}%",
            self.area_cryo_perc_data: f"{str(round(self.tyvt.damage_bonus_cryo_perc.stat_data, 1))}%",
            self.area_cryo_resi_data: f"{str(round(self.tyvt.resistance_cryo_perc.stat_data, 1))}%",
            self.area_geox_perc_data: f"{str(round(self.tyvt.damage_bonus_geo_perc.stat_data, 1))}%",
            self.area_geox_resi_data: f"{str(round(self.tyvt.resistance_geo_perc.stat_data, 1))}%",
            self.area_phys_perc_data: f"{str(round(self.tyvt.damage_bonus_physical_perc.stat_data, 1))}%",
            self.area_phys_resi_data: f"{str(round(self.tyvt.resistance_physical_perc.stat_data, 1))}%",
        }
        for item in assignment:
            item.setText(assignment[item])
