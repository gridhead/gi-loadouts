from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class PrimordialJadeCutter(Sword):
    name: str = "Primordial Jade Cutter"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=9.6)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Protector's Virtue"
    refi_list: list[str] = [
            "HP increased by 20%. Additionally, provides an ATK Bonus based on 1.2% of the wielder's Max HP.",
            "HP increased by 25%. Additionally, provides an ATK Bonus based on 1.5% of the wielder's Max HP.",
            "HP increased by 30%. Additionally, provides an ATK Bonus based on 1.8% of the wielder's Max HP.",
            "HP increased by 35%. Additionally, provides an ATK Bonus based on 2.1% of the wielder's Max HP.",
            "HP increased by 40%. Additionally, provides an ATK Bonus based on 2.4% of the wielder's Max HP.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=25.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=30.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=35.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=40.0)],
    ]
    file: str = "pmjc"
