from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TheCatch(Polearm):
    name: str = "\"The Catch\""
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=10.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Shanty"
    refi_list: list[str] = [
        "Increases Elemental Burst DMG by 16% and Elemental Burst CRIT Rate by 6%.",
        "Increases Elemental Burst DMG by 20% and Elemental Burst CRIT Rate by 7.5%.",
        "Increases Elemental Burst DMG by 24% and Elemental Burst CRIT Rate by 9%.",
        "Increases Elemental Burst DMG by 28% and Elemental Burst CRIT Rate by 10.5%.",
        "Increases Elemental Burst DMG by 32% and Elemental Burst CRIT Rate by 12%.",
    ]
    file: str = "tcth"
