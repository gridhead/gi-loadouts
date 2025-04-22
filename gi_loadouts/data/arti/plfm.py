from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Pale Flame"
    __pairdata__ = [ATTR(stat_name=STAT.damage_bonus_physical_perc, stat_data=25)]
    __pairtext__ = "Physical DMG +25%"
    __quaddata__ = []
    __quadtext__ = "When an Elemental Skill hits an opponent, ATK is increased by 9% for 7s. This effect stacks up to 2 times and can be triggered once every 0.3s. Once 2 stacks are reached, the 2-set effect is increased by 100%."


class fwol(team, FWOL):
    __name__ = "Stainless Bloom"


class pmod(team, PMOD):
    __name__ = "Wise Doctor's Pinion"


class sdoe(team, SDOE):
    __name__ = "Moment of Cessation"


class gboe(team, GBOE):
    __name__ = "Surpassing Cup"


class ccol(team, CCOL):
    __name__ = "Mocking Mask"
