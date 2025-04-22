from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class MissiveWindspear(Polearm):
    name: str = "Missive Windspear"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "The Wind Unattained"
    refi_list: list[str] = [
        "Within 10s after an Elemental Reaction is triggered, ATK is increased by 12% and Elemental Mastery is increased by 48.",
        "Within 10s after an Elemental Reaction is triggered, ATK is increased by 15% and Elemental Mastery is increased by 60.",
        "Within 10s after an Elemental Reaction is triggered, ATK is increased by 18% and Elemental Mastery is increased by 72.",
        "Within 10s after an Elemental Reaction is triggered, ATK is increased by 21% and Elemental Mastery is increased by 84.",
        "Within 10s after an Elemental Reaction is triggered, ATK is increased by 24% and Elemental Mastery is increased by 96.",
    ]
    file: str = "mswp"
