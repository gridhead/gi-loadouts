from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class NewBough(Sword):
    name: str = "New Bough"
    seco_stat: WeaponStat = WeaponStat(
        stat_name=WeaponStatType.critical_damage_perc, stat_data=12.0
    )
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Wildgrowth"
    refi_list: list[str] = [
        "When the equipping character hits the opponent with an attack within 12s after using the Elemental Skill, they gain the \"Verdant\" effect, which increases their ATK by 4% and their Elemental Mastery by 20. This effect lasts 6s and can trigger once every second. Max 3 stacks. The aforementioned effects can still trigger even when the equipping character is not on the field.\nRadiance: Stellar Glimmer: The effect of \"Verdant\" is changed to: Increases ATK by 6% as well as Stellar Glimmer reaction DMG dealt by the equipping character by 8%.",
        "When the equipping character hits the opponent with an attack within 12s after using the Elemental Skill, they gain the \"Verdant\" effect, which increases their ATK by 5% and their Elemental Mastery by 25. This effect lasts 6s and can trigger once every second. Max 3 stacks. The aforementioned effects can still trigger even when the equipping character is not on the field.\nRadiance: Stellar Glimmer: The effect of \"Verdant\" is changed to: Increases ATK by 7.5% as well as Stellar Glimmer reaction DMG dealt by the equipping character by 10%.",
        "When the equipping character hits the opponent with an attack within 12s after using the Elemental Skill, they gain the \"Verdant\" effect, which increases their ATK by 6% and their Elemental Mastery by 30. This effect lasts 6s and can trigger once every second. Max 3 stacks. The aforementioned effects can still trigger even when the equipping character is not on the field.\nRadiance: Stellar Glimmer: The effect of \"Verdant\" is changed to: Increases ATK by 9% as well as Stellar Glimmer reaction DMG dealt by the equipping character by 12%.",
        "When the equipping character hits the opponent with an attack within 12s after using the Elemental Skill, they gain the \"Verdant\" effect, which increases their ATK by 7% and their Elemental Mastery by 35. This effect lasts 6s and can trigger once every second. Max 3 stacks. The aforementioned effects can still trigger even when the equipping character is not on the field.\nRadiance: Stellar Glimmer: The effect of \"Verdant\" is changed to: Increases ATK by 10.5% as well as Stellar Glimmer reaction DMG dealt by the equipping character by 14%.",
        "When the equipping character hits the opponent with an attack within 12s after using the Elemental Skill, they gain the \"Verdant\" effect, which increases their ATK by 8% and their Elemental Mastery by 40. This effect lasts 6s and can trigger once every second. Max 3 stacks. The aforementioned effects can still trigger even when the equipping character is not on the field.\nRadiance: Stellar Glimmer: The effect of \"Verdant\" is changed to: Increases ATK by 12% as well as Stellar Glimmer reaction DMG dealt by the equipping character by 16%.",
    ]
    file: str = "nwbh"
