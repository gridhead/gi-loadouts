from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class WolfFang(Sword):
    name: str = "Wolf-Fang"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Northwind Wolf"
    refi_list: list[str] = [
        "DMG dealt by Elemental Skill and Elemental Burst is increased by 16%. When an Elemental Skill hits an opponent, its CRIT Rate will be increased by 2%. When an Elemental Burst hits an opponent, its CRIT Rate will be increased by 2%. Both of these effects last 10s separately, have 4 max stacks, and can be triggered once every 0.1s.",
        "DMG dealt by Elemental Skill and Elemental Burst is increased by 20%. When an Elemental Skill hits an opponent, its CRIT Rate will be increased by 2.5%. When an Elemental Burst hits an opponent, its CRIT Rate will be increased by 2.5%. Both of these effects last 10s separately, have 4 max stacks, and can be triggered once every 0.1s.",
        "DMG dealt by Elemental Skill and Elemental Burst is increased by 24%. When an Elemental Skill hits an opponent, its CRIT Rate will be increased by 3%. When an Elemental Burst hits an opponent, its CRIT Rate will be increased by 3%. Both of these effects last 10s separately, have 4 max stacks, and can be triggered once every 0.1s.",
        "DMG dealt by Elemental Skill and Elemental Burst is increased by 28%. When an Elemental Skill hits an opponent, its CRIT Rate will be increased by 3.5%. When an Elemental Burst hits an opponent, its CRIT Rate will be increased by 3.5%. Both of these effects last 10s separately, have 4 max stacks, and can be triggered once every 0.1s.",
        "DMG dealt by Elemental Skill and Elemental Burst is increased by 32%. When an Elemental Skill hits an opponent, its CRIT Rate will be increased by 4%. When an Elemental Burst hits an opponent, its CRIT Rate will be increased by 4%. Both of these effects last 10s separately, have 4 max stacks, and can be triggered once every 0.1s.",
    ]
    file: str = "wffg"
