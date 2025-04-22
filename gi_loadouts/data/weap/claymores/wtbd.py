from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Whiteblind(Claymore):
    name: str = "Whiteblind"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=11.3)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Infusion Blade"
    refi_list: list[str] = [
        "On hit, Normal or Charged Attacks increase ATK and DEF by 6% for 6s. Max 4 stacks (24%  total). Can only occur once every 0.5s.",
        "On hit, Normal or Charged Attacks increase ATK and DEF by 7.5% for 6s. Max 4 stacks (30%  total). Can only occur once every 0.5s.",
        "On hit, Normal or Charged Attacks increase ATK and DEF by 9% for 6s. Max 4 stacks (36%  total). Can only occur once every 0.5s.",
        "On hit, Normal or Charged Attacks increase ATK and DEF by 10.5% for 6s. Max 4 stacks (42%  total). Can only occur once every 0.5s.",
        "On hit, Normal or Charged Attacks increase ATK and DEF by 12% for 6s. Max 4 stacks (48%  total). Can only occur once every 0.5s.",
    ]
    file: str = "wtbd"
