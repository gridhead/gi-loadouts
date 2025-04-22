from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class CoolSteel(Sword):
    name: str = "Cool Steel"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=7.7)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_3
    refi_name: str = "Bane of Water and Ice"
    refi_list: list[str] = [
        "Increases DMG against opponents affected by Hydro or Cryo by 12%.",
        "Increases DMG against opponents affected by Hydro or Cryo by 15%.",
        "Increases DMG against opponents affected by Hydro or Cryo by 18%.",
        "Increases DMG against opponents affected by Hydro or Cryo by 21%.",
        "Increases DMG against opponents affected by Hydro or Cryo by 24%.",
    ]
    file: str = "clsl"
