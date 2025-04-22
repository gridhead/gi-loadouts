from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE


class team(BaseModel):
    __teamname__ = "Long Night's Oath"
    __pairdata__ = []
    __pairtext__ = "Plunging Attack DMG increased by 25%."
    __quaddata__ = []
    __quadtext__ = "After the equipping character's Plunging Attack/Charged Attack/Elemental Skill hits an opponent, they will gain 1/2/2 stack(s) of \"Radiance Everlasting.\" Plunging Attacks, Charged Attacks or Elemental Skills can each trigger this effect once every 1s. Radiance Everlasting: Plunging Attacks deal 15%. increased DMG for 6s. Max 5 stacks. Each stack's duration is counted independently."


class fwol(team, FWOL):
    __name__ = "Lightkeeper's Pledge"


class pmod(team, PMOD):
    __name__ = "Nightingale's Tail Feather"


class sdoe(team, SDOE):
    __name__ = "Undying One's Mourning Bell"


class gboe(team, GBOE):
    __name__ = "A Horn Unwinded"


class ccol(team, CCOL):
    __name__ = "Dyed Tassel"
