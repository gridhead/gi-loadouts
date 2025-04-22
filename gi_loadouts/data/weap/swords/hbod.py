from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class HarbingerofDawn(Sword):
    name: str = "Harbinger of Dawn"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=10.2)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_3
    refi_name: str = "Vigorous"
    refi_list: list[str] = [
        "When HP is above 90%, increases CRIT Rate by 14%.",
        "When HP is above 90%, increases CRIT Rate by 17.5%.",
        "When HP is above 90%, increases CRIT Rate by 21%.",
        "When HP is above 90%, increases CRIT Rate by 24.5%.",
        "When HP is above 90%, increases CRIT Rate by 28%.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=14.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=17.5)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=21.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=24.5)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=28.0)],
    ]
    file: str = "hbod"
