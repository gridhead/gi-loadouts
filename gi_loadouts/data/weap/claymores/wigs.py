from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class WhiteIronGreatsword(Claymore):
    name: str = "White Iron Greatsword"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=9.6)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_3
    refi_name: str = "Cull the Weak"
    refi_list: list[str] = [
        "Defeating an opponent restores 8% HP.",
        "Defeating an opponent restores 10% HP.",
        "Defeating an opponent restores 12% HP.",
        "Defeating an opponent restores 14% HP.",
        "Defeating an opponent restores 16% HP.",
    ]
    file: str = "wigs"
