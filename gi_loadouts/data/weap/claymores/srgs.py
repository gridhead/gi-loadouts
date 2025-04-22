from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SkyriderGreatsword(Claymore):
    name: str = "Skyrider Greatsword"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.damage_bonus_physical_perc, stat_data=9.6)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_3
    refi_name: str = "Courage"
    refi_list: list[str] = [
        "On hit, Normal or Charged Attacks increase ATK by 6% for 6s. Max 4 stacks. Can only occur once every 0.5s.",
        "On hit, Normal or Charged Attacks increase ATK by 7% for 6s. Max 4 stacks. Can only occur once every 0.5s.",
        "On hit, Normal or Charged Attacks increase ATK by 8% for 6s. Max 4 stacks. Can only occur once every 0.5s.",
        "On hit, Normal or Charged Attacks increase ATK by 9% for 6s. Max 4 stacks. Can only occur once every 0.5s.",
        "On hit, Normal or Charged Attacks increase ATK by 10% for 6s. Max 4 stacks. Can only occur once every 0.5s.",
    ]
    file: str = "srgs"
