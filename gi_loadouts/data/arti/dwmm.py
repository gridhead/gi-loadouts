from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Deepwood Memories"
    __pairdata__ = [ATTR(stat_name=STAT.damage_bonus_dendro_perc, stat_data=15)]
    __pairtext__ = "Dendro DMG Bonus +15%"
    __quaddata__ = []
    __quadtext__ = "After Elemental Skills or Bursts hit opponents, the targets' Dendro RES will be decreased by 30% for 8s. This effect can be triggered even if the equipping character is not on the field."


class fwol(team, FWOL):
    __name__ = "Labyrinth Wayfarer"


class pmod(team, PMOD):
    __name__ = "Scholar of Vines"


class sdoe(team, SDOE):
    __name__ = "A Time of Insight"


class gboe(team, GBOE):
    __name__ = "Lamp of the Lost"


class ccol(team, CCOL):
    __name__ = "Laurel Coronet"
