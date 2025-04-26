from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class PrototypeCrescent(Bow):
    name: str = "Prototype Crescent"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Unreturning"
    refi_list: list[str] = [
            "Charged Attack hits on weak points increase Movement SPD by 10% and ATK by 36% for 10s.",
            "Charged Attack hits on weak points increase Movement SPD by 10% and ATK by 45% for 10s.",
            "Charged Attack hits on weak points increase Movement SPD by 10% and ATK by 54% for 10s.",
            "Charged Attack hits on weak points increase Movement SPD by 10% and ATK by 63% for 10s.",
            "Charged Attack hits on weak points increase Movement SPD by 10% and ATK by 72% for 10s.",
        ]
    file: str = "ptct"
