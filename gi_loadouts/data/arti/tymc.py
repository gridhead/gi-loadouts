from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Tiny Miracle"
    __pairdata__ = [
        ATTR(stat_name=STAT.resistance_anemo_perc, stat_data=20),
        ATTR(stat_name=STAT.resistance_cryo_perc, stat_data=20),
        ATTR(stat_name=STAT.resistance_dendro_perc, stat_data=20),
        ATTR(stat_name=STAT.resistance_electro_perc, stat_data=20),
        ATTR(stat_name=STAT.resistance_geo_perc, stat_data=20),
        ATTR(stat_name=STAT.resistance_hydro_perc, stat_data=20),
        ATTR(stat_name=STAT.resistance_pyro_perc, stat_data=20)
    ]
    __pairtext__ = "All Elemental RES increased by 20%"
    __quaddata__ = []
    __quadtext__ = "Incoming elemental DMG increases corresponding Elemental RES by 30% for 10s. Can only occur once every 10s."


class fwol(team, FWOL):
    __name__ = "Tiny Miracle's Flower"


class pmod(team, PMOD):
    __name__ = "Tiny Miracle's Feather"


class sdoe(team, SDOE):
    __name__ = "Tiny Miracle's Hourglass"


class gboe(team, GBOE):
    __name__ = "Tiny Miracle's Goblet"


class ccol(team, CCOL):
    __name__ = "Tiny Miracle's Earrings"
