from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SacrificialGreatsword(Claymore):
    name: str = "Sacrificial Greatsword"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=6.7)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Composed"
    refi_list: list[str] = [
        "After dealing damage to an opponent with an Elemental Skill, the skill has a 40% chance to end its own CD. Can only occur once every 30s.",
        "After dealing damage to an opponent with an Elemental Skill, the skill has a 50% chance to end its own CD. Can only occur once every 26s.",
        "After dealing damage to an opponent with an Elemental Skill, the skill has a 60% chance to end its own CD. Can only occur once every 22s.",
        "After dealing damage to an opponent with an Elemental Skill, the skill has a 70% chance to end its own CD. Can only occur once every 19s.",
        "After dealing damage to an opponent with an Elemental Skill, the skill has a 80% chance to end its own CD. Can only occur once every 16s.",
    ]
    file: str = "sfgs"
