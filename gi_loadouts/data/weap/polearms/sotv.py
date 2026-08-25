from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SongOfTheVigil(Polearm):
    name: str = "Song of the Vigil"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=24.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Cadence of Days Gone By"
    refi_list: list[str] = [
        "Triggering an Elemental Reaction regenerates 4 Elemental Energy for the equipping character. This effect can trigger once every 9s. On the other hand, triggering a Stellar Glimmer reaction increases their ATK by 20% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction regenerates 5 Elemental Energy for the equipping character. This effect can trigger once every 9s. On the other hand, triggering a Stellar Glimmer reaction increases their ATK by 25% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction regenerates 6 Elemental Energy for the equipping character. This effect can trigger once every 9s. On the other hand, triggering a Stellar Glimmer reaction increases their ATK by 30% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction regenerates 7 Elemental Energy for the equipping character. This effect can trigger once every 9s. On the other hand, triggering a Stellar Glimmer reaction increases their ATK by 35% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
        "Triggering an Elemental Reaction regenerates 8 Elemental Energy for the equipping character. This effect can trigger once every 9s. On the other hand, triggering a Stellar Glimmer reaction increases their ATK by 40% for 12s. The aforementioned effects can trigger even when the character is not on the field.",
    ]
    file: str = "sotv"
