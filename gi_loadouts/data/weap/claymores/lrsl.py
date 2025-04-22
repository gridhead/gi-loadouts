from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class LuxuriousSeaLord(Claymore):
    name: str = "Luxurious Sea-Lord"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=12.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Oceanic Victory"
    refi_list: list[str] = [
        "Increases Elemental Burst DMG by 12%. When Elemental Burst hits opponents, there is a 100% chance of summoning a huge onrush of tuna that deals 100% ATK as AoE DMG. This effect can occur once every 15s.",
        "Increases Elemental Burst DMG by 15%. When Elemental Burst hits opponents, there is a 100% chance of summoning a huge onrush of tuna that deals 125% ATK as AoE DMG. This effect can occur once every 15s.",
        "Increases Elemental Burst DMG by 18%. When Elemental Burst hits opponents, there is a 100% chance of summoning a huge onrush of tuna that deals 150% ATK as AoE DMG. This effect can occur once every 15s.",
        "Increases Elemental Burst DMG by 21%. When Elemental Burst hits opponents, there is a 100% chance of summoning a huge onrush of tuna that deals 175% ATK as AoE DMG. This effect can occur once every 15s.",
        "Increases Elemental Burst DMG by 24%. When Elemental Burst hits opponents, there is a 100% chance of summoning a huge onrush of tuna that deals 200% ATK as AoE DMG. This effect can occur once every 15s.",
    ]
    file: str = "lrsl"
