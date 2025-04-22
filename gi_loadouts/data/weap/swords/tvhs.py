from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TravelersHandySword(Sword):
    name: str = "Traveler's Handy Sword"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=6.4)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_3
    refi_name: str = "Journey"
    refi_list: list[str] = [
        "Each Elemental Orb or Particle collected restores 1% HP.",
        "Each Elemental Orb or Particle collected restores 1.25% HP.",
        "Each Elemental Orb or Particle collected restores 1.5% HP.",
        "Each Elemental Orb or Particle collected restores 1.75% HP.",
        "Each Elemental Orb or Particle collected restores 2% HP.",
    ]
    file: str = "tvhs"
