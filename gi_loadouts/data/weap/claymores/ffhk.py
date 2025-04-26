from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FruitfulHook(Claymore):
    name: str = "Fruitful Hook"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "The Weight of Falling Branches"
    refi_list: list[str] = [
        "Increase Plunging Attack CRIT Rate by 16%; After a Plunging Attack hits an opponent, Normal, Charged, and Plunging Attack DMG increased by 16% for 10s.",
        "Increase Plunging Attack CRIT Rate by 20%; After a Plunging Attack hits an opponent, Normal, Charged, and Plunging Attack DMG increased by 20% for 10s.",
        "Increase Plunging Attack CRIT Rate by 24%; After a Plunging Attack hits an opponent, Normal, Charged, and Plunging Attack DMG increased by 24% for 10s.",
        "Increase Plunging Attack CRIT Rate by 28%; After a Plunging Attack hits an opponent, Normal, Charged, and Plunging Attack DMG increased by 28% for 10s.",
        "Increase Plunging Attack CRIT Rate by 32%; After a Plunging Attack hits an opponent, Normal, Charged, and Plunging Attack DMG increased by 32% for 10s.",
    ]
    file: str = "ffhk"
