from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Nymph's Dream"
    __pairdata__ = [ATTR(stat_name=STAT.damage_bonus_hydro_perc, stat_data=15)]
    __pairtext__ = "Hydro DMG Bonus +15%"
    __quaddata__ = []
    __quadtext__ = "After Normal, Charged, and Plunging Attacks, Elemental Skills, and Elemental Bursts hit opponents. 1 stack of Mirrored Nymph will triggered, lasting 8s. When under the effect of 1, 2, or 3 or more Mirrored Nymph stacks, ATK will be increased by 7%/16%/25%, and Hydro DMG will be increased by 4%/9%/15% Mirrored Nymph created by Normal, Charged, and Plunging Attacks, Elemental Skills, and Elemental Bursts exist independently."


class fwol(team, FWOL):
    __name__ = "Odyssean Flower"


class pmod(team, PMOD):
    __name__ = "Wicked Mage's Plumule"


class sdoe(team, SDOE):
    __name__ = "Nymph's Constancy"


class gboe(team, GBOE):
    __name__ = "Heroes' Tea Party"


class ccol(team, CCOL):
    __name__ = "Fell Dragon's Monocle"
