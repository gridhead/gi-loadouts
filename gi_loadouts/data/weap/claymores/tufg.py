from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TheUnforged(Claymore):
    name: str = "The Unforged"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=10.8)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Golden Majesty"
    refi_list: list[str] = [
        "Increases Shield Strength by 20%. Scoring hits on opponents increases ATK by 4% for 8s. Max 5 stacks. Can only occur once every 0.3s. While protected by a shield, this ATK increase effect is increased by 100%.",
        "Increases Shield Strength by 25%. Scoring hits on opponents increases ATK by 5% for 8s. Max 5 stacks. Can only occur once every 0.3s. While protected by a shield, this ATK increase effect is increased by 100%.",
        "Increases Shield Strength by 30%. Scoring hits on opponents increases ATK by 6% for 8s. Max 5 stacks. Can only occur once every 0.3s. While protected by a shield, this ATK increase effect is increased by 100%.",
        "Increases Shield Strength by 35%. Scoring hits on opponents increases ATK by 7% for 8s. Max 5 stacks. Can only occur once every 0.3s. While protected by a shield, this ATK increase effect is increased by 100%.",
        "Increases Shield Strength by 40%. Scoring hits on opponents increases ATK by 8% for 8s. Max 5 stacks. Can only occur once every 0.3s. While protected by a shield, this ATK increase effect is increased by 100%.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.shield_strength_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.shield_strength_perc, stat_data=25.0)],
        [WeaponStat(stat_name=WeaponStatType.shield_strength_perc, stat_data=30.0)],
        [WeaponStat(stat_name=WeaponStatType.shield_strength_perc, stat_data=35.0)],
        [WeaponStat(stat_name=WeaponStatType.shield_strength_perc, stat_data=40.0)],
    ]
    file: str = "tufg"
