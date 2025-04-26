from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE


class team(BaseModel):
    __teamname__ = "None"
    __pairdata__ = []
    __pairtext__ = ""
    __quaddata__ = []
    __quadtext__ = ""


class fwol(team, FWOL):
    __name__ = "None"


class pmod(team, PMOD):
    __name__ = "None"


class sdoe(team, SDOE):
    __name__ = "None"


class gboe(team, GBOE):
    __name__ = "None"


class ccol(team, CCOL):
    __name__ = "None"
