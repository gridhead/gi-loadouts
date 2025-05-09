from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SequenceofSolitude(Bow):
    name: str = "Sequence of Solitude"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Silent Trigger"
    refi_list: list[str] = [
        "When an attack hits an opponent, deal AoE DMG equal to 40% of Max HP at the target location. This effect can be triggered once every 15s.",
        "When an attack hits an opponent, deal AoE DMG equal to 50% of Max HP at the target location. This effect can be triggered once every 15s.",
        "When an attack hits an opponent, deal AoE DMG equal to 60% of Max HP at the target location. This effect can be triggered once every 15s.",
        "When an attack hits an opponent, deal AoE DMG equal to 70% of Max HP at the target location. This effect can be triggered once every 15s.",
        "When an attack hits an opponent, deal AoE DMG equal to 80% of Max HP at the target location. This effect can be triggered once every 15s.",
    ]
    file: str = "sest"
