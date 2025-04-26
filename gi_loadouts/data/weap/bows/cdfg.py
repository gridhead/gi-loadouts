from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Cloudforged(Bow):
    name: str = "Cloudforged"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=36.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Crag-Chiseled Forge"
    refi_list: list[str] = [
        "After Elemental Energy is decreased, the equipping character's Elemental Mastery will increase by 40 for 18s. Max 2 stacks.",
        "After Elemental Energy is decreased, the equipping character's Elemental Mastery will increase by 50 for 18s. Max 2 stacks.",
        "After Elemental Energy is decreased, the equipping character's Elemental Mastery will increase by 60 for 18s. Max 2 stacks.",
        "After Elemental Energy is decreased, the equipping character's Elemental Mastery will increase by 70 for 18s. Max 2 stacks.",
        "After Elemental Energy is decreased, the equipping character's Elemental Mastery will increase by 80 for 18s. Max 2 stacks.",
    ]
    file: str = "cdfg"
