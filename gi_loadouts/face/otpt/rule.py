from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow

from ...face.util import modify_graphics_resource
from .otpt import Ui_otptwind


class Rule(QMainWindow, Ui_otptwind):
    def __init__(self) -> None:
        super().__init__()
        self.arti = None
        self.char = None
        self.weap = None
        self.tyvt = None

    def populate_blanks(self) -> None:
        """
        Populate blanks on the output window

        :return:
        """
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
            self.area_crvl_data: f"{str(round(self.tyvt.critical_damage_perc.stat_data + 2*(self.tyvt.critical_rate_perc.stat_data), 1))}"
        }
        for item in assignment:
            item.setText(assignment[item])

    def populate_header(self) -> None:
        """
        Populate header on the output window

        :return:
        """
        self.head_area_line_prim.setText(f"<b>{self.char["char"].name.value}</b> - {self.char["levl"]} ({self.char["cons"]})")
        weaprefn = f"({self.weap["refn"]})" if self.weap["refn"] != "" else ""
        if self.arti["quad"] != "":
            artiline = f"4 x <b>{self.arti["quad"]}</b>"
        elif len(self.arti["pair"]) >= 1:
            artiline = ", ".join([f"2 x <b>{item}</b>" for item in self.arti["pair"]])
        else:
            artiline = "No artifact set bonus."
        secotext = f"<b>{self.weap["name"]}</b> - {self.weap["levl"]} {weaprefn}" + "<br/>" + f"{artiline}"
        self.head_area_line_seco.setText(secotext)

    def manage_assets(self) -> None:
        """
        Utilize the graphical resources on the output window

        :return:
        """
        self.head_vson.setPixmap(QPixmap(f":vson/imgs/vson/{self.char["char"].vision.value.name.lower()}.webp"))
        self.char_back.setPixmap(modify_graphics_resource(f":back/imgs/char/back/{self.char["char"].name.lower().replace(" ", "_")}.webp"))
        self.char_wish.setPixmap(QPixmap(f":wish/imgs/char/wish/{self.char["char"].name.lower().replace(" ", "_")}.webp"))
