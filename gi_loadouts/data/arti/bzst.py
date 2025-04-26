from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Blizzard Strayer"
    __pairdata__ = [ATTR(stat_name=STAT.damage_bonus_cryo_perc, stat_data=15)]
    __pairtext__ = "Cryo DMG Bonus +15%."
    __quaddata__ = []
    __quadtext__ = "When a character attacks an enemy affected by Cryo, their CRIT Rate is increased by 20%. If the enemy is Frozen, CRIT Rate is increased by an additional 20%."


class fwol(team, FWOL):
    __name__ = "Snowswept Memory"


class pmod(team, PMOD):
    __name__ = "Icebreaker's Resolve"


class sdoe(team, SDOE):
    __name__ = "Frozen Homeland's Demise"


class gboe(team, GBOE):
    __name__ = "Frost-Weaved Dignity"


class ccol(team, CCOL):
    __name__ = "Broken Rime's Echo"
