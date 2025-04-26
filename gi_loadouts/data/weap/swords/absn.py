from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Absolution(Sword):
    name: str = "Absolution"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=9.6)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "Deathly Pact"
    refi_list: list[str] = [
        "CRIT DMG increased by 20%. Increasing the value of a Bond of Life increases the DMG the equipping character deals by 16% for 6s. Max 3 stacks.",
        "CRIT DMG increased by 25%. Increasing the value of a Bond of Life increases the DMG the equipping character deals by 20% for 6s. Max 3 stacks.",
        "CRIT DMG increased by 30%. Increasing the value of a Bond of Life increases the DMG the equipping character deals by 24% for 6s. Max 3 stacks.",
        "CRIT DMG increased by 35%. Increasing the value of a Bond of Life increases the DMG the equipping character deals by 28% for 6s. Max 3 stacks.",
        "CRIT DMG increased by 40%. Increasing the value of a Bond of Life increases the DMG the equipping character deals by 32% for 6s. Max 3 stacks."
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=25.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=30.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=35.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=40.0)],
    ]
    file: str = "absn"
