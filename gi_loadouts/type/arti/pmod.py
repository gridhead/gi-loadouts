from typing import Optional

from gi_loadouts.type.arti.base import Artifact, MainStatType_PMOD, SecoStat
from gi_loadouts.type.arti.base.stat import attack


class PMOD(Artifact):
    stat_name: Optional[MainStatType_PMOD] = MainStatType_PMOD.attack
    secostat_a: Optional[SecoStat] = SecoStat()
    secostat_b: Optional[SecoStat] = SecoStat()
    secostat_c: Optional[SecoStat] = SecoStat()
    secostat_d: Optional[SecoStat] = SecoStat()

    @property
    def stat_data(self):
        return attack[self.rare]["init"] + sum(attack[self.rare]["diff"][0:self.levl+1])  # noqa : E501


__revmap__ = {
    "ATK": MainStatType_PMOD.attack
}
