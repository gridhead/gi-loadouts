from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TwinNephrite(Catalyst):
    name: str = "Twin Nephrite"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=3.4)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_3
    refi_name: str = "Guerilla Tactics"
    refi_list: list[str] = [
        "Defeating an opponent increases Movement SPD and ATK by 12% for 15s.",
        "Defeating an opponent increases Movement SPD and ATK by 14% for 15s.",
        "Defeating an opponent increases Movement SPD and ATK by 16% for 15s.",
        "Defeating an opponent increases Movement SPD and ATK by 18% for 15s.",
        "Defeating an opponent increases Movement SPD and ATK by 20% for 15s.",
    ]
    file: str = "twnp"
