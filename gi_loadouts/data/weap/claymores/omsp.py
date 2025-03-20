from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Claymore, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.tier import Tier


class OldMercsPal(Claymore):
    name: str = "Old Merc's Pal"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.none, stat_data=0.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_2
    refi_list: list[str] = []
    file: str = "omsp"
