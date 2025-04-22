from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Vourukasha's Glow"
    __pairdata__ = [ATTR(stat_name=STAT.health_points_perc, stat_data=20)]
    __pairtext__ = "HP +20%"
    __quaddata__ = []
    __quadtext__ = "Elemental Skill and Elemental Burst DMG will be increased by 10%. After the equipping character takes DMG, the aforementioned DMG Bonus is increased by 80% for 5s. This effect increase can have 5 stacks. The duration of each stack is counted independently. These effects can be triggered even when the equipping character is not on the field"


class fwol(team, FWOL):
    __name__ = "Stamen of Khvarena's Origin"


class pmod(team, PMOD):
    __name__ = "Vibrant Pinion"


class sdoe(team, SDOE):
    __name__ = "Ancient Abscission"


class gboe(team, GBOE):
    __name__ = "Feast of Boundless Joy"


class ccol(team, CCOL):
    __name__ = "Heart of Khvarena's Brilliance"
