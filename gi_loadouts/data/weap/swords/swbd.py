from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SkywardBlade(Sword):
    name: str = "Skyward Blade"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=12.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Sky-Piercing Fang"
    refi_list: list[str] = [
        "CRIT Rate increased by 4%. Gains Skypiercing Might upon using an Elemental Burst: Increases Movement SPD by 10%, increases ATK SPD by 10%, and Normal and Charged hits deal additional DMG equal to 20% of ATK. Skypiercing Might lasts for 12s.",
        "CRIT Rate increased by 5%. Gains Skypiercing Might upon using an Elemental Burst: Increases Movement SPD by 10%, increases ATK SPD by 10%, and Normal and Charged hits deal additional DMG equal to 25% of ATK. Skypiercing Might lasts for 12s.",
        "CRIT Rate increased by 6%. Gains Skypiercing Might upon using an Elemental Burst: Increases Movement SPD by 10%, increases ATK SPD by 10%, and Normal and Charged hits deal additional DMG equal to 30% of ATK. Skypiercing Might lasts for 12s.",
        "CRIT Rate increased by 7%. Gains Skypiercing Might upon using an Elemental Burst: Increases Movement SPD by 10%, increases ATK SPD by 10%, and Normal and Charged hits deal additional DMG equal to 35% of ATK. Skypiercing Might lasts for 12s.",
        "CRIT Rate increased by 8%. Gains Skypiercing Might upon using an Elemental Burst: Increases Movement SPD by 10%, increases ATK SPD by 10%, and Normal and Charged hits deal additional DMG equal to 40% of ATK. Skypiercing Might lasts for 12s.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=4.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=5.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=7.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=8.0)],
    ]
    file: str = "swbd"
