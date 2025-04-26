from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FerrousShadow(Claymore):
    name: str = "Ferrous Shadow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=7.7)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_3
    refi_name: str = "Unbending"
    refi_list: list[str] = [
        "When HP falls below 70%, increases Charged Attack DMG by 30%, and Charged Attacks become much harder to interrupt.",
        "When HP falls below 75%, increases Charged Attack DMG by 35%, and Charged Attacks become much harder to interrupt.",
        "When HP falls below 80%, increases Charged Attack DMG by 40%, and Charged Attacks become much harder to interrupt.",
        "When HP falls below 85%, increases Charged Attack DMG by 45%, and Charged Attacks become much harder to interrupt.",
        "When HP falls below 90%, increases Charged Attack DMG by 50%, and Charged Attacks become much harder to interrupt.",
    ]
    file: str = "fosd"
