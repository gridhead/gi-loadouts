from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class MagicGuide(Catalyst):
    name: str = "Magic Guide"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=41.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_3
    refi_name: str = "Bane of Storm and Tide"
    refi_list: list[str] = [
        "Increases DMG against opponents affected by Hydro or Electro by 12%.",
        "Increases DMG against opponents affected by Hydro or Electro by 15%.",
        "Increases DMG against opponents affected by Hydro or Electro by 18%.",
        "Increases DMG against opponents affected by Hydro or Electro by 21%.",
        "Increases DMG against opponents affected by Hydro or Electro by 24%.",
    ]
    file: str = "mcge"
