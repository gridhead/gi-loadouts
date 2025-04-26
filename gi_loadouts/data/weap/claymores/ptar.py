from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class PrototypeArchaic(Claymore):
    name: str = "Prototype Archaic"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Crush"
    refi_list: list[str] = [
        "On hit, Normal or Charged Attacks have a 50% chance to deal an additional 240% ATK DMG to opponents within a small AoE. Can only occur once every 15s.",
        "On hit, Normal or Charged Attacks have a 50% chance to deal an additional 300% ATK DMG to opponents within a small AoE. Can only occur once every 15s.",
        "On hit, Normal or Charged Attacks have a 50% chance to deal an additional 360% ATK DMG to opponents within a small AoE. Can only occur once every 15s.",
        "On hit, Normal or Charged Attacks have a 50% chance to deal an additional 420% ATK DMG to opponents within a small AoE. Can only occur once every 15s.",
        "On hit, Normal or Charged Attacks have a 50% chance to deal an additional 480% ATK DMG to opponents within a small AoE. Can only occur once every 15s.",
    ]
    file: str = "ptar"
