from typing import Optional

from .base import Artifact, MainStatType_SDOE, SecoStat
from .stat import (
    attack_perc,
    defense_perc,
    elemental_mastery,
    energy_recharge_perc,
    health_point_perc,
)


class SDOE(Artifact):
    """
    Artifact primitive for a "Sands of Eon" artifact
    """
    stat_name: Optional[MainStatType_SDOE] = MainStatType_SDOE.none
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
        if self.stat_name == MainStatType_SDOE.attack_perc:
            calc = attack_perc[self.rare]["init"] + sum(attack_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_SDOE.defense_perc:
            calc = defense_perc[self.rare]["init"] + sum(defense_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_SDOE.health_points_perc:
            calc = health_point_perc[self.rare]["init"] + sum(health_point_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_SDOE.elemental_mastery:
            calc = elemental_mastery[self.rare]["init"] + sum(elemental_mastery[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_SDOE.energy_recharge_perc:
            calc = energy_recharge_perc[self.rare]["init"] + sum(energy_recharge_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        return calc


__revmap__ = {
    "ATK %": MainStatType_SDOE.attack_perc,
    "DEF %": MainStatType_SDOE.defense_perc,
    "HP %": MainStatType_SDOE.health_points_perc,
    "Elemental Mastery": MainStatType_SDOE.elemental_mastery,
    "Energy Recharge": MainStatType_SDOE.energy_recharge_perc,
}
