from gi_loadouts.type.weap import Bow, Catalyst, Sword, Claymore, Polearm
from gi_loadouts.type.weap import WeaponStat, WeaponStatType
from gi_loadouts.type.weap.base.tier import Tier
from gi_loadouts.type.rare import Rare


class AlleyHunter(Bow):
    name: str = "Alley Hunter"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
