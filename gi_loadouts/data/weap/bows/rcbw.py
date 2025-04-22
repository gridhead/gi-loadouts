from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class RecurveBow(Bow):
    name: str = "Recurve Bow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=10.2)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_3
    refi_name: str = "Cull the Weak"
    refi_list: list[str] = [
            "Defeating an opponent restores 8% HP.",
            "Defeating an opponent restores 10% HP.",
            "Defeating an opponent restores 12% HP.",
            "Defeating an opponent restores 14% HP.",
            "Defeating an opponent restores 16% HP.",
        ]
    file: str = "rcbw"
