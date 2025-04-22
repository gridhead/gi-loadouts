from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Rainslasher(Claymore):
    name: str = "Rainslasher"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=36.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Bane of Storm and Tide"
    refi_list: list[str] = [
        "Increases DMG against opponents affected by Hydro or Electro by 20%.",
        "Increases DMG against opponents affected by Hydro or Electro by 24%.",
        "Increases DMG against opponents affected by Hydro or Electro by 28%.",
        "Increases DMG against opponents affected by Hydro or Electro by 32%.",
        "Increases DMG against opponents affected by Hydro or Electro by 36%.",
    ]
    file: str = "rnsh"
