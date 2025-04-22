from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class PrototypeAmber(Catalyst):
    name: str = "Prototype Amber"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Gilding"
    refi_list: list[str] = [
        "Using an Elemental Burst regenerates 4 Energy every 2s for 6s. All party members will regenerate 4% HP every 2s for this duration.",
        "Using an Elemental Burst regenerates 4.5 Energy every 2s for 6s. All party members will regenerate 4.5% HP every 2s for this duration.",
        "Using an Elemental Burst regenerates 5 Energy every 2s for 6s. All party members will regenerate 5% HP every 2s for this duration.",
        "Using an Elemental Burst regenerates 5.5 Energy every 2s for 6s. All party members will regenerate 5.5% HP every 2s for this duration.",
        "Using an Elemental Burst regenerates 6 Energy every 2s for 6s. All party members will regenerate 6% HP every 2s for this duration.",
    ]
    file: str = "ptab"
