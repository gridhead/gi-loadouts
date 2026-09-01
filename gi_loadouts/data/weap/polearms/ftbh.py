from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Frostbreath(Polearm):
    name: str = "Frostbreath"
    seco_stat: WeaponStat = WeaponStat(
        stat_name=WeaponStatType.energy_recharge_perc, stat_data=10.0
    )
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "A Cast Real Far"
    refi_list: list[str] = [
        "Triggering a Cryo or Hydro-related elemental reaction increases the equipping character's ATK by 20% for the next 15s, as well as regenerates 6 Elemental Energy for other members of their party. This effect can trigger once every 16s.",
        "Triggering a Cryo or Hydro-related elemental reaction increases the equipping character's ATK by 25% for the next 15s, as well as regenerates 7.5 Elemental Energy for other members of their party. This effect can trigger once every 16s.",
        "Triggering a Cryo or Hydro-related elemental reaction increases the equipping character's ATK by 30% for the next 15s, as well as regenerates 9 Elemental Energy for other members of their party. This effect can trigger once every 16s.",
        "Triggering a Cryo or Hydro-related elemental reaction increases the equipping character's ATK by 35% for the next 15s, as well as regenerates 10.5 Elemental Energy for other members of their party. This effect can trigger once every 16s.",
        "Triggering a Cryo or Hydro-related elemental reaction increases the equipping character's ATK by 40% for the next 15s, as well as regenerates 12 Elemental Energy for other members of their party. This effect can trigger once every 16s.",
    ]
    file: str = "ftbh"
