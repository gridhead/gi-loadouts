from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class DawningFrost(Catalyst):
    name: str = "Dawning Frost"
    seco_stat: WeaponStat = WeaponStat(
        stat_name=WeaponStatType.critical_damage_perc, stat_data=12.0
    )
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Nocturnal Dreams"
    refi_list: list[str] = [
        "For 10s after a Charged Attack hits an opponent, Elemental Mastery is increased by 72. For 10s after an Elemental Skill hits an opponent, Elemental Mastery is increased by 48.",
        "For 10s after a Charged Attack hits an opponent, Elemental Mastery is increased by 90. For 10s after an Elemental Skill hits an opponent, Elemental Mastery is increased by 60.",
        "For 10s after a Charged Attack hits an opponent, Elemental Mastery is increased by 108. For 10s after an Elemental Skill hits an opponent, Elemental Mastery is increased by 72.",
        "For 10s after a Charged Attack hits an opponent, Elemental Mastery is increased by 126. For 10s after an Elemental Skill hits an opponent, Elemental Mastery is increased by 84.",
        "For 10s after a Charged Attack hits an opponent, Elemental Mastery is increased by 144. For 10s after an Elemental Skill hits an opponent, Elemental Mastery is increased by 96.",
    ]
    file: str = "dgft"
