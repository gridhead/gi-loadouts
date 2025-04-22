from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class BloodtaintedGreatsword(Claymore):
    name: str = "Bloodtainted Greatsword"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=41)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_3
    refi_name: str = "Bane of Fire and Thunder"
    refi_list: list[str] = [
        "Increases DMG against opponents affected by Pyro or Electro by 12%.",
        "Increases DMG against opponents affected by Pyro or Electro by 15%.",
        "Increases DMG against opponents affected by Pyro or Electro by 18%.",
        "Increases DMG against opponents affected by Pyro or Electro by 21%.",
        "Increases DMG against opponents affected by Pyro or Electro by 24%.",
    ]
    file: str = "btgs"
