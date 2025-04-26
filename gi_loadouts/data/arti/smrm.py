from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Shimenawa's Reminiscence"
    __pairdata__ = [ATTR(stat_name=STAT.attack_perc, stat_data=18)]
    __pairtext__ = "ATK +18%"
    __quaddata__ = []
    __quadtext__ = "When casting an Elemental Skill, if the character has 15 or more Energy, they lose 15 Energy and Normal/Charged/Plunging Attack DMG is increased by 50% for 10s."


class fwol(team, FWOL):
    __name__ = "Entangling Bloom"


class pmod(team, PMOD):
    __name__ = "Shaft of Remembrance"


class sdoe(team, SDOE):
    __name__ = "Morning Dew's Moment"


class gboe(team, GBOE):
    __name__ = "Hopeful Heart"


class ccol(team, CCOL):
    __name__ = "Capricious Visage"
