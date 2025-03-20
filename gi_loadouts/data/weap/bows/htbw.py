from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Bow, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.tier import Tier


class HuntersBow(Bow):
    name: str = "Hunter's Bow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.none, stat_data=0.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_1
    refi_list: list[str] = []
    file: str = "htbw"
