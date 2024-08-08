from pydantic import BaseModel
from gi_loadouts.type.arti import FWOL, PMOD, CCOL, SDOE, GBOE


class team(BaseModel):
    __team__ = "Adventurer"


class fwol(team, FWOL):
    __name__ = "Adventurer's Flower"


class pmod(team, PMOD):
    __name__ = "Adventurer's Tail Feather"


class sdoe(team, SDOE):
    __name__ = "Adventurer's Pocket Watch"


class gboe(team, GBOE):
    __name__ = "Adventurer's Golden Goblet"


class ccol(team, CCOL):
    __name__ = "Adventurer's Bandana"
