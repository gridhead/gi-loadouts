from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Sword, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.tier import Tier


class DullBlade(Sword):
    name: str = "Dull Blade"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.none, stat_data=0.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_1
    refi_list: list[str] = []
    file: str = "dlbd"
