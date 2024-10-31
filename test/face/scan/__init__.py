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
                "d": ATTR(stat_name=STAT.defense, stat_data=53.0)
            }
        }
    },
    "Plume of Death": {
        "part": "pmod",
        "team": "Shimenawa's Reminiscence",
        "rare": "Star 5",
        "levl": "Level 18",
        "stat": {
            "main": ATTR(stat_name=STAT.attack, stat_data=285.0),
            "seco": {
                "a": ATTR(stat_name=STAT.critical_rate_perc, stat_data=3.1),
                "b": ATTR(stat_name=STAT.critical_damage_perc, stat_data=21.8),
                "c": ATTR(stat_name=STAT.attack_perc, stat_data=21.0),
                "d": ATTR(stat_name=STAT.defense, stat_data=21.0)
            }
        }
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
                "d": ATTR(stat_name=STAT.health_points_perc, stat_data=13.4)
            }
        }
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
                "d": ATTR(stat_name=STAT.attack, stat_data=35.0)
            }
        }
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
                "d": ATTR(stat_name=STAT.attack, stat_data=53.0)
            }
        }
    }
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
            "b": ATTR(stat_name=STAT.critical_rate_perc, stat_data=modify_datatype_to_transfer(" ")),
            "c": ATTR(stat_name=STAT.critical_damage_perc, stat_data=21.0),
            "d": ATTR(stat_name=STAT.health_points_perc, stat_data=modify_datatype_to_transfer("abc"))
        }
    }
}


class MockScanDialog:
    def exec(self):
        return QDialog.Accepted


class MockScanDialogFWOL(MockScanDialog):
    def __init__(self, part: str = "fwol") -> None:
        self.part = part

    def keep_info(self) -> dict:
        return __rtrn__["Flower of Life"]


class MockScanDialogPMOD(MockScanDialog):
    def __init__(self, part: str = "pmod") -> None:
        self.part = part

    def keep_info(self) -> dict:
        return __rtrn__["Plume of Death"]


class MockScanDialogSDOE(MockScanDialog):
    def __init__(self, part: str = "sdoe") -> None:
        self.part = part

    def keep_info(self) -> dict:
        return __rtrn__["Sands of Eon"]


class MockScanDialogGBOE(MockScanDialog):
    def __init__(self, part: str = "gboe") -> None:
        self.part = part

    def keep_info(self) -> dict:
        return __rtrn__["Goblet of Eonothem"]


class MockScanDialogCCOL(MockScanDialog):
    def __init__(self, part: str = "ccol") -> None:
        self.part = part

    def keep_info(self) -> dict:
        return __rtrn__["Circlet of Logos"]


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
