from PySide6.QtCore import QMimeData, QUrl
from PySide6.QtWidgets import QDialog

from gi_loadouts.face.util import modify_datatype_to_transfer
from gi_loadouts.type.arti.base import (
    MainStatType_CCOL,
    MainStatType_FWOL,
    MainStatType_GBOE,
    MainStatType_PMOD,
    MainStatType_SDOE,
)
from gi_loadouts.type.stat import ATTR, STAT

__dist__ = {
    "Flower of Life": {"list": MainStatType_FWOL, "part": "fwol"},
    "Plume of Death": {"list": MainStatType_PMOD, "part": "pmod"},
    "Sands of Eon": {"list": MainStatType_SDOE, "part": "sdoe"},
    "Goblet of Eonothem": {"list": MainStatType_GBOE, "part": "gboe"},
    "Circlet of Logos": {"list": MainStatType_CCOL, "part": "ccol"},
}

__text__ = {
    "Flower of Life": """
        Selfless Floral Accessory
        Flower of Life
        HP 4,780
        +20
        DEF+53
        CRIT DMG+14.0%
        DEF+12.4%
        CRIT Rate+6.2%
        Nighttime Whispers in the Echoing Woods:
        2-Piece Set: ATK +18%.
        4-Piece Set: After using an Elemental Skill, gain a 20% Geo DMG Bonus for 10s. While under a shield granted by
        the Crystallize reaction, the above effect will be increased by 150%, and this additional increase disappears
        1s after the shield is lost.
    """,
    "Plume of Death": """
        Shaft of Remembrance
        Plume of Death
        ATK 311
        +20
        CRIT DMG+21.8%
        DEF+21
        CRIT Rate+3.1%
        ATK+21.0%
        Shimenawa's Reminiscence:
        2-Piece Set: ATK +18%.
        4-Piece Set: When casting an Elemental Skill, if the character has 15 or more Energy, they lose 15 Energy and
        Normal/Charged/Plunging Attack DMG is increased by 50% for 10s. This effect will not trigger again during that
        duration.
    """,
    "Sands of Eon": """
        Morning Dew's Moment
        Sands of Eon
        Energy Recharge 51.8%
        +20
        HP+13.4%
        CRIT DMG+21.0%
        Elemental Mastery+23
        CRIT Rate+6.6%
        Shimenawa's Reminiscence:
        2-Piece Set: ATK +18%.
        4-Piece Set: When casting an Elemental Skill, if the character has 15 or more Energy, they lose 15 Energy and
        Normal/Charged/Plunging Attack DMG is increased by 50% for 10s. This effect will not trigger again during that
        duration.
    """,
    "Goblet of Eonothem": """
        Magnanimous Ink Bottle
        Goblet of Eonothem
        Geo DMG Bonus 46.6%
        +20
        HP+568
        DEF+56
        CRIT DMG+5.4%
        ATK+35
        Nighttime Whispers in the Echoing Woods:
        2-Piece Set: ATK +18%.
        4-Piece Set: After using an Elemental Skill, gain a 20% Geo DMG Bonus for 10s. While under a shield granted by
        the Crystallize reaction, the above effect will be increased by 150%, and this additional increase disappears
        1s after the shield is lost.
    """,
    "Circlet of Logos": """
        Witch's Scorching Hat
        Circlet of Logos
        CRIT Rate 31.1%
        +20
        HP+717
        HP+5.8%
        ATK+53
        CRIT DMG+13.2%
        Crimson Witch of Flames:
        2-Piece Set: Pyro DMG Bonus +15%
        4-Piece Set: Increases Overloaded, Burning, and Burgeon DMG by 40%. Increases Vaporize and Melt DMG by 15%.
        Using Elemental Skill increases the 2-Piece Set Bonus by 50% of its starting value for 10s. Max 2 stacks.
    """,
}

