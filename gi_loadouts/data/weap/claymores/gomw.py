from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class GestoftheMightyWolf(Claymore):
    name: str = "Gest of the Mighty Wolf"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=7.2)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Indomitable Chivalry"
    refi_list: list[str] = [
        "Increase ATK SPD by 10%. Every time the equipping character's Normal Attack(s) hit opponent(s), when they cast their Elemental Skill, or when they begin their Charged Attack(s), gain 1/2/2 stacks of Four Winds' Hymn respectively: DMG dealt is increased by 7.5%, for 4s. Max 4 stacks. This effect can be triggered once every 0.01s.\n\nAdditionally, when the team has the \"Hexerei: Secret Rite\" effect, each stack of Four Winds' Hymn will increase the CRIT DMG of the equipping character by 7.5%.",
        "Increase ATK SPD by 10%. Every time the equipping character's Normal Attack(s) hit opponent(s), when they cast their Elemental Skill, or when they begin their Charged Attack(s), gain 1/2/2 stacks of Four Winds' Hymn respectively: DMG dealt is increased by 9.5%, for 4s. Max 4 stacks. This effect can be triggered once every 0.01s.\n\nAdditionally, when the team has the \"Hexerei: Secret Rite\" effect, each stack of Four Winds' Hymn will increase the CRIT DMG of the equipping character by 9.5%.",
        "Increase ATK SPD by 10%. Every time the equipping character's Normal Attack(s) hit opponent(s), when they cast their Elemental Skill, or when they begin their Charged Attack(s), gain 1/2/2 stacks of Four Winds' Hymn respectively: DMG dealt is increased by 11.5%, for 4s. Max 4 stacks. This effect can be triggered once every 0.01s.\n\nAdditionally, when the team has the \"Hexerei: Secret Rite\" effect, each stack of Four Winds' Hymn will increase the CRIT DMG of the equipping character by 11.5%.",
        "Increase ATK SPD by 10%. Every time the equipping character's Normal Attack(s) hit opponent(s), when they cast their Elemental Skill, or when they begin their Charged Attack(s), gain 1/2/2 stacks of Four Winds' Hymn respectively: DMG dealt is increased by 13.5%, for 4s. Max 4 stacks. This effect can be triggered once every 0.01s.\n\nAdditionally, when the team has the \"Hexerei: Secret Rite\" effect, each stack of Four Winds' Hymn will increase the CRIT DMG of the equipping character by 13.5%.",
        "Increase ATK SPD by 10%. Every time the equipping character's Normal Attack(s) hit opponent(s), when they cast their Elemental Skill, or when they begin their Charged Attack(s), gain 1/2/2 stacks of Four Winds' Hymn respectively: DMG dealt is increased by 15.5%, for 4s. Max 4 stacks. This effect can be triggered once every 0.01s.\n\nAdditionally, when the team has the \"Hexerei: Secret Rite\" effect, each stack of Four Winds' Hymn will increase the CRIT DMG of the equipping character by 15.5%.",
    ]
    file: str = "gomw"
