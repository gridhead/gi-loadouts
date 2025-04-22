from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Gladiator's Finale"
    __pairdata__ = [ATTR(stat_name=STAT.attack_perc, stat_data=18)]
    __pairtext__ = "ATK +18%"
    __quaddata__ = []
    __quadtext__ = "If the wielder of this artifact set uses a Sword, Claymore or Polearm, increases their Normal Attack DMG by 35%."


class fwol(team, FWOL):
    __name__ = "Gladiator's Nostalgia"


class pmod(team, PMOD):
    __name__ = "Gladiator's Destiny"


class sdoe(team, SDOE):
    __name__ = "Gladiator's Longing"


class gboe(team, GBOE):
    __name__ = "Gladiator's Intoxication"


class ccol(team, CCOL):
    __name__ = "Gladiator's Triumphus"
