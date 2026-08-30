from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Emberwell(Sword):
    name: str = "Emberwell"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=36.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Starfire Upon the Snowplains"
    refi_list: list[str] = [
        "Triggering an Elemental Reaction increases the equipping character's ATK by 16% for 12s. Triggering a Stellar Glimmer reaction increases their Stellar Glimmer reaction DMG dealt by 16% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction increases the equipping character's ATK by 20% for 12s. Triggering a Stellar Glimmer reaction increases their Stellar Glimmer reaction DMG dealt by 20% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction increases the equipping character's ATK by 24% for 12s. Triggering a Stellar Glimmer reaction increases their Stellar Glimmer reaction DMG dealt by 24% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction increases the equipping character's ATK by 28% for 12s. Triggering a Stellar Glimmer reaction increases their Stellar Glimmer reaction DMG dealt by 28% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction increases the equipping character's ATK by 32% for 12s. Triggering a Stellar Glimmer reaction increases their Stellar Glimmer reaction DMG dealt by 32% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
    ]
    file: str = "erwl"
