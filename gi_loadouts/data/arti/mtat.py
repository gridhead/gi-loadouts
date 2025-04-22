from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE


class team(BaseModel):
    __teamname__ = "Martial Artist"
    __pairdata__ = []
    __pairtext__ = "Increases Normal Attack and Charged Attack DMG by 15%."
    __quaddata__ = []
    __quadtext__ = "After using Elemental Skill, increases Normal Attack and Charged Attack DMG by 25% for 8s."


class fwol(team, FWOL):
    __name__ = "Martial Artist's Red Flower"


class pmod(team, PMOD):
    __name__ = "Martial Artist's Feather Accessory"


class sdoe(team, SDOE):
    __name__ = "Martial Artist's Water Hourglass"


class gboe(team, GBOE):
    __name__ = "Martial Artist's Wine Cup"


class ccol(team, CCOL):
    __name__ = "Martial Artist's Bandana"
