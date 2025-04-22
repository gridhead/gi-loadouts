from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Emblem of Severed Fate"
    __pairdata__ = [ATTR(stat_name=STAT.energy_recharge_perc, stat_data=20)]
    __pairtext__ = "Energy Recharge +20%"
    __quaddata__ = []
    __quadtext__ = "Increases Elemental Burst DMG by 25% of Energy Recharge. A maximum of 75% bonus DMG can be obtained in this way."


class fwol(team, FWOL):
    __name__ = "Magnificent Tsuba"


class pmod(team, PMOD):
    __name__ = "Sundered Feather"


class sdoe(team, SDOE):
    __name__ = "Storm Cage"


class gboe(team, GBOE):
    __name__ = "Scarlet Vessel"


class ccol(team, CCOL):
    __name__ = "Ornate Kabuto"
