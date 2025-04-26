from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Husk of Opulent Dreams"
    __pairdata__ = [ATTR(stat_name=STAT.defense_perc, stat_data=30)]
    __pairtext__ = "DEF +30%"
    __quaddata__ = []
    __quadtext__ = "A character equipped with this Artifact set will obtain the Curiosity effect in the following conditions: When on the field, the character gains 1 stack after hitting an opponent with a Geo attack, triggering a maximum of once every 0.3s. When off the field, the character gains 1 stack every 3s. Curiosity can stack up to 4 times, each providing 6% DEF and a 6% Geo DMG Bonus. When 6 seconds pass without gaining a Curiosity stack, 1 stack is lost."


class fwol(team, FWOL):
    __name__ = "Bloom Times"


class pmod(team, PMOD):
    __name__ = "Plume of Luxury"


class sdoe(team, SDOE):
    __name__ = "Song of Life"


class gboe(team, GBOE):
    __name__ = "Calabash of Awakening"


class ccol(team, CCOL):
    __name__ = "Skeletal Hat"
