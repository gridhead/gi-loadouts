from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Deathmatch(Polearm):
    name: str = "Deathmatch"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=8.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Gladiator"
    refi_list: list[str] = [
        "If there are at least 2 opponents nearby, ATK is increased by 16% and DEF is increased by 16%. If there are fewer than 2 opponents nearby, ATK is increased by 24%.",
        "If there are at least 2 opponents nearby, ATK is increased by 20% and DEF is increased by 20%. If there are fewer than 2 opponents nearby, ATK is increased by 30%.",
        "If there are at least 2 opponents nearby, ATK is increased by 24% and DEF is increased by 24%. If there are fewer than 2 opponents nearby, ATK is increased by 36%.",
        "If there are at least 2 opponents nearby, ATK is increased by 28% and DEF is increased by 28%. If there are fewer than 2 opponents nearby, ATK is increased by 42%.",
        "If there are at least 2 opponents nearby, ATK is increased by 32% and DEF is increased by 32%. If there are fewer than 2 opponents nearby, ATK is increased by 48%.",
    ]
    file: str = "dtmh"
