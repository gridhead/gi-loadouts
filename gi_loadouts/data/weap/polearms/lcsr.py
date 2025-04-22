from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class LithicSpear(Polearm):
    name: str = "Lithic Spear"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Lithic Axiom: Unity"
    refi_list: list[str] = [
        "For every character in the party who hails from Liyue, the character who equips this weapon gains 7% ATK increase and a 3% CRIT Rate increase. This effect stacks up to 4 times.",
        "For every character in the party who hails from Liyue, the character who equips this weapon gains 8% ATK increase and a 4% CRIT Rate increase. This effect stacks up to 4 times.",
        "For every character in the party who hails from Liyue, the character who equips this weapon gains 9% ATK increase and a 5% CRIT Rate increase. This effect stacks up to 4 times.",
        "For every character in the party who hails from Liyue, the character who equips this weapon gains 10% ATK increase and a 6% CRIT Rate increase. This effect stacks up to 4 times.",
        "For every character in the party who hails from Liyue, the character who equips this weapon gains 11% ATK increase and a 7% CRIT Rate increase. This effect stacks up to 4 times.",
    ]
    file: str = "lcsr"
