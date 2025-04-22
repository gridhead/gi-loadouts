from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Echoes of an Offering"
    __pairdata__ = [ATTR(stat_name=STAT.attack_perc, stat_data=18)]
    __pairtext__ = "ATK +18%"
    __quaddata__ = []
    __quadtext__ = "When Normal Attacks hit opponents, there is a 36% chance that it will trigger Valley Rite, which will increase Normal Attack DMG by 70% of ATK. This effect will be dispelled 0.05s after a Normal Attack deals DMG. If a Normal Attack fails to trigger Valley Rite, the odds of it triggering the next time will increase by 20%. This trigger can occur once every 0.2s."


class fwol(team, FWOL):
    __name__ = "Soulscent Bloom"


class pmod(team, PMOD):
    __name__ = "Jade Leaf"


class sdoe(team, SDOE):
    __name__ = "Symbol of Felicitation"


class gboe(team, GBOE):
    __name__ = "Chalice of the Font"


class ccol(team, CCOL):
    __name__ = "Flowing Rings"
