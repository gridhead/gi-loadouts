from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Defender's Will"
    __pairdata__ = [ATTR(stat_name=STAT.defense_perc, stat_data=30)]
    __pairtext__ = "Base DEF +30%"
    __quaddata__ = []
    __quadtext__ = "Increases Elemental RES by 30% for each element present in the party."


class fwol(team, FWOL):
    __name__ = "Guardian's Flower"


class pmod(team, PMOD):
    __name__ = "Guardian's Sigil"


class sdoe(team, SDOE):
    __name__ = "Guardian's Clock"


class gboe(team, GBOE):
    __name__ = "Guardian's Vessel"


class ccol(team, CCOL):
    __name__ = "Guardian's Band"
