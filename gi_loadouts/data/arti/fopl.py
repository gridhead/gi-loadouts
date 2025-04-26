from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Flower of Paradise Lost"
    __pairdata__ = [ATTR(stat_name=STAT.elemental_mastery, stat_data=80)]
    __pairtext__ = "Increases Elemental Mastery by 80."
    __quaddata__ = []
    __quadtext__ = "The equipping character's Bloom, Hyperbloom, and Burgeon reaction DMG are increased by 40%. Additionally, after the equipping character triggers Bloom, Hyperbloom, or Burgeon, they will gain another 25% bonus to the effect mentioned prior. Each stack of this lasts 10s. Max 4 stacks simultaneously. This effect can only be triggered once per second. The character who equips this can still trigger its effects when not on the field."


class fwol(team, FWOL):
    __name__ = "Ay-Khanoum's Myriad"


class pmod(team, PMOD):
    __name__ = "Wilting Feast"


class sdoe(team, SDOE):
    __name__ = "A Moment Congealed"


class gboe(team, GBOE):
    __name__ = "Secret-Keeper's Magic Bottle"


class ccol(team, CCOL):
    __name__ = "Amethyst Crown"
