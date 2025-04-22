from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class PrototypeStarglitter(Polearm):
    name: str = "Prototype Starglitter"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=10.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Magic Affinity"
    refi_list: list[str] = [
        "After using an Elemental Skill, increases Normal and Charged Attack DMG by 8% for 12s. Max 2 stacks.",
        "After using an Elemental Skill, increases Normal and Charged Attack DMG by 10% for 12s. Max 2 stacks.",
        "After using an Elemental Skill, increases Normal and Charged Attack DMG by 12% for 12s. Max 2 stacks.",
        "After using an Elemental Skill, increases Normal and Charged Attack DMG by 14% for 12s. Max 2 stacks.",
        "After using an Elemental Skill, increases Normal and Charged Attack DMG by 16% for 12s. Max 2 stacks.",
    ]
    file: str = "ptsg"
