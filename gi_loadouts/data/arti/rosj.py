from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Resolution of Sojourner"
    __pairdata__ = [ATTR(stat_name=STAT.attack_perc, stat_data=18)]
    __pairtext__ = "ATK +18%"
    __quaddata__ = []
    __quadtext__ = "Increases Charged Attack CRIT Rate by 30%."


class fwol(team, FWOL):
    __name__ = "Heart of Comradeship"


class pmod(team, PMOD):
    __name__ = "Feather of Homecoming"


class sdoe(team, SDOE):
    __name__ = "Sundial of the Sojourner"


class gboe(team, GBOE):
    __name__ = "Goblet of the Sojourner"


class ccol(team, CCOL):
    __name__ = "Crown of Parting"
