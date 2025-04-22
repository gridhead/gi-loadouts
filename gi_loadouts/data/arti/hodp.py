from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Heart of Depth"
    __pairdata__ = [ATTR(stat_name=STAT.damage_bonus_hydro_perc, stat_data=15)]
    __pairtext__ = "Hydro DMG Bonus +15%"
    __quaddata__ = []
    __quadtext__ = "After using Elemental Skill, increases Normal Attack and Charged Attack DMG by 30% for 15s."


class fwol(team, FWOL):
    __name__ = "Gilded Corsage"


class pmod(team, PMOD):
    __name__ = "Gust of Nostalgia"


class sdoe(team, SDOE):
    __name__ = "Copper Compass"


class gboe(team, GBOE):
    __name__ = "Goblet of Thundering Deep"


class ccol(team, CCOL):
    __name__ = "Wine-Stained Tricorne"
