from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class AshGravenDrinkingHorn(Catalyst):
    name: str = "Ash-Graven Drinking Horn"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Tupac's Grip"
    refi_list: list[str] = [
        "When an attack hits an opponent, deal AoE DMG equal to 40% of Max HP at the target location. This effect can be triggered once every 15s.",
        "When an attack hits an opponent, deal AoE DMG equal to 50% of Max HP at the target location. This effect can be triggered once every 15s.",
        "When an attack hits an opponent, deal AoE DMG equal to 60% of Max HP at the target location. This effect can be triggered once every 15s.",
        "When an attack hits an opponent, deal AoE DMG equal to 70% of Max HP at the target location. This effect can be triggered once every 15s.",
        "When an attack hits an opponent, deal AoE DMG equal to 80% of Max HP at the target location. This effect can be triggered once every 15s."
    ]
    file: str = "agdh"
