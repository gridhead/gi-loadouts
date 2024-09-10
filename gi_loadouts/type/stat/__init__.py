from enum import Enum
from typing import Optional

from pydantic import BaseModel


class STAT(str, Enum):
    """
    Set of statistics possible
    """
    attack = "ATK"
    attack_perc = "ATK %"
    defense = "DEF"
    defense_perc = "DEF %"
    health_points = "HP"
    health_points_perc = "HP %"
    elemental_mastery = "Elemental Mastery"
    energy_recharge_perc = "Energy Recharge"
    damage_bonus_geo_perc = "Geo DMG Bonus"
    resistance_geo_perc = "Geo RES"
    damage_bonus_pyro_perc = "Pyro DMG Bonus"
    resistance_pyro_perc = "Pyro RES"
    damage_bonus_cryo_perc = "Cryo DMG Bonus"
    resistance_cryo_perc = "Cryo RES"
    damage_bonus_anemo_perc = "Anemo DMG Bonus"
    resistance_anemo_perc = "Anemo RES"
    damage_bonus_hydro_perc = "Hydro DMG Bonus"
    resistance_hydro_perc = "Hydro RES"
    damage_bonus_dendro_perc = "Dendro DMG Bonus"
    resistance_dendro_perc = "Dendro RES"
    damage_bonus_electro_perc = "Electro DMG Bonus"
    resistance_electro_perc = "Electro RES"
    damage_bonus_physical_perc = "Physical DMG Bonus"
    resistance_physical_perc = "Physical RES"
    critical_rate_perc = "Crit Rate"
    critical_damage_perc = "Crit DMG"
    incoming_healing_bonus_perc = "Incoming Healing Bonus"
    healing_bonus_perc = "Healing Bonus"
    shield_strength_perc = "Shield Strength"
    cooldown_reduction_perc = "CD Reduction"
    none = "None"


class ATTR(BaseModel):
    """
    Attribute primitive
    """
    stat_name: Optional[STAT] = STAT.none
    stat_data: Optional[float] = 0.0


__revmap__ = {
    "ATK": STAT.attack,
    "ATK %": STAT.attack_perc,
    "DEF": STAT.defense,
    "DEF %": STAT.defense_perc,
    "HP": STAT.health_points,
    "HP %": STAT.health_points_perc,
    "Elemental Mastery": STAT.elemental_mastery,
    "Energy Recharge": STAT.energy_recharge_perc,
    "Geo DMG Bonus": STAT.damage_bonus_geo_perc,
    "Geo RES": STAT.resistance_geo_perc,
    "Pyro DMG Bonus": STAT.damage_bonus_pyro_perc,
    "Pyro RES": STAT.resistance_pyro_perc,
    "Cryo DMG Bonus": STAT.damage_bonus_cryo_perc,
    "Cryo RES": STAT.resistance_cryo_perc,
    "Anemo DMG Bonus": STAT.damage_bonus_anemo_perc,
    "Anemo RES": STAT.resistance_anemo_perc,
    "Hydro DMG Bonus": STAT.damage_bonus_hydro_perc,
    "Hydro RES": STAT.resistance_hydro_perc,
    "Dendro DMG Bonus": STAT.damage_bonus_dendro_perc,
    "Dendro RES": STAT.resistance_dendro_perc,
    "Electro DMG Bonus": STAT.damage_bonus_electro_perc,
    "Electro RES": STAT.resistance_electro_perc,
    "Physical DMG Bonus": STAT.damage_bonus_physical_perc,
    "Physical RES": STAT.resistance_physical_perc,
    "Crit Rate": STAT.critical_rate_perc,
    "Crit DMG": STAT.critical_damage_perc,
    "Incoming Healing Bonus": STAT.incoming_healing_bonus_perc,
    "Healing Bonus": STAT.healing_bonus_perc,
    "Shield Strength": STAT.shield_strength_perc,
    "CD Reduction": STAT.cooldown_reduction_perc,
    "None": STAT.none
}
