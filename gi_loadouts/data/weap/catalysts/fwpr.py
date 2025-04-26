from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FlowingPurity(Catalyst):
    name: str = "Flowing Purity"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Unfinished Masterpiece"
    refi_list: list[str] = [
        "When using an Elemental Skill, All Elemental DMG Bonus will be increased by 8% for 15s, and a Bond of Life worth 24% of Max HP will be granted. This effect can be triggered once every 10s. When the Bond Of Life is cleared, every 1,000 HP cleared in the process will provide 2% All Elemental DMG Bonus, up to a maximum of 12%. This effect lasts 15s.",
        "When using an Elemental Skill, All Elemental DMG Bonus will be increased by 10% for 15s, and a Bond of Life worth 24% of Max HP will be granted. This effect can be triggered once every 10s. When the Bond Of Life is cleared, every 1,000 HP cleared in the process will provide 2.5% All Elemental DMG Bonus, up to a maximum of 15%. This effect lasts 15s.",
        "When using an Elemental Skill, All Elemental DMG Bonus will be increased by 12% for 15s, and a Bond of Life worth 24% of Max HP will be granted. This effect can be triggered once every 10s. When the Bond Of Life is cleared, every 1,000 HP cleared in the process will provide 3% All Elemental DMG Bonus, up to a maximum of 18%. This effect lasts 15s.",
        "When using an Elemental Skill, All Elemental DMG Bonus will be increased by 14% for 15s, and a Bond of Life worth 24% of Max HP will be granted. This effect can be triggered once every 10s. When the Bond Of Life is cleared, every 1,000 HP cleared in the process will provide 3.5% All Elemental DMG Bonus, up to a maximum of 21%. This effect lasts 15s.",
        "When using an Elemental Skill, All Elemental DMG Bonus will be increased by 16% for 15s, and a Bond of Life worth 24% of Max HP will be granted. This effect can be triggered once every 10s. When the Bond Of Life is cleared, every 1,000 HP cleared in the process will provide 4% All Elemental DMG Bonus, up to a maximum of 24%. This effect lasts 15s.",
    ]
    file: str = "fwpr"
