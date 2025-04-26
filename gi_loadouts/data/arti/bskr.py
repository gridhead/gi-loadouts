from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Berserker"
    __pairdata__ = [ATTR(stat_name=STAT.critical_rate_perc, stat_data=12)]
    __pairtext__ = "CRIT Rate +12%"
    __quaddata__ = []
    __quadtext__ = "When HP is below 70%, CRIT Rate increases by an additional 24%."


class fwol(team, FWOL):
    __name__ = "Berserker's Rose"


class pmod(team, PMOD):
    __name__ = "Berserker's Indigo Feather"


class sdoe(team, SDOE):
    __name__ = "Berserker's Timepiece"


class gboe(team, GBOE):
    __name__ = "Berserker's Bone Goblet"


class ccol(team, CCOL):
    __name__ = "Berserker's Battle Mask"
