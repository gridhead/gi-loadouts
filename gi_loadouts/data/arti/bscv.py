from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Bloodstained Chivalry"
    __pairdata__ = [ATTR(stat_name=STAT.damage_bonus_physical_perc, stat_data=25)]
    __pairtext__ = "Physical DMG +25%"
    __quaddata__ = []
    __quadtext__ = "After defeating an opponent, increases Charged Attack DMG by 50%, and reduces its Stamina cost to 0 for 10s."


class fwol(team, FWOL):
    __name__ = "Bloodstained Flower of Iron"


class pmod(team, PMOD):
    __name__ = "Bloodstained Black Plume"


class sdoe(team, SDOE):
    __name__ = "Bloodstained Final Hour"


class gboe(team, GBOE):
    __name__ = "Bloodstained Chevalier's Goblet"


class ccol(team, CCOL):
    __name__ = "Bloodstained Iron Mask"
