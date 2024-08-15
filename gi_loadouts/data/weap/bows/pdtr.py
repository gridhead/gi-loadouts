from typing import List

from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Bow, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.base.tier import Tier


class Predator(Bow):
    name: str = "Predator"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_list: List[str] = [

    ]
