from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class MountainBracingBolt(Polearm):
    name: str = "Mountain-Bracing Bolt"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=6.7)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Hope Beyond the Peaks"
    refi_list: list[str] = [
        "Decreases Climbing Stamina Consumption by 15% and increases Elemental Skill DMG by 12%. Also, after other nearby party members use Elemental Skills, the equipping character's Elemental Skill DMG will also increase by 12% for 8s.",
        "Decreases Climbing Stamina Consumption by 15% and increases Elemental Skill DMG by 15%. Also, after other nearby party members use Elemental Skills, the equipping character's Elemental Skill DMG will also increase by 15% for 8s.",
        "Decreases Climbing Stamina Consumption by 15% and increases Elemental Skill DMG by 18%. Also, after other nearby party members use Elemental Skills, the equipping character's Elemental Skill DMG will also increase by 18% for 8s.",
        "Decreases Climbing Stamina Consumption by 15% and increases Elemental Skill DMG by 21%. Also, after other nearby party members use Elemental Skills, the equipping character's Elemental Skill DMG will also increase by 21% for 8s.",
        "Decreases Climbing Stamina Consumption by 15% and increases Elemental Skill DMG by 24%. Also, after other nearby party members use Elemental Skills, the equipping character's Elemental Skill DMG will also increase by 24% for 8s.",
    ]
    file: str = "mtbb"
