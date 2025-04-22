from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class KagurasVerity(Catalyst):
    name: str = "Kagura's Verity"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=14.4)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Kagura Dance of the Sacred Sakura"
    refi_list: list[str] = [
        "Gains the Kagura Dance effect when using an Elemental Skill, causing the Elemental Skill DMG of the character wielding this weapon to increase by 12% for 16s. Max 3 stacks. This character will gain 12% All Elemental DMG Bonus when they possess 3 stacks.",
        "Gains the Kagura Dance effect when using an Elemental Skill, causing the Elemental Skill DMG of the character wielding this weapon to increase by 15% for 16s. Max 3 stacks. This character will gain 15% All Elemental DMG Bonus when they possess 3 stacks.",
        "Gains the Kagura Dance effect when using an Elemental Skill, causing the Elemental Skill DMG of the character wielding this weapon to increase by 18% for 16s. Max 3 stacks. This character will gain 18% All Elemental DMG Bonus when they possess 3 stacks.",
        "Gains the Kagura Dance effect when using an Elemental Skill, causing the Elemental Skill DMG of the character wielding this weapon to increase by 21% for 16s. Max 3 stacks. This character will gain 21% All Elemental DMG Bonus when they possess 3 stacks.",
        "Gains the Kagura Dance effect when using an Elemental Skill, causing the Elemental Skill DMG of the character wielding this weapon to increase by 24% for 16s. Max 3 stacks. This character will gain 24% All Elemental DMG Bonus when they possess 3 stacks.",
    ]
    file: str = "kgvy"
