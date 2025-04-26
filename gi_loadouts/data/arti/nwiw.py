from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Nighttime Whispers in the Echoing Woods"
    __pairdata__ = [ATTR(stat_name=STAT.attack_perc, stat_data=18)]
    __pairtext__ = "ATK +18%"
    __quaddata__ = []
    __quadtext__ = "After using an Elemental Skill, gain a 20% Geo DMG Bonus for 10s. While under a shield granted by the Crystallize reaction, the above effect will be increased by 150%, and this additional increase disappears 1s after that shield is lost."


class fwol(team, FWOL):
    __name__ = "Selfless Floral Accessory"


class pmod(team, PMOD):
    __name__ = "Honest Quill"


class sdoe(team, SDOE):
    __name__ = "Faithful Hourglass"


class gboe(team, GBOE):
    __name__ = "Magnanimous Ink Bottle"


class ccol(team, CCOL):
    __name__ = "Compassionate Ladies' Hat"
