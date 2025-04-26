from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Finale of the Deep Galleries"
    __pairdata__ = [ATTR(stat_name=STAT.damage_bonus_cryo_perc, stat_data=15)]
    __pairtext__ = "Cryo DMG Bonus +15%"
    __quaddata__ = []
    __quadtext__ = "When the equipping Character has 0 Elemental Energy, Normal Attack DMG is increased by 60% and Elemental Burst DMG is increased by 60%. After the equipping character deals Normal Attack DMG, the aforementioned Elemental Burst effect will stop applying for 6s. After the equipping character deals Elemental Burst DMG, the aforementioned Normal Attack effect will stop applying for 6s. This effect can trigger even if the equipping character is off the field."


class fwol(team, FWOL):
    __name__ = "Deep Gallery's Echoing Song"


class pmod(team, PMOD):
    __name__ = "Deep Gallery's Distant Pact"


class sdoe(team, SDOE):
    __name__ = "Deep Gallery's Moment of Oblivion"


class gboe(team, GBOE):
    __name__ = "Deep Gallery's Bestowed Banquet"


class ccol(team, CCOL):
    __name__ = "Deep Gallery's Lost Crown"
