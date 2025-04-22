from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE


class team(BaseModel):
    __teamname__ = "Marechaussee Hunter"
    __pairdata__ = []
    __pairtext__ = "Normal and Charged Attack DMG +15%."
    __quaddata__ = []
    __quadtext__ = "When current HP increases or decreases, CRIT Rate will be increased by 12% for 5s. Max 3 stacks."


class fwol(team, FWOL):
    __name__ = "Hunter's Brooch"


class pmod(team, PMOD):
    __name__ = "Masterpiece's Overture"


class sdoe(team, SDOE):
    __name__ = "Moment of Judgment"


class gboe(team, GBOE):
    __name__ = "Forgotten Vessel"


class ccol(team, CCOL):
    __name__ = "Veteran's Visage"