__rtrn__ = {
    "Flower of Life": {
        "part": "fwol",
        "team": "Nighttime Whispers in the Echoing Woods",
        "rare": "Star 5",
        "levl": "Level 20",
        "stat": {
            "main": ATTR(stat_name=STAT.health_points, stat_data=4780.0),
            "seco": {
                "a": ATTR(stat_name=STAT.critical_rate_perc, stat_data=6.2),
                "b": ATTR(stat_name=STAT.critical_damage_perc, stat_data=14.0),
                "c": ATTR(stat_name=STAT.defense_perc, stat_data=12.4),
                "d": ATTR(stat_name=STAT.defense, stat_data=53.0),
            },
        },
    },
    "Plume of Death": {
        "part": "pmod",
        "team": "Shimenawa's Reminiscence",
        "rare": "Star 5",
        "levl": "Level 20",
        "stat": {
            "main": ATTR(stat_name=STAT.attack, stat_data=311.0),
            "seco": {
                "a": ATTR(stat_name=STAT.critical_rate_perc, stat_data=3.1),
                "b": ATTR(stat_name=STAT.critical_damage_perc, stat_data=21.8),
                "c": ATTR(stat_name=STAT.attack_perc, stat_data=21.0),
                "d": ATTR(stat_name=STAT.defense, stat_data=21.0),
            },
        },
    },
    "Sands of Eon": {
        "part": "sdoe",
        "team": "Shimenawa's Reminiscence",
        "rare": "Star 5",
        "levl": "Level 20",
        "stat": {
            "main": ATTR(stat_name=STAT.energy_recharge_perc, stat_data=51.8),
            "seco": {
                "a": ATTR(stat_name=STAT.elemental_mastery, stat_data=23.0),
                "b": ATTR(stat_name=STAT.critical_rate_perc, stat_data=6.6),
                "c": ATTR(stat_name=STAT.critical_damage_perc, stat_data=21.0),
                "d": ATTR(stat_name=STAT.health_points_perc, stat_data=13.4),
            },
        },
    },
    "Goblet of Eonothem": {
        "part": "gboe",
        "team": "Nighttime Whispers in the Echoing Woods",
        "rare": "Star 5",
        "levl": "Level 20",
        "stat": {
            "main": ATTR(stat_name=STAT.damage_bonus_geo_perc, stat_data=46.6),
            "seco": {
                "a": ATTR(stat_name=STAT.critical_damage_perc, stat_data=5.4),
                "b": ATTR(stat_name=STAT.health_points, stat_data=568.0),
                "c": ATTR(stat_name=STAT.defense, stat_data=56.0),
                "d": ATTR(stat_name=STAT.attack, stat_data=35.0),
            },
        },
    },
    "Circlet of Logos": {
        "part": "ccol",
        "team": "Crimson Witch of Flames",
        "rare": "Star 5",
        "levl": "Level 20",
        "stat": {
            "main": ATTR(stat_name=STAT.critical_rate_perc, stat_data=31.1),
            "seco": {
                "a": ATTR(stat_name=STAT.critical_damage_perc, stat_data=13.2),
                "b": ATTR(stat_name=STAT.health_points_perc, stat_data=5.8),
                "c": ATTR(stat_name=STAT.health_points, stat_data=717.0),
                "d": ATTR(stat_name=STAT.attack, stat_data=53.0),
            },
        },
    },
}

__rtrn_flty__ = {
    "part": "sdoe",
    "team": "Shimenawa's Reminiscence",
    "rare": "Star 5",
    "levl": "Level 20",
    "stat": {
        "main": ATTR(stat_name=STAT.energy_recharge_perc, stat_data=51.8),
        "seco": {
            "a": ATTR(stat_name=STAT.elemental_mastery, stat_data=23.0),
            "b": ATTR(
                stat_name=STAT.critical_rate_perc, stat_data=modify_datatype_to_transfer(" ")
            ),
            "c": ATTR(stat_name=STAT.critical_damage_perc, stat_data=21.0),
            "d": ATTR(
                stat_name=STAT.health_points_perc, stat_data=modify_datatype_to_transfer("abc")
            ),
        },
    },
}


class MockScanDialog:
    def __init__(self, part: str):
        self.part = part
        self.pair = {
            "fwol": "Flower of Life",
            "pmod": "Plume of Death",
            "sdoe": "Sands of Eon",
            "gboe": "Goblet of Eonothem",
            "ccol": "Circlet of Logos",
        }

    def exec(self):
        return QDialog.Accepted

    def keep_info(self) -> dict:
        dist = self.pair[self.part]
        return __rtrn__[dist]


class MockIncident:
    def __init__(self, path: str):
        self.data = QMimeData()
        self.data.setUrls([QUrl.fromLocalFile(path)])

    def mimeData(self) -> QMimeData:
        return self.data


class MockMistakenIncident:
    def __init__(self):
        self.data = QMimeData()
        self.data.setHtml("")

    def mimeData(self) -> QMimeData:
        return self.data


class MockScanWorker:
    def __init__(self, parent):
        self.parent = parent

    def moveToThread(self, thread):
        raise ValueError("Please select an accurate screenshot.")
