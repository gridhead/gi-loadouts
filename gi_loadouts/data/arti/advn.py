from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Adventurer"
    __pairdata__ = [ATTR(stat_name=STAT.health_points, stat_data=1000)]
    __pairtext__ = "Max HP increased by 1,000."
    __quaddata__ = []
    __quadtext__ = "Opening chest regenerates 30% Max HP over 5s."


class fwol(team, FWOL):
    __name__ = "Adventurer's Flower"


class pmod(team, PMOD):
    __name__ = "Adventurer's Tail Feather"


class sdoe(team, SDOE):
    __name__ = "Adventurer's Pocket Watch"


class gboe(team, GBOE):
    __name__ = "Adventurer's Golden Goblet"


class ccol(team, CCOL):
    __name__ = "Adventurer's Bandana"
