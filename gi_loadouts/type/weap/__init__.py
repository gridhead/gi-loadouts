from enum import Enum
from typing import Optional

from pydantic import BaseModel

from ..levl import Level
from ..rare import Rare
from ..stat import STAT
from .ascn import Ascn
from .mult import Mult, MultSeco
from .tier import Tier


class WeaponStatType(Enum):
    """
    Set of possible statistics associated with a weapon
    """
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
    """
    Data class for statistics of a weapon
    """
    stat_name: Optional[WeaponStatType] = WeaponStatType.none
    stat_data: Optional[float] = 0


class WeaponType(str, Enum):
    """
    Set of weapon types
    """
    bow = "Bow"
    catalyst = "Catalyst"
    claymore = "Claymore"
    polearm = "Polearm"
    sword = "Sword"
    none = "none"


class Refinement(BaseModel):
    """
    Refinement primitive
    """
    qant: int = 1
    stat: list[WeaponStat] = []
    data: str = ""


class Weapon(BaseModel):
    """
    Weapon primitive
    """
    name: str = ""
    type: Optional[WeaponType] = WeaponType.none
    levl: Optional[Level] = Level.Level_01_20_Rank_0
    tier: Optional[Tier] = Tier.Tier_1
    rare: Optional[Rare] = Rare.Star_1
    stat_list: list[WeaponStat] = []
    refi_list: list[str] = []
    refi_stat: list[WeaponStat] = []
    file: str = ""

    @property
    def refinement(self) -> dict:
        refiobjc = dict()
        for indx in range(len(self.refi_list)):
            refiobjc[f"Refinement {indx + 1}"] = Refinement(
                qant=indx+1,
                data=self.refi_list[indx],
                stat=self.refi_stat[indx] if len(self.refi_stat) > 0 else [],
            )
        return refiobjc

    @property
    def main_stat(self) -> WeaponStat:
        """
        Calculate the statistics associated with the mainstat of a weapon

        :return: Statistics associated with the weapon
        """
        base = self.tier.value["rare"][self.rare.value.qant]

        if self.rare in [Rare.Star_1, Rare.Star_2]:
            mult = Mult[Rare.Star_3][self.levl.value.qant].data[self.tier]
        elif self.file == "sods" and self.name == "Sword of Descension":
            """
            `Sword of Descension` is a special weapon. Although it is a 4-Star rarity weapon which
            uses the 4-Star ascension value, it actually uses 3-Star Tier 2 base value and
            multipliers.

            Although this is an anti-pattern and we do not generally support such kinds of
            development, we have implemented this specific calculation to ensure the displayed
            values are accurate for users.
            """
            base = Tier.Tier_2.value["rare"][Rare.Star_3.value.qant]
            mult = Mult[Rare.Star_3][self.levl.value.qant].data[self.tier]
        else:
            mult = Mult[self.rare][self.levl.value.qant].data[self.tier]

        ascn = Ascn[self.rare].data[self.levl.value.rank]
        calc = (base * mult) + ascn
        return WeaponStat(stat_name=WeaponStatType.attack, stat_data=calc)

    @property
    def levl_bind(self) -> list:
        """
        Calculate the level limit possible for the weapon based on the rarity

        Weapons of qualities 1 Star and 2 Star can only be leveled up to "Level 70/70 Rank 4"

        :return: List of possible levels possible for the weapon
        """
        bind = {
            Rare.Star_1: 74,
            Rare.Star_2: 74,
            Rare.Star_3: 96,
            Rare.Star_4: 96,
            Rare.Star_5: 96,
        }
        return [item for indx, item in enumerate(Level) if indx < bind[self.rare]]

    @property
    def seco_stat_calc(self) -> WeaponStat:
        """
        Calculate the statistics associated with the secondary stat of the character based on its level

        :return: Secondary statistics associated with the weapon
        """
        stat_data = self.seco_stat.stat_data
        if self.seco_stat.stat_name != WeaponStatType.none:
            stat_data = stat_data * MultSeco[self.levl.value.qant - (self.levl.value.qant % 5)]
        return WeaponStat(stat_name=self.seco_stat.stat_name, stat_data=stat_data)


class Bow(Weapon):
    """
    Weapon directive of "Bow" type
    """
    type: str = WeaponType.bow


class Catalyst(Weapon):
    """
    Weapon directive of "Catalyst" type
    """
    type: str = WeaponType.catalyst


class Claymore(Weapon):
    """
    Weapon directive of "Claymore" type
    """
    type: str = WeaponType.claymore


class Polearm(Weapon):
    """
    Weapon directive of "Polearm" type
    """
    type: str = WeaponType.polearm


class Sword(Weapon):
    """
    Weapon directive of "Sword" type
    """
    type: str = WeaponType.sword
