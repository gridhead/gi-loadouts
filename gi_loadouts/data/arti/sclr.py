from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Scholar"
    __pairdata__ = [ATTR(stat_name=STAT.energy_recharge_perc, stat_data=20)]
    __pairtext__ = "Energy Recharge +20%"
    __quaddata__ = []
    __quadtext__ = "Gaining Energy gives 3 Energy to all party members who have a bow or a catalyst equipped. Can only occurs once every 3s."


class fwol(team, FWOL):
    __name__ = "Scholar's Bookmark"


class pmod(team, PMOD):
    __name__ = "Scholar's Quill Pen"


class sdoe(team, SDOE):
    __name__ = "Scholar's Clock"


class gboe(team, GBOE):
    __name__ = "Scholar's Ink Cup"


class ccol(team, CCOL):
    __name__ = "Scholar's Lens"
