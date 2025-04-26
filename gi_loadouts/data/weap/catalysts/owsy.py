from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class OtherworldlyStory(Catalyst):
    name: str = "Otherworldly Story"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=8.5)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_3
    refi_name: str = "Energy Shower"
    refi_list: list[str] = [
        "Each Elemental Orb or Particle collected restores 1% HP.",
        "Each Elemental Orb or Particle collected restores 1.25% HP.",
        "Each Elemental Orb or Particle collected restores 1.5% HP.",
        "Each Elemental Orb or Particle collected restores 1.75% HP.",
        "Each Elemental Orb or Particle collected restores 2% HP.",
    ]
    file: str = "owsy"
