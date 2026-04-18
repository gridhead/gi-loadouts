from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class GoldenFrostboundOath(Bow):
    name: str = "Golden Frostbound Oath"
    seco_stat: WeaponStat = WeaponStat(
        stat_name=WeaponStatType.critical_damage_perc, stat_data=19.2
    )
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Dawn's Salutation Returned"
    refi_list: list[str] = [
        'Increase DEF by 16%. When the equipping character\'s Elemental Skill or Lunar-Crystallize attacks hit opponents, gain the "Frost Fae\'s Favor" effect for 6s: Geo DMG inflicted by the equipping character increases by 40%, Lunar-Crystallize Reaction DMG increases by 40%. While this effect is active, if there are Moondrifts near the equipping character, all other nearby party members will gain the "Frost Fae\'s Mischief" effect: Geo DMG dealt increases by 20% and Lunar-Crystallize Reaction DMG increases by 20%.',
        'Increase DEF by 20%. When the equipping character\'s Elemental Skill or Lunar-Crystallize attacks hit opponents, gain the "Frost Fae\'s Favor" effect for 6s: Geo DMG inflicted by the equipping character increases by 50%, Lunar-Crystallize Reaction DMG increases by 50%. While this effect is active, if there are Moondrifts near the equipping character, all other nearby party members will gain the "Frost Fae\'s Mischief" effect: Geo DMG dealt increases by 25% and Lunar-Crystallize Reaction DMG increases by 25%.',
        'Increase DEF by 24%. When the equipping character\'s Elemental Skill or Lunar-Crystallize attacks hit opponents, gain the "Frost Fae\'s Favor" effect for 6s: Geo DMG inflicted by the equipping character increases by 60%, Lunar-Crystallize Reaction DMG increases by 60%. While this effect is active, if there are Moondrifts near the equipping character, all other nearby party members will gain the "Frost Fae\'s Mischief" effect: Geo DMG dealt increases by 30% and Lunar-Crystallize Reaction DMG increases by 30%.',
        'Increase DEF by 28%. When the equipping character\'s Elemental Skill or Lunar-Crystallize attacks hit opponents, gain the "Frost Fae\'s Favor" effect for 6s: Geo DMG inflicted by the equipping character increases by 70%, Lunar-Crystallize Reaction DMG increases by 70%. While this effect is active, if there are Moondrifts near the equipping character, all other nearby party members will gain the "Frost Fae\'s Mischief" effect: Geo DMG dealt increases by 35% and Lunar-Crystallize Reaction DMG increases by 35%.',
        'Increase DEF by 32%. When the equipping character\'s Elemental Skill or Lunar-Crystallize attacks hit opponents, gain the "Frost Fae\'s Favor" effect for 6s: Geo DMG inflicted by the equipping character increases by 80%, Lunar-Crystallize Reaction DMG increases by 80%. While this effect is active, if there are Moondrifts near the equipping character, all other nearby party members will gain the "Frost Fae\'s Mischief" effect: Geo DMG dealt increases by 40% and Lunar-Crystallize Reaction DMG increases by 40%.',
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=16.0)],
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=24.0)],
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=28.0)],
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=32.0)],
    ]
    file: str = "gfbo"
