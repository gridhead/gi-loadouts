from typing import List

from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Catalyst, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.base.tier import Tier


class SolarPearl(Catalyst):
    name: str = "Solar Pearl"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate, stat_data=6.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_list: List[str] = [
        "Normal Attack hits increase Elemental Skill and Elemental Burst DMG by 20% for 6s. Likewise, Elemental Skill or Elemental Burst hits increase Normal Attack DMG by 20% for 6s.",
        "Normal Attack hits increase Elemental Skill and Elemental Burst DMG by 25% for 6s. Likewise, Elemental Skill or Elemental Burst hits increase Normal Attack DMG by 25% for 6s.",
        "Normal Attack hits increase Elemental Skill and Elemental Burst DMG by 30% for 6s. Likewise, Elemental Skill or Elemental Burst hits increase Normal Attack DMG by 30% for 6s.",
        "Normal Attack hits increase Elemental Skill and Elemental Burst DMG by 35% for 6s. Likewise, Elemental Skill or Elemental Burst hits increase Normal Attack DMG by 35% for 6s.",
        "Normal Attack hits increase Elemental Skill and Elemental Burst DMG by 40% for 6s. Likewise, Elemental Skill or Elemental Burst hits increase Normal Attack DMG by 40% for 6s.",
    ]
