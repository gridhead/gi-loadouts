from typing import Optional

from .base import Artifact, MainStatType_CCOL, SecoStat
from .stat import (
    attack_perc,
    critical_damage_perc,
    critical_rate_perc,
    defense_perc,
    elemental_mastery,
    healing_bonus_perc,
    health_point_perc,
)


class CCOL(Artifact):
    """
    Artifact primitive for a "Circlet of Logos" artifact
    """
    stat_name: Optional[MainStatType_CCOL] = MainStatType_CCOL.none
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
        if self.stat_name == MainStatType_CCOL.attack_perc:
            calc = attack_perc[self.rare]["init"] + sum(attack_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_CCOL.defense_perc:
            calc = defense_perc[self.rare]["init"] + sum(defense_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_CCOL.health_points_perc:
            calc = health_point_perc[self.rare]["init"] + sum(health_point_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_CCOL.elemental_mastery:
            calc = elemental_mastery[self.rare]["init"] + sum(elemental_mastery[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_CCOL.healing_bonus_perc:
            calc = healing_bonus_perc[self.rare]["init"] + sum(healing_bonus_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_CCOL.critical_rate_perc:
            calc = critical_rate_perc[self.rare]["init"] + sum(critical_rate_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        elif self.stat_name == MainStatType_CCOL.critical_damage_perc:
            calc = critical_damage_perc[self.rare]["init"] + sum(critical_damage_perc[self.rare]["diff"][0:self.levl+1])  # noqa : E501
        return calc


__revmap__ = {
    "ATK %": MainStatType_CCOL.attack_perc,
    "DEF %": MainStatType_CCOL.defense_perc,
    "HP %": MainStatType_CCOL.health_points_perc,
    "Elemental Mastery": MainStatType_CCOL.elemental_mastery,
    "Healing Bonus": MainStatType_CCOL.healing_bonus_perc,
    "Crit Rate": MainStatType_CCOL.critical_rate_perc,
    "Crit DMG": MainStatType_CCOL.critical_damage_perc,
}
