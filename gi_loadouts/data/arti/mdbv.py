from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Maiden Beloved"
    __pairdata__ = [ATTR(stat_name=STAT.healing_bonus_perc, stat_data=15)]
    __pairtext__ = "Character Healing Effectiveness +15%"
    __quaddata__ = []
    __quadtext__ = "Using an Elemental Skill or Burst increases healing received by all party members by 20% for 10s."


class fwol(team, FWOL):
    __name__ = "Maiden's Distant Love"


class pmod(team, PMOD):
    __name__ = "Maiden's Heart-Stricken Infatuation"


class sdoe(team, SDOE):
    __name__ = "Maiden's Passing Youth"


class gboe(team, GBOE):
    __name__ = "Maiden's Fleeting Leisure"


class ccol(team, CCOL):
    __name__ = "Maiden's Fading Beauty"
