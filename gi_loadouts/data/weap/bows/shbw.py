from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SeasonedHuntersBow(Bow):
    name: str = "Seasoned Hunter's Bow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.none, stat_data=0.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_2
    refi_list: list[str] = []
    file: str = "shbw"
