from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Archaic Petra"
    __pairdata__ = [ATTR(stat_name=STAT.damage_bonus_geo_perc, stat_data=15)]
    __pairtext__ = "Gain a 15% Geo DMG Bonus."
    __quaddata__ = []
    __quadtext__ = "Upon obtaining an Elemental Shard created through a Crystallize Reaction, all party members gain a 35% DMG Bonus for that particular element for 10s. Only one form of Elemental DMG Bonus can be gained in this manner at any one time."


class fwol(team, FWOL):
    __name__ = "Flower of Creviced Cliff"


class pmod(team, PMOD):
    __name__ = "Feather of Jagged Peaks"


class sdoe(team, SDOE):
    __name__ = "Sundial of Enduring Jade"


class gboe(team, GBOE):
    __name__ = "Goblet of Chiseled Crag"


class ccol(team, CCOL):
    __name__ = "Mask of Solitude Basalt"
