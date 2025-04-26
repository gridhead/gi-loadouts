from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class LionsRoar(Sword):
    name: str = "Lion's Roar"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Bane of Fire and Thunder"
    refi_list: list[str] = [
        "Increases DMG against enemies affected by Pyro or Electro by 20%.",
        "Increases DMG against enemies affected by Pyro or Electro by 24%.",
        "Increases DMG against enemies affected by Pyro or Electro by 28%.",
        "Increases DMG against enemies affected by Pyro or Electro by 32%.",
        "Increases DMG against enemies affected by Pyro or Electro by 36%.",
    ]
    file: str = "lnrr"
