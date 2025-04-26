from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Lavawalker"
    __pairdata__ = [ATTR(stat_name=STAT.resistance_pyro_perc, stat_data=40)]
    __pairtext__ = "Pyro RES increased by 40%"
    __quaddata__ = []
    __quadtext__ = "Increases DMG against enemies that are Burning or affected by Pyro by 35%."


class fwol(team, FWOL):
    __name__ = "Lavawalker's Resolution"


class pmod(team, PMOD):
    __name__ = "Lavawalker's Salvation"


class sdoe(team, SDOE):
    __name__ = "Lavawalker's Torment"


class gboe(team, GBOE):
    __name__ = "Lavawalker's Epiphany"


class ccol(team, CCOL):
    __name__ = "Lavawalker's Wisdom"
