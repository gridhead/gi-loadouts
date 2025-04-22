from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Fragment of Harmonic Whimsy"
    __pairdata__ = [ATTR(stat_name=STAT.attack_perc, stat_data=18)]
    __pairtext__ = "ATK +18%"
    __quaddata__ = []
    __quadtext__ = "When the value of a Bond of Life increases or decreases, this character deals 18% increased DMG for 6s. Max 3 stacks."


class fwol(team, FWOL):
    __name__ = "Harmonious Symphony Prelude"


class pmod(team, PMOD):
    __name__ = "Ancient Sea's Nocturnal Musing"


class sdoe(team, SDOE):
    __name__ = "The Grand Jape of the Turning of Fate"


class gboe(team, GBOE):
    __name__ = "Ichor Shower Rhapsody"


class ccol(team, CCOL):
    __name__ = "Whimsical Dance of the Withered"
