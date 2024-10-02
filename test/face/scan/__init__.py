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
}
