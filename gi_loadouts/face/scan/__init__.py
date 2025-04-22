from ...data.arti import ArtiList
from ...type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from ...type.stat import STAT

areaiden = {
    FWOL: "Flower of Life",
    PMOD: "Plume of Death",
    SDOE: "Sands of Eon",
    GBOE: "Goblet of Eonothem",
    CCOL: "Circlet of Logos",
}

teamiden = {
    item.value.name: {
        "name": item.value.name.split(" "),
        "dist": {
            "Flower of Life": item.value.fwol.__name__.split(" "),
            "Plume of Death": item.value.pmod.__name__.split(" "),
            "Sands of Eon": item.value.sdoe.__name__.split(" "),
            "Goblet of Eonothem": item.value.gboe.__name__.split(" "),
            "Circlet of Logos": item.value.ccol.__name__.split(" "),
        }
    } for item in ArtiList
}

"""
It is crucial for the absolute HP, DEF and ATK units to be superseded by relative HP%, DEF% and
ATK% units as the expression with the absolute units match the regular expression for the relative
units but not vice versa. Therefore, it is strongly recommended to start with a more stringent
regular expression comparison and proceed to more general ones while ensuring that the parts of the
string that match the regular expression are removed to prevent duplicates.

For eg. `ATK+6.9%` can be seen as `ATK+6` (absolute unit) and `ATK+6.9%` (relative unit)
"""

substats = {
    r".*Elemental\s*Mastery\+[0-9]+.*": STAT.elemental_mastery,
    r".*Energy\s*Recharge\+[0-9]*\.[0-9]+%.*": STAT.energy_recharge_perc,
    r".*CRIT\s*Rate\+[0-9]*\.[0-9]+%.*": STAT.critical_rate_perc,
    r".*CRIT\s*DMG\+[0-9]*\.[0-9]+%.*": STAT.critical_damage_perc,
    r".*HP\+[0-9]*\.[0-9]+%.*": STAT.health_points_perc,
    r".*ATK\+[0-9]*\.[0-9]+%.*": STAT.attack_perc,
    r".*DEF\+[0-9]*\.[0-9]+%.*": STAT.defense_perc,
    r".*HP\+[0-9]+.*": STAT.health_points,
    r".*DEF\+[0-9]+.*": STAT.defense,
    r".*ATK\+[0-9]+.*": STAT.attack,
}

mainstat = {
    "Flower of Life": {
        r".*HP.*": STAT.health_points
    },
    "Plume of Death": {
        r".*ATK.*": STAT.attack,
    },
    "Sands of Eon": {
        r".*Elemental\s*Mastery.*": STAT.elemental_mastery,
        r".*Energy\s*Recharge.*": STAT.energy_recharge_perc,
        r".*HP.*": STAT.health_points_perc,
        r".*DEF.*": STAT.defense_perc,
        r".*ATK.*": STAT.attack_perc,
    },
    "Goblet of Eonothem": {
        r".*Anemo\s*DMG\s*Bonus.*": STAT.damage_bonus_anemo_perc,
        r".*Cryo\s*DMG\s*Bonus.*": STAT.damage_bonus_cryo_perc,
        r".*Dendro\s*DMG\s*Bonus.*": STAT.damage_bonus_dendro_perc,
        r".*Electro\s*DMG\s*Bonus.*": STAT.damage_bonus_electro_perc,
        r".*Geo\s*DMG\s*Bonus.*": STAT.damage_bonus_geo_perc,
        r".*Hydro\s*DMG\s*Bonus.*": STAT.damage_bonus_hydro_perc,
        r".*Pyro\s*DMG\s*Bonus.*": STAT.damage_bonus_pyro_perc,
        r".*Physical\s*DMG\s*Bonus.*": STAT.damage_bonus_physical_perc,
        r".*Elemental\s*Mastery.*": STAT.elemental_mastery,
        r".*HP.*": STAT.health_points_perc,
        r".*DEF.*": STAT.defense_perc,
        r".*ATK.*": STAT.attack_perc,
    },
    "Circlet of Logos": {
        r".*Elemental\s*Mastery.*": STAT.elemental_mastery,
        r".*Healing\s*Points.*": STAT.healing_bonus_perc,
        r".*CRIT\s*Rate.*": STAT.critical_rate_perc,
        r".*CRIT\s*DMG.*": STAT.critical_damage_perc,
        r".*HP.*": STAT.health_points_perc,
        r".*DEF.*": STAT.defense_perc,
        r".*ATK.*": STAT.attack_perc,
    }
}

levliden = r"\+([0-9]|1[0-9]|20)\b"

# List of widgets present in artifact information panel
info_arti_widget = [
    "arti_dist",
    "arti_type",
    "arti_levl",
    "arti_rare",
    "arti_name_main",
    "arti_data_main",
    "arti_name_a",
    "arti_data_a",
    "arti_name_b",
    "arti_data_b",
    "arti_name_c",
    "arti_data_c",
    "arti_name_d",
    "arti_data_d"
]

# List of widgets present in return back panel
back_arti_widget = [
    "arti_back_done",
    "arti_back_wipe"
]

# List of widgets present in right sidebar
right_sidebar_widget = [
    "arti_cnvs_load",
    "arti_cnvs_conf",
    "arti_cnvs_wipe"
]

# List of unpacked widgets arranged as per chronological `TAB` order
tab_order_scan = [
    *info_arti_widget,
    *back_arti_widget,
    *right_sidebar_widget
]
