from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE


class team(BaseModel):
    __teamname__ = "Gambler"
    __pairdata__ = []
    __pairtext__ = "Elemental Skill DMG increased by 20%"
    __quaddata__ = []
    __quadtext__ = "Defeating an enemy has 100% chance to remove Elemental Skill CD. Can only occur once every 15s."


class fwol(team, FWOL):
    __name__ = "Gambler's Brooch"


class pmod(team, PMOD):
    __name__ = "Gambler's Feather Accessory"


class sdoe(team, SDOE):
    __name__ = "Gambler's Pocket Watch"


class gboe(team, GBOE):
    __name__ = "Gambler's Dice Cup"


class ccol(team, CCOL):
    __name__ = "Gambler's Earrings"
