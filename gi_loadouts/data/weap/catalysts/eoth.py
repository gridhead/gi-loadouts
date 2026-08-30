from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class EchoesOfTheHeart(Catalyst):
    name: str = "Echoes of the Heart"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Echo of a Vow"
    refi_list: list[str] = [
        "Triggering an Elemental Reaction increases the equipping character's Elemental Mastery by 60 for 12s, while triggering a Stellar Glimmer reaction increases their Stellar Glimmer reaction DMG dealt by 16% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction increases the equipping character's Elemental Mastery by 75 for 12s, while triggering a Stellar Glimmer reaction increases their Stellar Glimmer reaction DMG dealt by 20% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction increases the equipping character's Elemental Mastery by 90 for 12s, while triggering a Stellar Glimmer reaction increases their Stellar Glimmer reaction DMG dealt by 24% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction increases the equipping character's Elemental Mastery by 105 for 12s, while triggering a Stellar Glimmer reaction increases their Stellar Glimmer reaction DMG dealt by 28% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction increases the equipping character's Elemental Mastery by 120 for 12s, while triggering a Stellar Glimmer reaction increases their Stellar Glimmer reaction DMG dealt by 32% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
    ]
    file: str = "eoth"
