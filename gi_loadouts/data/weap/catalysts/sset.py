from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class StarsealedEdict(Catalyst):
    name: str = "Starsealed Edict"
    seco_stat: WeaponStat = WeaponStat(
        stat_name=WeaponStatType.critical_damage_perc, stat_data=19.2
    )
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Dawnstar's Flowing Trail"
    refi_list: list[str] = [
        "CRIT DMG increased by 24%. When using an Elemental Skill, the equipping character gains the Crystal Compounding effect: Increases Elemental Mastery by 48 for 20s. During this time, the equipping character gains a stack of Law of Combustion when a nearby party member triggers an Elemental Reaction. Each stack increases Elemental Mastery by an additional 24. Max 3 stacks. Radiance: Stellar-Conduct: Each Law of Combustion stack also increases the CRIT DMG of the equipping character's Stellar-Conduct reactions by 12%. This effect can be triggered even when the equipping character is off-field.",
        "CRIT DMG increased by 30%. When using an Elemental Skill, the equipping character gains the Crystal Compounding effect: Increases Elemental Mastery by 60 for 20s. During this time, the equipping character gains a stack of Law of Combustion when a nearby party member triggers an Elemental Reaction. Each stack increases Elemental Mastery by an additional 30. Max 3 stacks. Radiance: Stellar-Conduct: Each Law of Combustion stack also increases the CRIT DMG of the equipping character's Stellar-Conduct reactions by 15%. This effect can be triggered even when the equipping character is off-field.",
        "CRIT DMG increased by 36%. When using an Elemental Skill, the equipping character gains the Crystal Compounding effect: Increases Elemental Mastery by 72 for 20s. During this time, the equipping character gains a stack of Law of Combustion when a nearby party member triggers an Elemental Reaction. Each stack increases Elemental Mastery by an additional 36. Max 3 stacks. Radiance: Stellar-Conduct: Each Law of Combustion stack also increases the CRIT DMG of the equipping character's Stellar-Conduct reactions by 18%. This effect can be triggered even when the equipping character is off-field.",
        "CRIT DMG increased by 42%. When using an Elemental Skill, the equipping character gains the Crystal Compounding effect: Increases Elemental Mastery by 84 for 20s. During this time, the equipping character gains a stack of Law of Combustion when a nearby party member triggers an Elemental Reaction. Each stack increases Elemental Mastery by an additional 42. Max 3 stacks. Radiance: Stellar-Conduct: Each Law of Combustion stack also increases the CRIT DMG of the equipping character's Stellar-Conduct reactions by 21%. This effect can be triggered even when the equipping character is off-field.",
        "CRIT DMG increased by 48%. When using an Elemental Skill, the equipping character gains the Crystal Compounding effect: Increases Elemental Mastery by 96 for 20s. During this time, the equipping character gains a stack of Law of Combustion when a nearby party member triggers an Elemental Reaction. Each stack increases Elemental Mastery by an additional 48. Max 3 stacks. Radiance: Stellar-Conduct: Each Law of Combustion stack also increases the CRIT DMG of the equipping character's Stellar-Conduct reactions by 24%. This effect can be triggered even when the equipping character is off-field.",
    ]
    refi_stat: list[list[WeaponStat]] = [
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=24.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=30.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=36.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=42.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=48.0)],
    ]
    file: str = "sset"
