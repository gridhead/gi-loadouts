from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class WhiteTassel(Polearm):
    name: str = "White Tassel"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=5.1)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_3
    refi_name: str = "Sharp"
    refi_list: list[str] = [
        "Increases Normal Attack DMG by 24%.",
        "Increases Normal Attack DMG by 30%.",
        "Increases Normal Attack DMG by 36%.",
        "Increases Normal Attack DMG by 42%.",
        "Increases Normal Attack DMG by 48%.",
    ]
    file: str = "wetl"
