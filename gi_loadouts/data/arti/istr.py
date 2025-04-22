from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Instructor"
    __pairdata__ = [ATTR(stat_name=STAT.elemental_mastery, stat_data=80)]
    __pairtext__ = "Increases Elemental Mastery by 80."
    __quaddata__ = []
    __quadtext__ = "After using Elemental Skill, increases all party members' Elemental Mastery by 120 for 8s."


class fwol(team, FWOL):
    __name__ = "Instructor's Brooch"


class pmod(team, PMOD):
    __name__ = "Instructor's Feather Accessory"


class sdoe(team, SDOE):
    __name__ = "Instructor's Pocket Watch"


class gboe(team, GBOE):
    __name__ = "Instructor's Tea Cup"


class ccol(team, CCOL):
    __name__ = "Instructor's Cap"
