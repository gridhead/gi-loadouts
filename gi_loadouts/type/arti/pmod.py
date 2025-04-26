from typing import Optional

from .base import Artifact, MainStatType_PMOD, SecoStat
from .stat import attack


class PMOD(Artifact):
    """
    Artifact primitive for a "Plume of Death" artifact
    """
    stat_name: Optional[MainStatType_PMOD] = MainStatType_PMOD.attack
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
        return attack[self.rare]["init"] + sum(attack[self.rare]["diff"][0:self.levl+1])  # noqa : E501


__revmap__ = {
    "ATK": MainStatType_PMOD.attack
}
