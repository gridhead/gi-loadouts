from ...data.arti import ArtiList
from ...data.weap import Family
from ..arti import ArtiLevl
from ..stat import STAT

__stat_good__ = {
    STAT.health_points: "hp",
    STAT.health_points_perc: "hp_",
    STAT.attack: "atk",
    STAT.attack_perc: "atk_",
    STAT.defense: "def",
    STAT.defense_perc: "def_",
    STAT.elemental_mastery: "eleMas",
    STAT.energy_recharge_perc: "enerRech_",
    STAT.healing_bonus_perc: "heal_",
    STAT.critical_rate_perc: "critRate_",
    STAT.critical_damage_perc: "critDMG_",
    STAT.damage_bonus_physical_perc: "physical_dmg_",
    STAT.damage_bonus_anemo_perc: "anemo_dmg_",
    STAT.damage_bonus_cryo_perc: "cryo_dmg_",
    STAT.damage_bonus_dendro_perc: "dendro_dmg_",
    STAT.damage_bonus_electro_perc: "electro_dmg_",
    STAT.damage_bonus_geo_perc: "geo_dmg_",
    STAT.damage_bonus_hydro_perc: "hydro_dmg_",
    STAT.damage_bonus_pyro_perc: "pyro_dmg_",
    STAT.none: "none"
}

__stat_good_revmap__ = {
    data: item for item, data in __stat_good__.items()
}

__artiarea_good__ = {
    "FWOL": "flower",
    "PMOD": "plume",
    "SDOE": "sands",
    "GBOE": "goblet",
    "CCOL": "circlet",
}

__artiarea_good_revmap__ = {
    data: item for item, data in __artiarea_good__.items()
}

__artilist_good__ = {
    item.value.name: "".join([item.title() for item in item.value.name.replace("'", "").replace("-", " ").split(" ")]) for item in ArtiList
}

__artilist_good_revmap__ = {
    data: item for item, data in __artilist_good__.items()
}

__artilevl_good__ = {
    item: getattr(ArtiLevl, f"Level_0{item}" if item < 10 else f"Level_{item}") for item in range(21)
}

__weaplist_good__ = {
    item: "".join([word.title() for word in item.replace("'", "").replace("\"", "").replace("-", " ").split(" ")]) for weap in Family.values() for item in weap.keys()
}

__weaplist_good_revmap__ = {
    data: item for item, data in __weaplist_good__.items()
}

__ascn_bond__ = {
    0: 20,
    1: 40,
    2: 50,
    3: 60,
    4: 70,
    5: 80,
    6: 90,
}
