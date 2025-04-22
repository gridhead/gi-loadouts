from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class KeyofKhajNisut(Sword):
    name: str = "Key of Khaj-Nisut"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=14.4)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Sunken Song of the Sands"
    refi_list: list[str] = [
            "HP increased by 20%. When an Elemental Skill hits opponents, you gain the Grand Hymn effect for 20s. This effect increases the equipping character's Elemental Mastery by 0.12% of their Max HP. This effect can trigger once every 0.3s. Max 3 stacks. When this effect gains 3 stacks, or when the third stack's duration is refreshed, the Elemental Mastery of all nearby party members will be increased by 0.2% of the equipping character's max HP for 20s.",
            "HP increased by 25%. When an Elemental Skill hits opponents, you gain the Grand Hymn effect for 20s. This effect increases the equipping character's Elemental Mastery by 0.15% of their Max HP. This effect can trigger once every 0.3s. Max 3 stacks. When this effect gains 3 stacks, or when the third stack's duration is refreshed, the Elemental Mastery of all nearby party members will be increased by 0.25% of the equipping character's max HP for 20s.",
            "HP increased by 30%. When an Elemental Skill hits opponents, you gain the Grand Hymn effect for 20s. This effect increases the equipping character's Elemental Mastery by 0.18% of their Max HP. This effect can trigger once every 0.3s. Max 3 stacks. When this effect gains 3 stacks, or when the third stack's duration is refreshed, the Elemental Mastery of all nearby party members will be increased by 0.3% of the equipping character's max HP for 20s.",
            "HP increased by 35%. When an Elemental Skill hits opponents, you gain the Grand Hymn effect for 20s. This effect increases the equipping character's Elemental Mastery by 0.21% of their Max HP. This effect can trigger once every 0.3s. Max 3 stacks. When this effect gains 3 stacks, or when the third stack's duration is refreshed, the Elemental Mastery of all nearby party members will be increased by 0.35% of the equipping character's max HP for 20s.",
            "HP increased by 40%. When an Elemental Skill hits opponents, you gain the Grand Hymn effect for 20s. This effect increases the equipping character's Elemental Mastery by 0.24% of their Max HP. This effect can trigger once every 0.3s. Max 3 stacks. When this effect gains 3 stacks, or when the third stack's duration is refreshed, the Elemental Mastery of all nearby party members will be increased by 0.4% of the equipping character's max HP for 20s.",
        ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=25.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=30.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=35.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=40.0)],
    ]
    file: str = "kokn"
