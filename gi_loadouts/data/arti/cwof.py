from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Crimson Witch of Flames"
    __pairdata__ = [ATTR(stat_name=STAT.damage_bonus_pyro_perc, stat_data=15)]
    __pairtext__ = "Pyro DMG Bonus +15%"
    __quaddata__ = []
    __quadtext__ = "Increases Overloaded and Burning DMG by 40%. Increases Vaporize and Melt DMG by 15%. Using an Elemental Skill increases 2-Piece Set effects by 50% for 10s. Max 3 stacks."


class fwol(team, FWOL):
    __name__ = "Witch's Flower of Blaze"


class pmod(team, PMOD):
    __name__ = "Witch's Ever-Burning Plume"


class sdoe(team, SDOE):
    __name__ = "Witch's End Time"


class gboe(team, GBOE):
    __name__ = "Witch's Heart Flames"


class ccol(team, CCOL):
    __name__ = "Witch's Scorching Hat"
