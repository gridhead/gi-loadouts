from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Rust(Bow):
    name: str = "Rust"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Rapid Firing"
    refi_list: list[str] = [
            "Increases Normal Attack DMG by 40% but decreases Charged Attack DMG by 10%.",
            "Increases Normal Attack DMG by 50% but decreases Charged Attack DMG by 10%.",
            "Increases Normal Attack DMG by 60% but decreases Charged Attack DMG by 10%.",
            "Increases Normal Attack DMG by 70% but decreases Charged Attack DMG by 10%.",
            "Increases Normal Attack DMG by 80% but decreases Charged Attack DMG by 10%.",
        ]
    file: str = "rust"
