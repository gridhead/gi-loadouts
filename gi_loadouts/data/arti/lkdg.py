from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Lucky Dog"
    __pairdata__ = [ATTR(stat_name=STAT.defense, stat_data=100)]
    __pairtext__ = "DEF increased by 100."
    __quaddata__ = []
    __quadtext__ = "Picking up Mora restores 300 HP."


class fwol(team, FWOL):
    __name__ = "Lucky Dog's Clover"


class pmod(team, PMOD):
    __name__ = "Lucky Dog's Eagle Feather"


class sdoe(team, SDOE):
    __name__ = "Lucky Dog's Hourglass"


class gboe(team, GBOE):
    __name__ = "Lucky Dog's Goblet"


class ccol(team, CCOL):
    __name__ = "Lucky Dog's Silver Circlet"
