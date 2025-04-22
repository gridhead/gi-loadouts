from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Traveling Doctor"
    __pairdata__ = [ATTR(stat_name=STAT.incoming_healing_bonus_perc, stat_data=20)]
    __pairtext__ = "Increases incoming healing by 20%."
    __quaddata__ = []
    __quadtext__ = "Using Elemental Burst restores 20% HP."


class fwol(team, FWOL):
    __name__ = "Traveling Doctor's Silver Lotus"


class pmod(team, PMOD):
    __name__ = "Traveling Doctor's Owl Feather"


class sdoe(team, SDOE):
    __name__ = "Traveling Doctor's Pocket Watch"


class gboe(team, GBOE):
    __name__ = "Traveling Doctor's Medicine Pot"


class ccol(team, CCOL):
    __name__ = "Traveling Doctor's Handkerchief"
