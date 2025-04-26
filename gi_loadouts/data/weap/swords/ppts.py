from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class PeakPatrolSong(Sword):
    name: str = "Peak Patrol Song"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=18.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Halcyon Years Unending"
    refi_list: list[str] = [
        "Gain \"Ode to Flowers\" after Normal or Plunging Attacks hit an opponent: DEF increases by 8% and gain a 10% All Elemental DMG Bonus for 6s. Max 2 stacks. Can trigger once per 0.1s. When this effect reaches 2 stacks or the 2nd stack's duration is refreshed, increase all nearby party members' All Elemental DMG Bonus by 8% for every 1,000 DEF the equipping character has, up to a maximum of 25.6%, for 15s.",
        "Gain \"Ode to Flowers\" after Normal or Plunging Attacks hit an opponent: DEF increases by 10% and gain a 12.5% All Elemental DMG Bonus for 6s. Max 2 stacks. Can trigger once per 0.1s. When this effect reaches 2 stacks or the 2nd stack's duration is refreshed, increase all nearby party members' All Elemental DMG Bonus by 10% for every 1,000 DEF the equipping character has, up to a maximum of 32%, for 15s.",
        "Gain \"Ode to Flowers\" after Normal or Plunging Attacks hit an opponent: DEF increases by 12% and gain a 15% All Elemental DMG Bonus for 6s. Max 2 stacks. Can trigger once per 0.1s. When this effect reaches 2 stacks or the 2nd stack's duration is refreshed, increase all nearby party members' All Elemental DMG Bonus by 12% for every 1,000 DEF the equipping character has, up to a maximum of 38.4%, for 15s.",
        "Gain \"Ode to Flowers\" after Normal or Plunging Attacks hit an opponent: DEF increases by 14% and gain a 17.5% All Elemental DMG Bonus for 6s. Max 2 stacks. Can trigger once per 0.1s. When this effect reaches 2 stacks or the 2nd stack's duration is refreshed, increase all nearby party members' All Elemental DMG Bonus by 14% for every 1,000 DEF the equipping character has, up to a maximum of 44.8%, for 15s.",
        "Gain \"Ode to Flowers\" after Normal or Plunging Attacks hit an opponent: DEF increases by 16% and gain a 20% All Elemental DMG Bonus for 6s. Max 2 stacks. Can trigger once per 0.1s. When this effect reaches 2 stacks or the 2nd stack's duration is refreshed, increase all nearby party members' All Elemental DMG Bonus by 16% for every 1,000 DEF the equipping character has, up to a maximum of 51.2%, for 15s.",
    ]
    file: str = "ppts"
