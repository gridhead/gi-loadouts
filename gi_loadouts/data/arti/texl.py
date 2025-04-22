from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "The Exile"
    __pairdata__ = [ATTR(stat_name=STAT.energy_recharge_perc, stat_data=20)]
    __pairtext__ = "Energy Recharge +20%"
    __quaddata__ = []
    __quadtext__ = "Using an Elemental Burst regenerates 2 Energy for other party members every 2s for 6s. This effect cannot stack."


class fwol(team, FWOL):
    __name__ = "Exile's Flower"


class pmod(team, PMOD):
    __name__ = "Exile's Feather"


class sdoe(team, SDOE):
    __name__ = "Exile's Pocket Watch"


class gboe(team, GBOE):
    __name__ = "Exile's Goblet"


class ccol(team, CCOL):
    __name__ = "Exile's Circlet"
