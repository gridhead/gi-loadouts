from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class BalladoftheFjords(Polearm):
    name: str = "Ballad of the Fjords"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Tales of the Tundra"
    refi_list: list[str] = [
        "When there are at least 3 different Elemental Types in your party, Elemental Mastery will be increased by 120.",
        "When there are at least 3 different Elemental Types in your party, Elemental Mastery will be increased by 150.",
        "When there are at least 3 different Elemental Types in your party, Elemental Mastery will be increased by 180.",
        "When there are at least 3 different Elemental Types in your party, Elemental Mastery will be increased by 210.",
        "When there are at least 3 different Elemental Types in your party, Elemental Mastery will be increased by 240.",
    ]
    file: str = "botf"
