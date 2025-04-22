from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Unfinished Reverie"
    __pairdata__ = [ATTR(stat_name=STAT.attack_perc, stat_data=18)]
    __pairtext__ = "ATK +18%"
    __quaddata__ = []
    __quadtext__ = "After leaving combat for 3s, DMG dealt increased by 50%. In combat, if no Burning opponents are nearby for more than 6s, this DMG Bonus will decrease by 10% per second until it reaches 0%. When a Burning opponent exists, it will increase by 10% instead until it reaches 50%. This effect still triggers if the equipping character is off-field"


class fwol(team, FWOL):
    __name__ = "Dark Fruit of Bright Flowers"


class pmod(team, PMOD):
    __name__ = "Faded Emerald Tail"


class sdoe(team, SDOE):
    __name__ = "Moment of Attainment"


class gboe(team, GBOE):
    __name__ = "The Wine-Flask Over Which the Plan Was Hatched"


class ccol(team, CCOL):
    __name__ = "Crownless Crown"
