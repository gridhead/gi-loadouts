from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SilvershowerHeartstrings(Bow):
    name: str = "Silvershower Heartstrings"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=14.4)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Dryas's Nocturne"
    refi_list: list[str] = [
            "The equipping character can gain the Remedy effect. When they possess 1/2/3 Remedy stacks, Max HP will increase by 12%/24%/40%. 1 stack may be gained when the following conditions are met: 1 stack for 25s when using an Elemental Skill; 1 stack for 25s when the value of a Bond of Life value increases; 1 stack for 20s for performing healing. Stacks can still be triggered when the equipping character is not on the field. Each stack's duration is counted independently. In addition, when 3 stacks are active, Elemental Burst CRIT Rate will be increased by 28%. This effect will be canceled 4s after falling under 3 stacks.",
            "The equipping character can gain the Remedy effect. When they possess 1/2/3 Remedy stacks, Max HP will increase by 15%/30%/50%. 1 stack may be gained when the following conditions are met: 1 stack for 25s when using an Elemental Skill; 1 stack for 25s when the value of a Bond of Life value increases; 1 stack for 20s for performing healing. Stacks can still be triggered when the equipping character is not on the field. Each stack's duration is counted independently. In addition, when 3 stacks are active, Elemental Burst CRIT Rate will be increased by 35%. This effect will be canceled 4s after falling under 3 stacks.",
            "The equipping character can gain the Remedy effect. When they possess 1/2/3 Remedy stacks, Max HP will increase by 18%/36%/60%. 1 stack may be gained when the following conditions are met: 1 stack for 25s when using an Elemental Skill; 1 stack for 25s when the value of a Bond of Life value increases; 1 stack for 20s for performing healing. Stacks can still be triggered when the equipping character is not on the field. Each stack's duration is counted independently. In addition, when 3 stacks are active, Elemental Burst CRIT Rate will be increased by 42%. This effect will be canceled 4s after falling under 3 stacks.",
            "The equipping character can gain the Remedy effect. When they possess 1/2/3 Remedy stacks, Max HP will increase by 21%/42%/70%. 1 stack may be gained when the following conditions are met: 1 stack for 25s when using an Elemental Skill; 1 stack for 25s when the value of a Bond of Life value increases; 1 stack for 20s for performing healing. Stacks can still be triggered when the equipping character is not on the field. Each stack's duration is counted independently. In addition, when 3 stacks are active, Elemental Burst CRIT Rate will be increased by 49%. This effect will be canceled 4s after falling under 3 stacks.",
            "The equipping character can gain the Remedy effect. When they possess 1/2/3 Remedy stacks, Max HP will increase by 24%/48%/80%. 1 stack may be gained when the following conditions are met: 1 stack for 25s when using an Elemental Skill; 1 stack for 25s when the value of a Bond of Life value increases; 1 stack for 20s for performing healing. Stacks can still be triggered when the equipping character is not on the field. Each stack's duration is counted independently. In addition, when 3 stacks are active, Elemental Burst CRIT Rate will be increased by 56%. This effect will be canceled 4s after falling under 3 stacks.",
        ]
    file: str = "sshs"
