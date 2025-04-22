from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class CompoundBow(Bow):
    name: str = "Compound Bow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.damage_bonus_physical_perc, stat_data=15.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Infusion Arrow"
    refi_list: list[str] = [
        "Normal Attack and Charged Attack hits increase ATK by 4% and Normal ATK SPD by 1.2% for 6s. Max 4 stacks. Can only occur once every 0.3s.",
        "Normal Attack and Charged Attack hits increase ATK by 5% and Normal ATK SPD by 1.5% for 6s. Max 4 stacks. Can only occur once every 0.3s.",
        "Normal Attack and Charged Attack hits increase ATK by 6% and Normal ATK SPD by 1.8% for 6s. Max 4 stacks. Can only occur once every 0.3s.",
        "Normal Attack and Charged Attack hits increase ATK by 7% and Normal ATK SPD by 2.1% for 6s. Max 4 stacks. Can only occur once every 0.3s.",
        "Normal Attack and Charged Attack hits increase ATK by 8% and Normal ATK SPD by 2.4% for 6s. Max 4 stacks. Can only occur once every 0.3s.",
    ]
    file: str = "cpbw"
