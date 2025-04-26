from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FesteringDesire(Sword):
    name: str = "Festering Desire"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=10.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Undying Admiration"
    refi_list: list[str] = [
        "Increases Elemental Skill DMG by 16% and Elemental Skill CRIT Rate by 6%.",
        "Increases Elemental Skill DMG by 20% and Elemental Skill CRIT Rate by 7.5%.",
        "Increases Elemental Skill DMG by 24% and Elemental Skill CRIT Rate by 9%.",
        "Increases Elemental Skill DMG by 28% and Elemental Skill CRIT Rate by 10.5%.",
        "Increases Elemental Skill DMG by 32% and Elemental Skill CRIT Rate by 12%.",
    ]
    file: str = "ftds"
