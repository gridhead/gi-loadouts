from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class BlackTassel(Polearm):
    name: str = "Black Tassel"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=10.2)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_3
    refi_name: str = "Bane of the Soft"
    refi_list: list[str] = [
        "Increases DMG against slimes by 40%.",
        "Increases DMG against slimes by 50%.",
        "Increases DMG against slimes by 60%.",
        "Increases DMG against slimes by 70%.",
        "Increases DMG against slimes by 80%.",
    ]
    file: str = "bktl"
