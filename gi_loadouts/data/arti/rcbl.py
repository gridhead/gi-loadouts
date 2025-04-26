from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Retracing Bolide"
    __pairdata__ = [ATTR(stat_name=STAT.shield_strength_perc, stat_data=35)]
    __pairtext__ = "Increases Shield Strength by 35%."
    __quaddata__ = []
    __quadtext__ = "While protected by a shield, gain an additional 40% Normal and Charged Attack DMG."


class fwol(team, FWOL):
    __name__ = "Summer Night's Bloom"


class pmod(team, PMOD):
    __name__ = "Summer Night's Finale"


class sdoe(team, SDOE):
    __name__ = "Summer Night's Moment"


class gboe(team, GBOE):
    __name__ = "Summer Night's Waterballoon"


class ccol(team, CCOL):
    __name__ = "Summer Night's Mask"
