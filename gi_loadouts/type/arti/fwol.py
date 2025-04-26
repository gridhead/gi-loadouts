from typing import Optional

from .base import Artifact, MainStatType_FWOL, SecoStat
from .stat import health_points


class FWOL(Artifact):
    """
    Artifact primitive for a "Flower of Life" artifact
    """
    stat_name: Optional[MainStatType_FWOL] = MainStatType_FWOL.health_points
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
        return health_points[self.rare]["init"] + sum(health_points[self.rare]["diff"][0:self.levl+1])  # noqa : E501

__revmap__ = {
    "HP": MainStatType_FWOL.health_points
}
