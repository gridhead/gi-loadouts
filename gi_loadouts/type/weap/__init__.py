from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from gi_loadouts.type.stat import STAT
from gi_loadouts.type.levl import Level
from gi_loadouts.type.weap.base.tier import Tier
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap.base.mult import Mult, MultSeco
from gi_loadouts.type.weap.base.ascn import Ascn


class WeaponStatType(Enum):
    attack = STAT.attack
    attack_perc = STAT.attack_perc
    defense_perc = STAT.defense_perc
    health_points_perc = STAT.health_points_perc
    elemental_mastery = STAT.elemental_mastery
    energy_recharge_perc = STAT.energy_recharge_perc
    critical_rate_perc = STAT.critical_rate_perc
    critical_damage_perc = STAT.critical_damage_perc
    damage_bonus_physical_perc = STAT.damage_bonus_physical_perc
    damage_bonus_anemo_perc = STAT.damage_bonus_anemo_perc
    damage_bonus_cryo_perc = STAT.damage_bonus_cryo_perc
    damage_bonus_dendro_perc = STAT.damage_bonus_dendro_perc
    damage_bonus_electro_perc = STAT.damage_bonus_electro_perc
    damage_bonus_geo_perc = STAT.damage_bonus_geo_perc
    damage_bonus_hydro_perc = STAT.damage_bonus_hydro_perc
    damage_bonus_pyro_perc = STAT.damage_bonus_pyro_perc
    shield_strength_perc = STAT.shield_strength_perc
    healing_bonus_perc = STAT.healing_bonus_perc
    none = STAT.none


class WeaponStat(BaseModel):
    stat_name: Optional[WeaponStatType] = WeaponStatType.none
    stat_data: Optional[float] = 0


class WeaponType(str, Enum):
    bow = "Bow"
    catalyst = "Catalyst"
    claymore = "Claymore"
    polearm = "Polearm"
    sword = "Sword"
    none = "none"


class Weapon(BaseModel):
    name: str
    type: Optional[WeaponType] = WeaponType.none
    levl: Optional[Level] = Level.Level_01_20_Rank_0
    tier: Optional[Tier] = Tier.Tier_1
    rare: Optional[Rare] = Rare.Star_1
    refinement: Optional[int] = 1
    stat_list: List[WeaponStat] = []
    refi_list: List[str] = []
    refi_stat: List[WeaponStat] = []
    refi_name: str = ""

    @property
    def main_stat(self):
        base = self.tier.value["rare"][self.rare.value]

        if self.rare in [Rare.Star_1, Rare.Star_2]:
            mult = Mult[Rare.Star_3][self.levl.value.qant].data[self.tier]
        else:
            mult = Mult[self.rare][self.levl.value.qant].data[self.tier]

        ascn = Ascn[self.rare].data[self.levl.value.rank]
        calc = (base * mult) + ascn
        return WeaponStat(stat_name=WeaponStatType.attack, stat_data=calc)

    @property
    def levl_bind(self):
        bind = {
            Rare.Star_1: 74,
            Rare.Star_2: 74,
            Rare.Star_3: 96,
            Rare.Star_4: 96,
            Rare.Star_5: 96,
        }
        return [item for indx, item in enumerate(Level) if indx < bind[self.rare]]

    @property
    def seco_stat_calc(self):
        stat_data = self.seco_stat.stat_data
        if self.seco_stat.stat_name != WeaponStatType.none:
            stat_data = stat_data * MultSeco[self.levl.value.qant - (self.levl.value.qant % 5)]
        return WeaponStat(stat_name=self.seco_stat.stat_name, stat_data=stat_data)


class Bow(Weapon):
    type: str = WeaponType.bow


class Catalyst(Weapon):
    type: str = WeaponType.catalyst


class Claymore(Weapon):
    type: str = WeaponType.claymore


class Polearm(Weapon):
    type: str = WeaponType.polearm


class Sword(Weapon):
    type: str = WeaponType.sword
