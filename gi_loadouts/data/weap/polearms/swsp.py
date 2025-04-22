from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SkywardSpine(Polearm):
    name: str = "Skyward Spine"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=8.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "Black Wing"
    refi_list: list[str] = [
        "Increases CRIT Rate by 8% and increases Normal ATK SPD by 12%. Additionally, Normal and Charged Attacks hits on opponents have a 50% chance to trigger a vacuum blade that deals 40% of ATK as DMG in a small AoE. This effect can occur no more than once every 2s.",
        "Increases CRIT Rate by 10% and increases Normal ATK SPD by 12%. Additionally, Normal and Charged Attacks hits on opponents have a 50% chance to trigger a vacuum blade that deals 55% of ATK as DMG in a small AoE. This effect can occur no more than once every 2s.",
        "Increases CRIT Rate by 12% and increases Normal ATK SPD by 12%. Additionally, Normal and Charged Attacks hits on opponents have a 50% chance to trigger a vacuum blade that deals 70% of ATK as DMG in a small AoE. This effect can occur no more than once every 2s.",
        "Increases CRIT Rate by 14% and increases Normal ATK SPD by 12%. Additionally, Normal and Charged Attacks hits on opponents have a 50% chance to trigger a vacuum blade that deals 85% of ATK as DMG in a small AoE. This effect can occur no more than once every 2s.",
        "Increases CRIT Rate by 16% and increases Normal ATK SPD by 12%. Additionally, Normal and Charged Attacks hits on opponents have a 50% chance to trigger a vacuum blade that deals 100% of ATK as DMG in a small AoE. This effect can occur no more than once every 2s.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=8.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=10.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=12.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=14.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=16.0)],
    ]
    file: str = "swsp"
