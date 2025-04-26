from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class DebateClub(Claymore):
    name: str = "Debate Club"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=7.7)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_3
    refi_name: str = "Blunt Conclusion"
    refi_list: list[str] = [
        "After using an Elemental Skill, Normal or Charged Attacks, on hit, deal an additional 60% ATK DMG in a small area. Effect lasts 15s. DMG can only occur once every 3s.",
        "After using an Elemental Skill, Normal or Charged Attacks, on hit, deal an additional 75% ATK DMG in a small area. Effect lasts 15s. DMG can only occur once every 3s.",
        "After using an Elemental Skill, Normal or Charged Attacks, on hit, deal an additional 90% ATK DMG in a small area. Effect lasts 15s. DMG can only occur once every 3s.",
        "After using an Elemental Skill, Normal or Charged Attacks, on hit, deal an additional 105% ATK DMG in a small area. Effect lasts 15s. DMG can only occur once every 3s.",
        "After using an Elemental Skill, Normal or Charged Attacks, on hit, deal an additional 120% ATK DMG in a small area. Effect lasts 15s. DMG can only occur once every 3s.",
    ]
    file: str = "dbcl"
