from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Thundersoother"
    __pairdata__ = [ATTR(stat_name=STAT.resistance_electro_perc, stat_data=40)]
    __pairtext__ = "Electro RES increased by 40%"
    __quaddata__ = []
    __quadtext__ = "Increases DMG against opponents affected by Electro by 35%."


class fwol(team, FWOL):
    __name__ = "Thundersoother's Heart"


class pmod(team, PMOD):
    __name__ = "Thundersoother's Plume"


class sdoe(team, SDOE):
    __name__ = "Hour of Soothing Thunder"


class gboe(team, GBOE):
    __name__ = "Thundersoother's Goblet"


class ccol(team, CCOL):
    __name__ = "Thundersoother's Diadem"
