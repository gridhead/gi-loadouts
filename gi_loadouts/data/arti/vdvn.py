from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Viridescent Venerer"
    __pairdata__ = [ATTR(stat_name=STAT.damage_bonus_anemo_perc, stat_data=15)]
    __pairtext__ = "Anemo DMG Bonus +15%"
    __quaddata__ = []
    __quadtext__ = "Increases Swirl reaction DMG dealt by 60%, and Stellar Swirl reaction DMG dealt by 20%. Decreases opponent's Elemental RES to the element infused in the Swirl by 40% for 10s. Upon triggering a Stellar Swirl in the opponent, will also decrease their Cryo RES by 40%. RES debuffs of the same elemental type do not stack."


class fwol(team, FWOL):
    __name__ = "In Remembrance of Viridescent Fields"


class pmod(team, PMOD):
    __name__ = "Viridescent Arrow Feather"


class sdoe(team, SDOE):
    __name__ = "Viridescent Venerer's Determination"


class gboe(team, GBOE):
    __name__ = "Viridescent Venerer's Vessel"


class ccol(team, CCOL):
    __name__ = "Viridescent Venerer's Diadem"
