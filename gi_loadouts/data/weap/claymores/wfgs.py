from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class WolfsGravestone(Claymore):
    name: str = "Wolf's Gravestone"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=10.8)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Wolfish Tracker"
    refi_list: list[str] = [
        "Increases ATK by 20%. On hit, attacks against opponents with less than 30% HP increase all party members' ATK by 40% for 12s. Can only occur once every 30s.",
        "Increases ATK by 25%. On hit, attacks against opponents with less than 30% HP increase all party members' ATK by 50% for 12s. Can only occur once every 30s.",
        "Increases ATK by 30%. On hit, attacks against opponents with less than 30% HP increase all party members' ATK by 60% for 12s. Can only occur once every 30s.",
        "Increases ATK by 35%. On hit, attacks against opponents with less than 30% HP increase all party members' ATK by 70% for 12s. Can only occur once every 30s.",
        "Increases ATK by 40%. On hit, attacks against opponents with less than 30% HP increase all party members' ATK by 80% for 12s. Can only occur once every 30s."
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=25.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=30.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=35.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=40.0)],
    ]
    file: str = "wfgs"
