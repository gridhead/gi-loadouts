from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SilverLight(Sword):
    name: str = "Silver Light"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Radiance on the Water"
    refi_list: list[str] = [
        "Increases Elemental Mastery by 52 for 12s after Elemental Skill use. Max 2 stacks, and each stack's duration is independent of the others.",
        "Increases Elemental Mastery by 65 for 12s after Elemental Skill use. Max 2 stacks, and each stack's duration is independent of the others.",
        "Increases Elemental Mastery by 78 for 12s after Elemental Skill use. Max 2 stacks, and each stack's duration is independent of the others.",
        "Increases Elemental Mastery by 91 for 12s after Elemental Skill use. Max 2 stacks, and each stack's duration is independent of the others.",
        "Increases Elemental Mastery by 104 for 12s after Elemental Skill use. Max 2 stacks, and each stack's duration is independent of the others.",
    ]
    refi_stat: list[list[WeaponStat]] = [
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=52)],
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=65)],
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=78)],
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=91)],
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=104)],
    ]
    file: str = "srlt"
