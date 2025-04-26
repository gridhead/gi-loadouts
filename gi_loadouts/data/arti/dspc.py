from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Desert Pavilion Chronicle"
    __pairdata__ = [ATTR(stat_name=STAT.damage_bonus_anemo_perc, stat_data=15)]
    __pairtext__ = "Anemo DMG Bonus +15%."
    __quaddata__ = []
    __quadtext__ = "When Charged Attacks hit opponents, the equipping character's Normal Attack SPD will increase by 10% while Normal, Charged, and Plunging Attack DMG will increase by 40% for 15s."


class fwol(team, FWOL):
    __name__ = "The First Days of the City of Kings"


class pmod(team, PMOD):
    __name__ = "End of the Golden Realm"


class sdoe(team, SDOE):
    __name__ = "Timepiece of the Lost Path"


class gboe(team, GBOE):
    __name__ = "Defender of the Enchanting Dream"


class ccol(team, CCOL):
    __name__ = "Legacy of the Desert High-Born"
