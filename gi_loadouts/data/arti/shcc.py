from pydantic import BaseModel

from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE


class team(BaseModel):
    __teamname__ = "Scroll of the Hero of Cinder City"
    __pairdata__ = []
    __pairtext__ = "When a nearby party member triggers a Nightsoul Burst, the equipping character regenerates 6 Elemental Energy."
    __quaddata__ = []
    __quadtext__ = "After the equipping character triggers a reaction related to their Elemental Type, all nearby party members gain a 12% Elemental DMG Bonus for the Elemental Types involved in the elemental reaction for 15s. If the equipping character is in the Nightsoul's Blessing state when triggering this effect, all nearby party members gain an additional 28% Elemental DMG Bonus for the Elemental Types involved in the elemental reaction for 20s. The equipping character can trigger this effect while off-field, and the DMG bonus from Artifact Sets with the same name do not stack."


class fwol(team, FWOL):
    __name__ = "Beast Tamer's Talisman"


class pmod(team, PMOD):
    __name__ = "Mountain Ranger's Marker"


class sdoe(team, SDOE):
    __name__ = "Mystic's Gold Dial"


class gboe(team, GBOE):
    __name__ = "Wandering Scholar's Claw Cup"


class ccol(team, CCOL):
    __name__ = "Demon-Warrior's Feather Mask"
