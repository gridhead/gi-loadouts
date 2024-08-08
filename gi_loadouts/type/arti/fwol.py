from typing import Optional

from gi_loadouts.type.arti.base import Artifact, MainStatType_FWOL, SecoStat
from gi_loadouts.type.arti.base.stat import health_points


class FWOL(Artifact):
    stat_name: Optional[MainStatType_FWOL] = MainStatType_FWOL.health_points
    secostat_a: Optional[SecoStat] = SecoStat()
    secostat_b: Optional[SecoStat] = SecoStat()
    secostat_c: Optional[SecoStat] = SecoStat()
    secostat_d: Optional[SecoStat] = SecoStat()

    @property
    def stat_data(self):
        return health_points[self.rare]["init"] + sum(health_points[self.rare]["diff"][0:self.levl+1])  # noqa : E501

__revmap__ = {
    "HP": MainStatType_FWOL.health_points
}