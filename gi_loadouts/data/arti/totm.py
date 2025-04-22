from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Tenacity of the Millelith"
    __pairdata__ = [ATTR(stat_name=STAT.health_points_perc, stat_data=20)]
    __pairtext__ = "HP +20%"
    __quaddata__ = []
    __quadtext__ = "When an Elemental Skill hits an opponent, the ATK of all nearby party members is increased by 20% and their Shield Strength is increased by 30% for 3s. This effect can be triggered once every 0.5s. This effect can still be triggered even when the character who is using this artifact set is not on the field."


class fwol(team, FWOL):
    __name__ = "Flower of Accolades"


class pmod(team, PMOD):
    __name__ = "Ceremonial War-Plume"


class sdoe(team, SDOE):
    __name__ = "Orichalceous Time-Dial"


class gboe(team, GBOE):
    __name__ = "Noble's Pledging Vessel"


class ccol(team, CCOL):
    __name__ = "General's Ancient Helm"
