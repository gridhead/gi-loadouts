from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SharpshootersOath(Bow):
    name: str = "Sharpshooter's Oath"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=10.2)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_3
    refi_name: str = "Precise"
    refi_list: list[str] = [
            "Increases DMG against weak spots by 24%.",
            "Increases DMG against weak spots by 30%.",
            "Increases DMG against weak spots by 36%.",
            "Increases DMG against weak spots by 42%.",
            "Increases DMG against weak spots by 48%.",
        ]
    file: str = "ssoh"
