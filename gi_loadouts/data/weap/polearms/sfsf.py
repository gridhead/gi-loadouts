from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SacrificersStaff(Polearm):
    name: str = "Sacrificer's Staff"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=2.0)
    tier: Tier = Tier.Tier_4
    rare: Rare = Rare.Star_4
    refi_name: str = "Untainted Desire"
    refi_list: list[str] = [
        "For 6s after an Elemental Skill hits an opponent, ATK is increased by 8% and Energy Recharge is increased by 6%. Max 3 stacks. This effect can be triggered even when the equipping character is off-field.",
        "For 6s after an Elemental Skill hits an opponent, ATK is increased by 10% and Energy Recharge is increased by 7.5%. Max 3 stacks. This effect can be triggered even when the equipping character is off-field.",
        "For 6s after an Elemental Skill hits an opponent, ATK is increased by 12% and Energy Recharge is increased by 9%. Max 3 stacks. This effect can be triggered even when the equipping character is off-field.",
        "For 6s after an Elemental Skill hits an opponent, ATK is increased by 14% and Energy Recharge is increased by 10.5%. Max 3 stacks. This effect can be triggered even when the equipping character is off-field.",
        "For 6s after an Elemental Skill hits an opponent, ATK is increased by 16% and Energy Recharge is increased by 12%. Max 3 stacks. This effect can be triggered even when the equipping character is off-field.",
    ]
    file: str = "sfsf"
