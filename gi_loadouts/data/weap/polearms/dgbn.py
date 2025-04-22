from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class DragonsBane(Polearm):
    name: str = "Dragon's Bane"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=48.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Bane of Flame and Water"
    refi_list: list[str] = [
        "Increases DMG against opponents affected by Hydro or Pyro by 20%.",
        "Increases DMG against opponents affected by Hydro or Pyro by 24%.",
        "Increases DMG against opponents affected by Hydro or Pyro by 28%.",
        "Increases DMG against opponents affected by Hydro or Pyro by 32%.",
        "Increases DMG against opponents affected by Hydro or Pyro by 36%.",
    ]
    file: str = "dgbn"
