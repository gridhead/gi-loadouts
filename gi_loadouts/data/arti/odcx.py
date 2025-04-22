from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE


class team(BaseModel):
    __teamname__ = "Obsidian Codex"
    __pairdata__ = []
    __pairtext__ = "While the equipping character is in Nightsoul's Blessing and is on the field, their DMG dealt is increased by 15%."
    __quaddata__ = []
    __quadtext__ = "After the equipping character consumes 1 Nightsoul point while on the field, CRIT Rate increases by 40% for 6s. This effect can trigger once every second."


class fwol(team, FWOL):
    __name__ = "Reckoning of the Xenogenic"


class pmod(team, PMOD):
    __name__ = "Root of the Spirit-Marrow"


class sdoe(team, SDOE):
    __name__ = "Myths of the Night Realm"


class gboe(team, GBOE):
    __name__ = "Pre-Banquet of the Contenders"


class ccol(team, CCOL):
    __name__ = "Crown of the Saints"
