from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Silken Moon's Serenade"
    __pairdata__ = [ATTR(stat_name=STAT.energy_recharge_perc, stat_data=20)]
    __pairtext__ = "Energy Recharge +20%"
    __quaddata__ = []
    __quadtext__ = "When dealing Elemental DMG, gain the Gleaming Moon: Devotion effect for 8s: Increases all party members' Elemental Mastery by 60/120 when the party's Moonsign is Nascent Gleam/Ascendant Gleam. The equipping character can trigger this effect while off-field. All party members' Lunar Reaction DMG is increased by 10% for each different Gleaming Moon effect that party members have. Effects from Gleaming Moon cannot stack."


class fwol(team, FWOL):
    __name__ = "Crystal Tear of the Wanderer"


class pmod(team, PMOD):
    __name__ = "Pristine Plume of the Blessed"


class sdoe(team, SDOE):
    __name__ = "Frost Devotee’s Delirium"


class gboe(team, GBOE):
    __name__ = "Joyous Glory of the Pure"


class ccol(team, CCOL):
    __name__ = "Holy Crown of the Believer"
