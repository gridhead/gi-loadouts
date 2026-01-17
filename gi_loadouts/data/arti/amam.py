from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Aubade of Morningstar and Moon"
    __pairdata__ = [ATTR(stat_name=STAT.elemental_mastery, stat_data=80)]
    __pairtext__ = "Increases Elemental Mastery by 80."
    __quaddata__ = []
    __quadtext__ = "When the equipping character is off-field, Lunar Reaction DMG is increased by 20%. When the party's Moonsign Level is at least Ascendant Gleam, Lunar Reaction DMG will be further increased by 40%. This effect will disappear after the equipping character is active for 3s."


class fwol(team, FWOL):
    __name__ = "Moonlit Offering's Opulent Dream"


class pmod(team, PMOD):
    __name__ = "Moonlit Offering's Parting Light"


class sdoe(team, SDOE):
    __name__ = "Moonlit Offering's Final Hour"


class gboe(team, GBOE):
    __name__ = "Moonlit Offering's Libation"


class ccol(team, CCOL):
    __name__ = "Moonlit Offering's Silver Crown"
