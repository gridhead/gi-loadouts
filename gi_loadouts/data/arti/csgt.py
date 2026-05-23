from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Celestial Gift"
    __pairdata__ = [ATTR(stat_name=STAT.energy_recharge_perc, stat_data=20)]
    __pairtext__ = "Energy Recharge +20%."
    __quaddata__ = []
    __quadtext__ = "If the equipping character has completed Witch's Homework, after they use an Elemental Skill, they also gain \"Light's Guidance\" for 20s: All nearby party members gain a 20% Elemental DMG Bonus corresponding to the equipping character's Elemental Type. The equipping character can trigger this effect while off-field. DMG Bonuses provided by Artifact Sets with the same name do not stack. When your party has the Hexerei: Secret Rite effect, Light's Guidance is upgraded to \"Mortal Hymn\": All nearby party members gain a 40% Elemental DMG Bonus corresponding to both the equipping character and the current active party member's Elemental Type instead. If both characters have the same Elemental Type, these bonuses will not stack."


class fwol(team, FWOL):
    __name__ = "Heavensent Fragrance"


class pmod(team, PMOD):
    __name__ = "Heavensent Demise"


class sdoe(team, SDOE):
    __name__ = "Heavensent Decree"


class gboe(team, GBOE):
    __name__ = "Heavensent Reward"


class ccol(team, CCOL):
    __name__ = "Heavensent Crown"
