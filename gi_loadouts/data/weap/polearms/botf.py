
from typing import List

from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Polearm, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.base.tier import Tier


class BalladoftheFjords(Polearm):
    name: str = "Ballad of the Fjords"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate, stat_data=6.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_list: List[str] = [
        "When there are at least 3 different Elemental Types in your party, Elemental Mastery will be increased by 120.",
        "When there are at least 3 different Elemental Types in your party, Elemental Mastery will be increased by 150.",
        "When there are at least 3 different Elemental Types in your party, Elemental Mastery will be increased by 180.",
        "When there are at least 3 different Elemental Types in your party, Elemental Mastery will be increased by 210.",
        "When there are at least 3 different Elemental Types in your party, Elemental Mastery will be increased by 240.",
    ]
