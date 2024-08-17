from typing import List

from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Sword, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.base.tier import Tier


class HarbingerofDawn(Sword):
    name: str = "Harbinger of Dawn"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=10.2)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_3
    refi_name: str = "Vigorous"
    refi_list: List[str] = [
        "When HP is above 90%, increases CRIT Rate by 14%.",
        "When HP is above 90%, increases CRIT Rate by 17.5%.",
        "When HP is above 90%, increases CRIT Rate by 21%.",
        "When HP is above 90%, increases CRIT Rate by 24.5%.",
        "When HP is above 90%, increases CRIT Rate by 28%.",
    ]
