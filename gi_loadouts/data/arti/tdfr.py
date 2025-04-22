from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Thundering Fury"
    __pairdata__ = [ATTR(stat_name=STAT.damage_bonus_electro_perc, stat_data=15)]
    __pairtext__ = "Electro DMG Bonus +15%"
    __quaddata__ = []
    __quadtext__ = "Increases DMG caused by Overloaded, Electro-Charged, Superconduct, and Hyperbloom by 40%, and the DMG Bonus conferred by Aggravate is increased by 20%. When Quicken or the aforementioned Elemental Reactions are triggered, Elemental Skill CD is decreased by 1s. Can only occur once every 0.8s"


class fwol(team, FWOL):
    __name__ = "Thunderbird's Mercy"


class pmod(team, PMOD):
    __name__ = "Survivor of Catastrophe"


class sdoe(team, SDOE):
    __name__ = "Hourglass of Thunder"


class gboe(team, GBOE):
    __name__ = "Omen of Thunderstorm"


class ccol(team, CCOL):
    __name__ = "Thunder Summoner's Crown"
