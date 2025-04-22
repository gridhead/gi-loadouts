from pydantic import BaseModel

from ..char import CharName
from ..char.cons import Cons
from ..levl import Level
from ..stat import ATTR, STAT


class BaseStats(BaseModel):
    """
    Set of stats belonging to the base category
    """
    health_points: ATTR = ATTR(stat_name=STAT.health_points, stat_data=0.0)
    attack: ATTR = ATTR(stat_name=STAT.attack, stat_data=0.0)
    defense: ATTR = ATTR(stat_name=STAT.defense, stat_data=0.0)
    elemental_mastery: ATTR = ATTR(stat_name=STAT.elemental_mastery, stat_data=0.0)


class AdvancedStats(BaseModel):
    """
    Set of stats belonging to the advanced category
    """
    critical_rate_perc: ATTR = ATTR(stat_name=STAT.critical_rate_perc, stat_data=5.0)
    critical_damage_perc: ATTR = ATTR(stat_name=STAT.critical_damage_perc, stat_data=50.0)
    healing_bonus_perc: ATTR = ATTR(stat_name=STAT.healing_bonus_perc, stat_data=0.0)
    incoming_healing_bonus_perc: ATTR = ATTR(stat_name=STAT.incoming_healing_bonus_perc, stat_data=0.0)
    energy_recharge_perc: ATTR = ATTR(stat_name=STAT.energy_recharge_perc, stat_data=100.0)
    cooldown_reduction_perc: ATTR = ATTR(stat_name=STAT.cooldown_reduction_perc, stat_data=0.0)
    shield_strength_perc: ATTR = ATTR(stat_name=STAT.shield_strength_perc, stat_data=0.0)


class ElementalStats(BaseModel):
    """
    Set of stats belonging to the elemental category
    """
    damage_bonus_pyro_perc: ATTR = ATTR(stat_name=STAT.damage_bonus_pyro_perc, stat_data=0.0)
    resistance_pyro_perc: ATTR = ATTR(stat_name=STAT.resistance_pyro_perc, stat_data=0.0)
    damage_bonus_hydro_perc: ATTR = ATTR(stat_name=STAT.damage_bonus_hydro_perc, stat_data=0.0)
    resistance_hydro_perc: ATTR = ATTR(stat_name=STAT.resistance_hydro_perc, stat_data=0.0)
    damage_bonus_dendro_perc: ATTR = ATTR(stat_name=STAT.damage_bonus_dendro_perc, stat_data=0.0)
    resistance_dendro_perc: ATTR = ATTR(stat_name=STAT.resistance_dendro_perc, stat_data=0.0)
    damage_bonus_electro_perc: ATTR = ATTR(stat_name=STAT.damage_bonus_electro_perc, stat_data=0.0)
    resistance_electro_perc: ATTR = ATTR(stat_name=STAT.resistance_electro_perc, stat_data=0.0)
    damage_bonus_anemo_perc: ATTR = ATTR(stat_name=STAT.damage_bonus_anemo_perc, stat_data=0.0)
    resistance_anemo_perc: ATTR = ATTR(stat_name=STAT.resistance_anemo_perc, stat_data=0.0)
    damage_bonus_cryo_perc: ATTR = ATTR(stat_name=STAT.damage_bonus_cryo_perc, stat_data=0.0)
    resistance_cryo_perc: ATTR = ATTR(stat_name=STAT.resistance_cryo_perc, stat_data=0.0)
    damage_bonus_geo_perc: ATTR = ATTR(stat_name=STAT.damage_bonus_geo_perc, stat_data=0.0)
    resistance_geo_perc: ATTR = ATTR(stat_name=STAT.resistance_geo_perc, stat_data=0.0)
    damage_bonus_physical_perc: ATTR = ATTR(stat_name=STAT.damage_bonus_physical_perc, stat_data=0.0)
    resistance_physical_perc: ATTR = ATTR(stat_name=STAT.resistance_physical_perc, stat_data=0.0)


class Counting(BaseModel):
    """
    Set of stats for computational purposes
    """
    health_points_perc: ATTR = ATTR(stat_name=STAT.health_points_perc, stat_data=0.0)
    attack_perc: ATTR = ATTR(stat_name=STAT.attack_perc, stat_data=0.0)
    defense_perc: ATTR = ATTR(stat_name=STAT.defense_perc, stat_data=0.0)
    none: ATTR = ATTR(stat_name=STAT.none, stat_data=0.0)


class Addendum(BaseModel):
    """
    Set of stats for delta storage
    """
    addendum_base_health_points: ATTR = ATTR(stat_name=STAT.health_points, stat_data=0.0)
    addendum_plus_health_points: ATTR = ATTR(stat_name=STAT.health_points, stat_data=0.0)
    addendum_base_attack: ATTR = ATTR(stat_name=STAT.attack, stat_data=0.0)
    addendum_plus_attack: ATTR = ATTR(stat_name=STAT.attack, stat_data=0.0)
    addendum_base_defense: ATTR = ATTR(stat_name=STAT.defense, stat_data=0.0)
    addendum_plus_defense: ATTR = ATTR(stat_name=STAT.defense, stat_data=0.0)


class CHAR(BaseStats, AdvancedStats, ElementalStats, Counting, Addendum):
    """
    Character primitive for computational purposes
    """
    name: CharName = ""
    levl: Level = Level.Level_01_20_Rank_0
    cons: Cons = Cons.Constellation_0
    revmap: dict = {
        STAT.health_points: "health_points",
        STAT.health_points_perc: "health_points_perc",
        STAT.attack: "attack",
        STAT.attack_perc: "attack_perc",
        STAT.defense: "defense",
        STAT.defense_perc: "defense_perc",
        STAT.elemental_mastery: "elemental_mastery",
        STAT.critical_rate_perc: "critical_rate_perc",
        STAT.critical_damage_perc: "critical_damage_perc",
        STAT.healing_bonus_perc: "healing_bonus_perc",
        STAT.incoming_healing_bonus_perc: "incoming_healing_bonus_perc",
        STAT.energy_recharge_perc: "energy_recharge_perc",
        STAT.cooldown_reduction_perc: "cooldown_reduction_perc",
        STAT.shield_strength_perc: "shield_strength_perc",
        STAT.damage_bonus_pyro_perc: "damage_bonus_pyro_perc",
        STAT.resistance_pyro_perc: "resistance_pyro_perc",
        STAT.damage_bonus_hydro_perc: "damage_bonus_hydro_perc",
        STAT.resistance_hydro_perc: "resistance_hydro_perc",
        STAT.damage_bonus_dendro_perc: "damage_bonus_dendro_perc",
        STAT.resistance_dendro_perc: "resistance_dendro_perc",
        STAT.damage_bonus_electro_perc: "damage_bonus_electro_perc",
        STAT.resistance_electro_perc: "resistance_electro_perc",
        STAT.damage_bonus_anemo_perc: "damage_bonus_anemo_perc",
        STAT.resistance_anemo_perc: "resistance_anemo_perc",
        STAT.damage_bonus_cryo_perc: "damage_bonus_cryo_perc",
        STAT.resistance_cryo_perc: "resistance_cryo_perc",
        STAT.damage_bonus_geo_perc: "damage_bonus_geo_perc",
        STAT.resistance_geo_perc: "resistance_geo_perc",
        STAT.damage_bonus_physical_perc: "damage_bonus_physical_perc",
        STAT.resistance_physical_perc: "resistance_physical_perc",
        STAT.none: "none"
    }
