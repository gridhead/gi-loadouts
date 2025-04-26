from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Wanderer's Troupe"
    __pairdata__ = [ATTR(stat_name=STAT.elemental_mastery, stat_data=80)]
    __pairtext__ = "Increases Elemental Mastery by 80"
    __quaddata__ = []
    __quadtext__ = "Increases Charged Attack DMG by 35% if the character uses a Catalyst or Bow"


class fwol(team, FWOL):
    __name__ = "Troupe's Dawnlight"


class pmod(team, PMOD):
    __name__ = "Bard's Arrow Feather"


class sdoe(team, SDOE):
    __name__ = "Concert's Final Hour"


class gboe(team, GBOE):
    __name__ = "Wanderer's String-Kettle"


class ccol(team, CCOL):
    __name__ = "Conductor's Top Hat"
