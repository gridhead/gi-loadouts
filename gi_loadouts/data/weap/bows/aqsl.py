from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class AquaSimulacra(Bow):
    name: str = "Aqua Simulacra"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=19.2)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "The Cleansing Form"
    refi_list: list[str] = [
        "HP is increased by 16%. When there are opponents nearby, the DMG dealt by the wielder of this weapon is increased by 20%. This will take effect whether the character is on-field or not.",
        "HP is increased by 20%. When there are opponents nearby, the DMG dealt by the wielder of this weapon is increased by 25%. This will take effect whether the character is on-field or not.",
        "HP is increased by 24%. When there are opponents nearby, the DMG dealt by the wielder of this weapon is increased by 30%. This will take effect whether the character is on-field or not.",
        "HP is increased by 28%. When there are opponents nearby, the DMG dealt by the wielder of this weapon is increased by 35%. This will take effect whether the character is on-field or not.",
        "HP is increased by 32%. When there are opponents nearby, the DMG dealt by the wielder of this weapon is increased by 40%. This will take effect whether the character is on-field or not.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=16.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=24.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=28.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=32.0)],
    ]
    file: str = "aqsl"
