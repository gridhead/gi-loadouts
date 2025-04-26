from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class RedhornStonethresher(Claymore):
    name: str = "Redhorn Stonethresher"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=19.2)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Gokadaiou Otogibanashi"
    refi_list: list[str] = [
        "DEF is increased by 28%. Normal and Charged Attack DMG is increased by 40% of DEF.",
        "DEF is increased by 35%. Normal and Charged Attack DMG is increased by 50% of DEF.",
        "DEF is increased by 42%. Normal and Charged Attack DMG is increased by 60% of DEF.",
        "DEF is increased by 49%. Normal and Charged Attack DMG is increased by 70% of DEF.",
        "DEF is increased by 56%. Normal and Charged Attack DMG is increased by 80% of DEF.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=28.0)],
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=35.0)],
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=42.0)],
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=49.0)],
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=56.0)],
    ]
    file: str = "rhst"
