from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class KagurasVerity(Catalyst):
    name: str = "Kagura's Verity"
    seco_stat: WeaponStat = WeaponStat(
        stat_name=WeaponStatType.critical_damage_perc, stat_data=14.4
    )
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Kagura Dance of the Sacred Sakura"
    refi_list: list[str] = [
        "Using an Elemental Skill grants the Kagura Dance effect, increasing the wielding character's Elemental Skill DMG by 12% as well as their Stellar-Conduct DMG by 12% for 24s. Max 3 stacks. This character will gain a 12% All Elemental DMG Bonus when they possess 3 stacks.",
        "Using an Elemental Skill grants the Kagura Dance effect, increasing the wielding character's Elemental Skill DMG by 15% as well as their Stellar-Conduct DMG by 15% for 24s. Max 3 stacks. This character will gain a 15% All Elemental DMG Bonus when they possess 3 stacks.",
        "Using an Elemental Skill grants the Kagura Dance effect, increasing the wielding character's Elemental Skill DMG by 18% as well as their Stellar-Conduct DMG by 18% for 24s. Max 3 stacks. This character will gain a 18% All Elemental DMG Bonus when they possess 3 stacks.",
        "Using an Elemental Skill grants the Kagura Dance effect, increasing the wielding character's Elemental Skill DMG by 21% as well as their Stellar-Conduct DMG by 21% for 24s. Max 3 stacks. This character will gain a 21% All Elemental DMG Bonus when they possess 3 stacks.",
        "Using an Elemental Skill grants the Kagura Dance effect, increasing the wielding character's Elemental Skill DMG by 24% as well as their Stellar-Conduct DMG by 24% for 24s. Max 3 stacks. This character will gain a 24% All Elemental DMG Bonus when they possess 3 stacks.",
    ]
    file: str = "kgvy"
