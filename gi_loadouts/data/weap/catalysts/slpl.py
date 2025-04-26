from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SolarPearl(Catalyst):
    name: str = "Solar Pearl"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Solar Shine"
    refi_list: list[str] = [
        "Normal Attack hits increase Elemental Skill and Elemental Burst DMG by 20% for 6s. Likewise, Elemental Skill or Elemental Burst hits increase Normal Attack DMG by 20% for 6s.",
        "Normal Attack hits increase Elemental Skill and Elemental Burst DMG by 25% for 6s. Likewise, Elemental Skill or Elemental Burst hits increase Normal Attack DMG by 25% for 6s.",
        "Normal Attack hits increase Elemental Skill and Elemental Burst DMG by 30% for 6s. Likewise, Elemental Skill or Elemental Burst hits increase Normal Attack DMG by 30% for 6s.",
        "Normal Attack hits increase Elemental Skill and Elemental Burst DMG by 35% for 6s. Likewise, Elemental Skill or Elemental Burst hits increase Normal Attack DMG by 35% for 6s.",
        "Normal Attack hits increase Elemental Skill and Elemental Burst DMG by 40% for 6s. Likewise, Elemental Skill or Elemental Burst hits increase Normal Attack DMG by 40% for 6s.",
    ]
    file: str = "slpl"
