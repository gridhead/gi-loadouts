from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE


class team(BaseModel):
    __teamname__ = "Noblesse Oblige"
    __pairdata__ = []
    __pairtext__ = "Elemental Burst DMG +20%"
    __quaddata__ = []
    __quadtext__ = "Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack."


class fwol(team, FWOL):
    __name__ = "Royal Flora"


class pmod(team, PMOD):
    __name__ = "Royal Plume"


class sdoe(team, SDOE):
    __name__ = "Royal Pocket Watch"


class gboe(team, GBOE):
    __name__ = "Royal Silver Urn"


class ccol(team, CCOL):
    __name__ = "Royal Masque"
