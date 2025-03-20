from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Sword, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.tier import Tier


class DarkIronSword(Sword):
    name: str = "Dark Iron Sword"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=31.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_3
    refi_name: str = "Overloaded"
    refi_list: list[str] = [
        "Upon causing an Overloaded, Superconduct, Electro-Charged, Quicken, Aggravate, Hyperbloom, or Electro-infused Swirl reaction, ATK is increased by 20% for 12s.",
        "Upon causing an Overloaded, Superconduct, Electro-Charged, Quicken, Aggravate, Hyperbloom, or Electro-infused Swirl reaction, ATK is increased by 25% for 12s.",
        "Upon causing an Overloaded, Superconduct, Electro-Charged, Quicken, Aggravate, Hyperbloom, or Electro-infused Swirl reaction, ATK is increased by 30% for 12s.",
        "Upon causing an Overloaded, Superconduct, Electro-Charged, Quicken, Aggravate, Hyperbloom, or Electro-infused Swirl reaction, ATK is increased by 35% for 12s.",
        "Upon causing an Overloaded, Superconduct, Electro-Charged, Quicken, Aggravate, Hyperbloom, or Electro-infused Swirl reaction, ATK is increased by 40% for 12s.",
    ]
    file: str = "disd"
