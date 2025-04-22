from typing import Optional

from .base import Artifact, MainStatType_GBOE, SecoStat
from .stat import (
    attack_perc,
    damage_bonus_elemental_perc,
    damage_bonus_physical_perc,
    defense_perc,
    elemental_mastery,
    health_point_perc,
)


class GBOE(Artifact):
    """
    Artifact primitive for a "Goblet of Eonothem" artifact
    """
    stat_name: Optional[MainStatType_GBOE] = MainStatType_GBOE.none
    secostat_a: Optional[SecoStat] = SecoStat()
    secostat_b: Optional[SecoStat] = SecoStat()
    secostat_c: Optional[SecoStat] = SecoStat()
    secostat_d: Optional[SecoStat] = SecoStat()

    @property
    def stat_data(self) -> float:
        """
        Calculate the statistics associated with the artifact mainstat based on the artifact quality and artifact level

        :return:
        """
        calc = 0.0
        if self.stat_name == MainStatType_GBOE.attack_perc:
            calc = attack_perc[self.rare]["init"] + sum(attack_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_GBOE.defense_perc:
            calc = defense_perc[self.rare]["init"] + sum(defense_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_GBOE.health_points_perc:
            calc = health_point_perc[self.rare]["init"] + sum(health_point_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_GBOE.elemental_mastery:
            calc = calc = elemental_mastery[self.rare]["init"] + sum(elemental_mastery[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name in (
            MainStatType_GBOE.damage_bonus_anemo_perc,
            MainStatType_GBOE.damage_bonus_cryo_perc,
            MainStatType_GBOE.damage_bonus_dendro_perc,
            MainStatType_GBOE.damage_bonus_electro_perc,
            MainStatType_GBOE.damage_bonus_geo_perc,
            MainStatType_GBOE.damage_bonus_hydro_perc,
            MainStatType_GBOE.damage_bonus_pyro_perc
        ):
            calc = damage_bonus_elemental_perc[self.rare]["init"] + sum(damage_bonus_elemental_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_GBOE.damage_bonus_physical_perc:
            calc = damage_bonus_physical_perc[self.rare]["init"] + sum(damage_bonus_physical_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        return calc


__revmap__ = {
    "ATK %": MainStatType_GBOE.attack_perc,
    "DEF %": MainStatType_GBOE.defense_perc,
    "HP %": MainStatType_GBOE.health_points_perc,
    "Elemental Mastery": MainStatType_GBOE.elemental_mastery,
    "Anemo DMG Bonus": MainStatType_GBOE.damage_bonus_anemo_perc,
    "Cryo DMG Bonus": MainStatType_GBOE.damage_bonus_cryo_perc,
    "Dendro DMG Bonus": MainStatType_GBOE.damage_bonus_dendro_perc,
    "Electro DMG Bonus": MainStatType_GBOE.damage_bonus_electro_perc,
    "Geo DMG Bonus": MainStatType_GBOE.damage_bonus_geo_perc,
    "Hydro DMG Bonus": MainStatType_GBOE.damage_bonus_hydro_perc,
    "Pyro DMG Bonus": MainStatType_GBOE.damage_bonus_pyro_perc,
    "Physical DMG Bonus": MainStatType_GBOE.damage_bonus_physical_perc,
}
