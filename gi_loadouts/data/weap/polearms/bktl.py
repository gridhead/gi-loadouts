from typing import List

from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Polearm, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.base.tier import Tier


class BlackTassel(Polearm):
    name: str = "Black Tassel"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_3
    refi_list: List[str] = [
        "Increases DMG against slimes by 40%.",
        "Increases DMG against slimes by 50%.",
        "Increases DMG against slimes by 60%.",
        "Increases DMG against slimes by 70%.",
        "Increases DMG against slimes by 80%.",
    ]
