from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "A Day Carved From Rising Winds"
    __pairdata__ = [ATTR(stat_name=STAT.attack_perc, stat_data=18)]
    __pairtext__ = "ATK +18%"
    __quaddata__ = []
    __quadtext__ = "After a Normal Attack, Charged Attack, Elemental Skill or Elemental Burst hits an opponent, gain the Blessing of Pastoral Winds effect for 6s: ATK is increased by 25%. If the equipping character has completed Witch's Homework, Blessing of Pastoral Winds will be upgraded to Resolve of Pastoral Winds, which also increases the CRIT Rate of the equipping character by an additional 20%. This effect can be triggered even when the character is off-field."


class fwol(team, FWOL):
    __name__ = "Windborne Flower's Spruchdichtung"


class pmod(team, PMOD):
    __name__ = "Dawn's Brilliant Oath"


class sdoe(team, SDOE):
    __name__ = "A Note in Spring's Leich"


class gboe(team, GBOE):
    __name__ = "Heldenepos's Unspoken Tale"


class ccol(team, CCOL):
    __name__ = "Minnesang of Love and Lament"
