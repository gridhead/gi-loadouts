from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Heart of the Furnace"
    __pairdata__ = [ATTR(stat_name=STAT.attack_perc, stat_data=18)]
    __pairtext__ = "ATK +18%"
    __quaddata__ = []
    __quadtext__ = "Increases the equipping character's ATK by 12% for 12s when they trigger a Stellar Glimmer reaction or deal Stellar Glimmer reaction DMG. Also increases Stellar Glimmer reaction DMG dealt by all nearby party members by 50%. The above effects can trigger even when the equipping character is not on the field, and the DMG bonus from multiple Artifact Sets with the same name do not stack."


class fwol(team, FWOL):
    __name__ = "Foundryman's Conjecture"


class pmod(team, PMOD):
    __name__ = "Foundryman's Observation"


class sdoe(team, SDOE):
    __name__ = "Foundryman's Calculus"


class gboe(team, GBOE):
    __name__ = "Foundryman's Magnanimity"


class ccol(team, CCOL):
    __name__ = "Foundryman's Legacy"
