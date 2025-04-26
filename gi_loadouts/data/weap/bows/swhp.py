from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SkywardHarp(Bow):
    name: str = "Skyward Harp"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=4.8)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "Echoing Ballad"
    refi_list: list[str] = [
        "Increases CRIT DMG by 20%. Hits have a 60% chance to inflict a small AoE attack, dealing 125% Physical ATK DMG. Can only occur once every 4s.",
        "Increases CRIT DMG by 25%. Hits have a 70% chance to inflict a small AoE attack, dealing 125% Physical ATK DMG. Can only occur once every 3.5s.",
        "Increases CRIT DMG by 30%. Hits have a 80% chance to inflict a small AoE attack, dealing 125% Physical ATK DMG. Can only occur once every 3s.",
        "Increases CRIT DMG by 35%. Hits have a 90% chance to inflict a small AoE attack, dealing 125% Physical ATK DMG. Can only occur once every 2.5s.",
        "Increases CRIT DMG by 40%. Hits have a 100% chance to inflict a small AoE attack, dealing 125% Physical ATK DMG. Can only occur once every 2s.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=25.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=30.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=35.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=40.0)],
    ]
    file: str = "swhp"
