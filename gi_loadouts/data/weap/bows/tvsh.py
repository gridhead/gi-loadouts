from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TheViridescentHunt(Bow):
    name: str = "The Viridescent Hunt"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Verdant Wind"
    refi_list: list[str] = [
            "Upon hit, Normal and Aimed Shot Attacks have a 50% chance to generate a Cyclone, which will continuously attract surrounding opponents, dealing 40% of ATK as DMG to these opponents every 0.5s for 4s. This effect can only occur once every 14s.",
            "Upon hit, Normal and Aimed Shot Attacks have a 50% chance to generate a Cyclone, which will continuously attract surrounding opponents, dealing 50% of ATK as DMG to these opponents every 0.5s for 4s. This effect can only occur once every 13s.",
            "Upon hit, Normal and Aimed Shot Attacks have a 50% chance to generate a Cyclone, which will continuously attract surrounding opponents, dealing 60% of ATK as DMG to these opponents every 0.5s for 4s. This effect can only occur once every 12s.",
            "Upon hit, Normal and Aimed Shot Attacks have a 50% chance to generate a Cyclone, which will continuously attract surrounding opponents, dealing 70% of ATK as DMG to these opponents every 0.5s for 4s. This effect can only occur once every 11s.",
            "Upon hit, Normal and Aimed Shot Attacks have a 50% chance to generate a Cyclone, which will continuously attract surrounding opponents, dealing 80% of ATK as DMG to these opponents every 0.5s for 4s. This effect can only occur once every 10s.",
        ]
    file: str = "tvsh"
