from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FootprintoftheRainbow(Polearm):
    name: str = "Footprint of the Rainbow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=11.3)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Pact of Flowing Springs"
    refi_list: list[str] = [
        "Using an Elemental Skill increases DEF by 16% for 15s.",
        "Using an Elemental Skill increases DEF by 20% for 15s.",
        "Using an Elemental Skill increases DEF by 24% for 15s.",
        "Using an Elemental Skill increases DEF by 28% for 15s.",
        "Using an Elemental Skill increases DEF by 32% for 15s.",
    ]
    file: str = "fotr"
