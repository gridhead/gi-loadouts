from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Song of Days Past"
    __pairdata__ = [ATTR(stat_name=STAT.healing_bonus_perc, stat_data=15)]
    __pairtext__ = "Healing Bonus +15%"
    __quaddata__ = []
    __quadtext__ = "When the equipping character heals a party member, the Yearning effect will be created for 6s, which records the total amount of healing provided (including overflow healing). When the duration expires, the Yearning effect will be transformed into the \"Waves of Days Past\" effect: When your active party member hits an opponent with a Normal Attack, Charged Attack, Plunging Attack, Elemental Skill, or Elemental Burst, the DMG dealt will be increased by 8% of the total healing amount recorded by the Yearning effect. The \"Waves of Days Past\" effect is removed after it has taken effect 5 times or after 10s. A single instance of the Yearning effect can record up to 15,000 healing, and only a single instance can exist at once, but it can record the healing from multiple equipping characters. Equipping characters on standby can still trigger this effect."


class fwol(team, FWOL):
    __name__ = "Forgotten Oath of Days Past"


class pmod(team, PMOD):
    __name__ = "Recollection of Days Past"


class sdoe(team, SDOE):
    __name__ = "Echoing Sound From Days Past"


class gboe(team, GBOE):
    __name__ = "Promised Dream of Days Past"


class ccol(team, CCOL):
    __name__ = "Poetry of Days Past"
