from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FluteofEzpitzal(Sword):
    name: str = "Flute of Ezpitzal"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=15.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Smoke-and-Mirror Mystery"
    refi_list: list[str] = [
        "Using an Elemental Skill increases DEF by 16% for 15s.",
        "Using an Elemental Skill increases DEF by 20% for 15s.",
        "Using an Elemental Skill increases DEF by 24% for 15s.",
        "Using an Elemental Skill increases DEF by 28% for 15s.",
        "Using an Elemental Skill increases DEF by 32% for 15s.",
    ]
    file: str = "foel"
