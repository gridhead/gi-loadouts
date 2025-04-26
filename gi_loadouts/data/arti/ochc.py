from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Ocean-Hued Clam"
    __pairdata__ = [ATTR(stat_name=STAT.healing_bonus_perc, stat_data=15)]
    __pairtext__ = "Healing Bonus +15%"
    __quaddata__ = []
    __quadtext__ = "When the character equipping this artifact set heals a character in the party, a Sea-Dyed Foam will appear for 3 seconds, accumulating the amount of HP recovered from healing (including overflow healing). At the end of the duration, the Sea-Dyed Foam will explode, dealing DMG to nearby opponents based on 90% of the accumulated healing. (This DMG is calculated similarly to Reactions such as Electro-Charged, and Superconduct, but it is not affected by Elemental Mastery, Character Levels, or Reaction DMG Bonuses). Only one Sea-Dyed Foam can be produced every 3.5 seconds. Each Sea-Dyed Foam can accumulate up to 30,000 HP (including overflow healing). There can be no more than one Sea-Dyed Foam active at any given time. This effect can still be triggered even when the character who is using this artifact set is not on the field."


class fwol(team, FWOL):
    __name__ = "Sea-Dyed Blossom"


class pmod(team, PMOD):
    __name__ = "Deep Palace's Plume"


class sdoe(team, SDOE):
    __name__ = "Cowry of Parting"


class gboe(team, GBOE):
    __name__ = "Pearl Cage"


class ccol(team, CCOL):
    __name__ = "Crown of Watatsumi"
