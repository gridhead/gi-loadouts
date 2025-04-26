from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class RavenBow(Bow):
    name: str = "Raven Bow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=20.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_3
    refi_name: str = "Bane of Flame and Water"
    refi_list: list[str] = [
            "Increases DMG against opponents affected by Hydro or Pyro by 12%.",
            "Increases DMG against opponents affected by Hydro or Pyro by 15%.",
            "Increases DMG against opponents affected by Hydro or Pyro by 18%.",
            "Increases DMG against opponents affected by Hydro or Pyro by 21%.",
            "Increases DMG against opponents affected by Hydro or Pyro by 24%.",
        ]
    file: str = "rvbw"
