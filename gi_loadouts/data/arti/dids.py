from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Disenchantment in Deep Shadow"
    __pairdata__ = [ATTR(stat_name=STAT.attack_perc, stat_data=18)]
    __pairtext__ = "ATK +18%."
    __quaddata__ = []
    __quadtext__ = "Increases Superconduct Reaction DMG by 80%. When the wielder attacks opponents affected by Superconduct, this attack's CRIT Rate is increased by 16%. An all-new blessing may be obtained as you make your way toward Snezhnaya..."


class fwol(team, FWOL):
    __name__ = "Iridescence That Ceased Amidst Glory"


class pmod(team, PMOD):
    __name__ = "Sharpness That Ceased Upon Wondrous Creation"


class sdoe(team, SDOE):
    __name__ = "Moment That Ceased Upon Waking From Grand Dreams"


class gboe(team, GBOE):
    __name__ = "Ovations That Ceased Upon Festivity"


class ccol(team, CCOL):
    __name__ = "Pendulum That Ceased Amidst a Great Fall"
