from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class PrototypeRancour(Sword):
    name: str = "Prototype Rancour"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.damage_bonus_physical_perc, stat_data=7.5)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Smashed Stone"
    refi_list: list[str] = [
        "On hit, Normal or Charged Attacks increase ATK and DEF by 4% for 6s. Max 4 stacks. This effect can only occur once every 0.3s.",
        "On hit, Normal or Charged Attacks increase ATK and DEF by 5% for 6s. Max 4 stacks. This effect can only occur once every 0.3s.",
        "On hit, Normal or Charged Attacks increase ATK and DEF by 6% for 6s. Max 4 stacks. This effect can only occur once every 0.3s.",
        "On hit, Normal or Charged Attacks increase ATK and DEF by 7% for 6s. Max 4 stacks. This effect can only occur once every 0.3s.",
        "On hit, Normal or Charged Attacks increase ATK and DEF by 8% for 6s. Max 4 stacks. This effect can only occur once every 0.3s.",
    ]
    file: str = "ptrc"
