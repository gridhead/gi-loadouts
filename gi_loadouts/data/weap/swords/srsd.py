from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SkyriderSword(Sword):
    name: str = "Skyrider Sword"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=11.3)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_3
    refi_name: str = "Determination"
    refi_list: list[str] = [
        "Using an Elemental Burst grants a 12% increase in ATK and Movement SPD for 15s.",
        "Using an Elemental Burst grants a 15% increase in ATK and Movement SPD for 15s.",
        "Using an Elemental Burst grants a 18% increase in ATK and Movement SPD for 15s.",
        "Using an Elemental Burst grants a 21% increase in ATK and Movement SPD for 15s.",
        "Using an Elemental Burst grants a 24% increase in ATK and Movement SPD for 15s.",
    ]
    file: str = "srsd"
