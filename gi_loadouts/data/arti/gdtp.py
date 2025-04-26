from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE


class team(BaseModel):
    __teamname__ = "Golden Troupe"
    __pairdata__ = []
    __pairtext__ = "Increases Elemental Skill DMG by 20%."
    __quaddata__ = []
    __quadtext__ = "Increases Elemental Skill DMG by 25%. Additionally, when not on the field, Elemental Skill DMG will be further increased by 25%. This effect will be cleared 2s after taking the field."


class fwol(team, FWOL):
    __name__ = "Golden Song's Variation"


class pmod(team, PMOD):
    __name__ = "Golden Bird's Shedding"


class sdoe(team, SDOE):
    __name__ = "Golden Era's Prelude"


class gboe(team, GBOE):
    __name__ = "Golden Night's Bustle"


class ccol(team, CCOL):
    __name__ = "Golden Troupe's Reward"
