from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class LithicBlade(Claymore):
    name: str = "Lithic Blade"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Lithic Axiom: Unity"
    refi_list: list[str] = [
        "For every character in the party who hails from Liyue, the character who equips this weapon gains 7% ATK increase and 3% CRIT Rate increase. This effect stacks up to 4 times.",
        "For every character in the party who hails from Liyue, the character who equips this weapon gains 8% ATK increase and 4% CRIT Rate increase. This effect stacks up to 4 times.",
        "For every character in the party who hails from Liyue, the character who equips this weapon gains 9% ATK increase and 5% CRIT Rate increase. This effect stacks up to 4 times.",
        "For every character in the party who hails from Liyue, the character who equips this weapon gains 10% ATK increase and 6% CRIT Rate increase. This effect stacks up to 4 times.",
        "For every character in the party who hails from Liyue, the character who equips this weapon gains 11% ATK increase and 7% CRIT Rate increase. This effect stacks up to 4 times.",
    ]
    file: str = "libd"
