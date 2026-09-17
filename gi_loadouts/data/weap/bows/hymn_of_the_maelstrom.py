from ...type.weap import Weap


class HymnOfTheMaelstrom(Weap):
    __weapname__ = "Hymn of the Maelstrom"
    __weapkind__ = "Bow"
    __basestat__ = "ATK"
    __basestat_val__ = 454
    __secstat__ = "Elemental Mastery"
    __secstat_val__ = 209
    __tier__ = 5
    __refistat__ = {
        1: "16.0%",
        2: "18.0%",
        3: "20.0%",
        4: "22.0%",
        5: "24.0%",
    }
    __refilist__ = {
        1: "Increases Elemental Skill DMG by 16.0%. For every 10 Elemental Mastery, increases Elemental Skill DMG by 0.5%, up to 30.0%.",
        2: "Increases Elemental Skill DMG by 18.0%. For every 10 Elemental Mastery, increases Elemental Skill DMG by 0.5%, up to 30.0%.",
        3: "Increases Elemental Skill DMG by 20.0%. For every 10 Elemental Mastery, increases Elemental Skill DMG by 0.5%, up to 30.0%.",
        4: "Increases Elemental Skill DMG by 22.0%. For every 10 Elemental Mastery, increases Elemental Skill DMG by 0.5%, up to 30.0%.",
        5: "Increases Elemental Skill DMG by 24.0%. For every 10 Elemental Mastery, increases Elemental Skill DMG by 0.5%, up to 30.0%.",
    }
