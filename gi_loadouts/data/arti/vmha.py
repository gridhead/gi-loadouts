from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import ATTR, STAT


class team(BaseModel):
    __teamname__ = "Vermillion Hereafter"
    __pairdata__ = [ATTR(stat_name=STAT.attack_perc, stat_data=18)]
    __pairtext__ = "ATK +18%"
    __quaddata__ = []
    __quadtext__ = "After using an Elemental Burst. this character will gain the Nascent Light effect, increasing their ATK by 8% for 16s. When the character's HP decreases, their ATK will further increase by 10%. This increase can occur this way maximum of 4 times. This effect can be triggered once every 0.8s. Nascent Light will be dispelled when the character leaves the field. If an Elemental Burst is used again during the duration of Nascent Light, the original Nascent Light will be dispelled"


class fwol(team, FWOL):
    __name__ = "Flowering Life"


class pmod(team, PMOD):
    __name__ = "Feather of Nascent Light"


class sdoe(team, SDOE):
    __name__ = "Solar Relic"


class gboe(team, GBOE):
    __name__ = "Moment of the Pact"


class ccol(team, CCOL):
    __name__ = "Thundering Poise"
