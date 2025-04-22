from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier

# Dynamic calculation has not been implemented

class StaffOfTheScarletSands(Polearm):
    name: str = "Staff of the Scarlet Sands"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=9.6)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Heat Haze at Horizon's End"
    refi_list: list[str] = [
        "The equipping character gains 52% of their Elemental Mastery as bonus ATK. When an Elemental Skill hits opponents, the Dream of the Scarlet Sands effect will be gained for 10s: The equipping character will gain 28% of their Elemental Mastery as bonus ATK. Max 3 stacks.",
        "The equipping character gains 65% of their Elemental Mastery as bonus ATK. When an Elemental Skill hits opponents, the Dream of the Scarlet Sands effect will be gained for 10s: The equipping character will gain 35% of their Elemental Mastery as bonus ATK. Max 3 stacks.",
        "The equipping character gains 78% of their Elemental Mastery as bonus ATK. When an Elemental Skill hits opponents, the Dream of the Scarlet Sands effect will be gained for 10s: The equipping character will gain 42% of their Elemental Mastery as bonus ATK. Max 3 stacks.",
        "The equipping character gains 91% of their Elemental Mastery as bonus ATK. When an Elemental Skill hits opponents, the Dream of the Scarlet Sands effect will be gained for 10s: The equipping character will gain 49% of their Elemental Mastery as bonus ATK. Max 3 stacks.",
        "The equipping character gains 104% of their Elemental Mastery as bonus ATK. When an Elemental Skill hits opponents, the Dream of the Scarlet Sands effect will be gained for 10s: The equipping character will gain 56% of their Elemental Mastery as bonus ATK. Max 3 stacks.",
    ]
    file: str = "soss"
