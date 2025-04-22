from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Brave Heart"
    __pairdata__ = [ATTR(stat_name=STAT.attack_perc, stat_data=18)]
    __pairtext__ = "ATK +18%"
    __quaddata__ = []
    __quadtext__ = "Increases DMG by 30% against enemies with more than 50% HP."


class fwol(team, FWOL):
    __name__ = "Medal of the Brave"


class pmod(team, PMOD):
    __name__ = "Prospect of the Brave"


class sdoe(team, SDOE):
    __name__ = "Fortitude of the Brave"


class gboe(team, GBOE):
    __name__ = "Outset of the Brave"


class ccol(team, CCOL):
    __name__ = "Crown of the Brave"
