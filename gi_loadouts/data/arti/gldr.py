from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Gilded Dreams"
    __pairdata__ = [ATTR(stat_name=STAT.elemental_mastery, stat_data=80)]
    __pairtext__ = "Elemental Mastery +80"
    __quaddata__ = []
    __quadtext__ = "Within 8s of triggering an Elemental Reaction, the character equipping this will obtain buffs based on the Elemental Type of the other party members, ATK is increased by 14% for each party member whose Elemental Type is the same as the equipping character, and Elemental Mastery is increased by 50 for every party member with a different Elemental Type. Each of the aforementioned buffs will count up to 3 characters. This effect can be triggered once every 8s. The character who equips this can still trigger its effects when not on the field."


class fwol(team, FWOL):
    __name__ = "Dreaming Steelbloom"


class pmod(team, PMOD):
    __name__ = "Feather of Judgment"


class sdoe(team, SDOE):
    __name__ = "The Sunken Years"


class gboe(team, GBOE):
    __name__ = "Honeyed Final Feast"


class ccol(team, CCOL):
    __name__ = "Shadow of the Sand King"
