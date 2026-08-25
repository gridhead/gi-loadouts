from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Scarlet Proof"
    __pairdata__ = [ATTR(stat_name=STAT.attack_perc, stat_data=18)]
    __pairtext__ = "ATK +18%."
    __quaddata__ = []
    __quadtext__ = "Increases the equipping character's CRIT Rate by 16%, and their Stellar Swirl reaction dealt by 40%, for 10s after they trigger a Stellar Swirl reaction."


class fwol(team, FWOL):
    __name__ = "Honor to Your Devotion"


class pmod(team, PMOD):
    __name__ = "Glory to Your Legacy"


class sdoe(team, SDOE):
    __name__ = "Time Gifted Unto You"


class gboe(team, GBOE):
    __name__ = "Chalice of Your Blood and Sorrow"


class ccol(team, CCOL):
    __name__ = "Testament to Your Faith"
