from enum import Enum
from typing import Optional

from pydantic import BaseModel

from ..stat import ATTR, STAT


class MainStatType_FWOL(Enum):
    """
    Set of mainstats possible for artifacts belonging from the "Flower of Life" area
    """
    health_points = STAT.health_points
    none = STAT.none


class MainStatType_PMOD(Enum):
    """
    Set of mainstats possible for artifacts belonging from the "Plume of Death" area
    """
    attack = STAT.attack
    none = STAT.none


class MainStatType_SDOE(Enum):
    """
    Set of mainstats possible for artifacts belonging from the "Sands of Eon" area
    """
    attack_perc = STAT.attack_perc
    defense_perc = STAT.defense_perc
    health_points_perc = STAT.health_points_perc
    elemental_mastery = STAT.elemental_mastery
    energy_recharge_perc = STAT.energy_recharge_perc
    none = STAT.none


class MainStatType_GBOE(Enum):
    """
    Set of mainstats possible for artifacts belonging from the "Goblet of Eonothem" area
    """
    attack_perc = STAT.attack_perc
    defense_perc = STAT.defense_perc
    health_points_perc = STAT.health_points_perc
    elemental_mastery = STAT.elemental_mastery
    damage_bonus_geo_perc = STAT.damage_bonus_geo_perc
    damage_bonus_pyro_perc = STAT.damage_bonus_pyro_perc
    damage_bonus_cryo_perc = STAT.damage_bonus_cryo_perc
    damage_bonus_anemo_perc = STAT.damage_bonus_anemo_perc
    damage_bonus_hydro_perc = STAT.damage_bonus_hydro_perc
    damage_bonus_dendro_perc = STAT.damage_bonus_dendro_perc
    damage_bonus_electro_perc = STAT.damage_bonus_electro_perc
    damage_bonus_physical_perc = STAT.damage_bonus_physical_perc
    none = STAT.none


class MainStatType_CCOL(Enum):
    """
    Set of mainstats possible for artifacts belonging from the "Circlet of Logos" area
    """
    attack_perc = STAT.attack_perc
    defense_perc = STAT.defense_perc
    health_points_perc = STAT.health_points_perc
    healing_bonus_perc = STAT.healing_bonus_perc
    elemental_mastery = STAT.elemental_mastery
    critical_rate_perc = STAT.critical_rate_perc
    critical_damage_perc = STAT.critical_damage_perc
    none = STAT.none


class SecoStatType(Enum):
    """
    Set of possible secondary stat types in an artifact
    """
    attack = STAT.attack
    attack_perc = STAT.attack_perc
    defense = STAT.defense
    defense_perc = STAT.defense_perc
    health_points = STAT.health_points
    health_points_perc = STAT.health_points_perc
    elemental_mastery = STAT.elemental_mastery
    energy_recharge_perc = STAT.energy_recharge_perc
    critical_rate_perc = STAT.critical_rate_perc
    critical_damage_perc = STAT.critical_damage_perc
    none = STAT.none


class SecoStat(BaseModel):
    """
    Data class for secondary stat of an artifact
    """
    stat_name: Optional[SecoStatType] = SecoStatType.none
    stat_data: Optional[float] = 0


class Artifact(BaseModel):
    """
    Artifact primitive
    """
    __teamname__: str = ""
    __pairdata__: list[ATTR] = []
    __pairtext__: str = ""
    __quaddata__: list[ATTR] = []
    __quadtext__: str = ""
    levl: Optional[int] = 0
    rare: Optional[int] = 1
