from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Night of the Sky's Unveiling"
    __pairdata__ = [ATTR(stat_name=STAT.elemental_mastery, stat_data=80)]
    __pairtext__ = "Elemental Mastery +80"
    __quaddata__ = []
    __quadtext__ = "When nearby party members trigger Lunar Reactions, if the equipping character is on the field, gain the Gleaming Moon: Intent effect for 4s: Increases CRIT Rate by 15%/30% when the party's Moonsign is Nascent Gleam/Ascendant Gleam. All party members' Lunar Reaction DMG is increased by 10% for each different Gleaming Moon effect that party members have. Effects from Gleaming Moon cannot stack."


class fwol(team, FWOL):
    __name__ = "Bloom of the Mind's Desire"


class pmod(team, PMOD):
    __name__ = "Feather of Indelible Sin"


class sdoe(team, SDOE):
    __name__ = "Revelation's Toll"


class gboe(team, GBOE):
    __name__ = "Vessel of Plenty"


class ccol(team, CCOL):
    __name__ = "Crown of the Befallen"
