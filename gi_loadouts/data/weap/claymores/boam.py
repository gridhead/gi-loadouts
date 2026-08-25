from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class BladeOfAtonement(Claymore):
    name: str = "Blade of Atonement"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Repentance and Redemption"
    refi_list: list[str] = [
        "Triggering an Elemental Reaction increases the equipping character's Elemental Mastery by 64 for 12s, while triggering a Stellar Glimmer reaction increases their ATK by 16% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction increases the equipping character's Elemental Mastery by 80 for 12s, while triggering a Stellar Glimmer reaction increases their ATK by 20% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction increases the equipping character's Elemental Mastery by 96 for 12s, while triggering a Stellar Glimmer reaction increases their ATK by 24% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction increases the equipping character's Elemental Mastery by 112 for 12s, while triggering a Stellar Glimmer reaction increases their ATK by 28% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction increases the equipping character's Elemental Mastery by 128 for 12s, while triggering a Stellar Glimmer reaction increases their ATK by 32% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
    ]
    file: str = "boam"
