from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class WindblumeOde(Bow):
    name: str = "Windblume Ode"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=36.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Windblume Wish"
    refi_list: list[str] = [
            "After using an Elemental Skill, receive a boon from the ancient wish of the Windblume, increasing ATK by 16% for 6s.",
            "After using an Elemental Skill, receive a boon from the ancient wish of the Windblume, increasing ATK by 20% for 6s.",
            "After using an Elemental Skill, receive a boon from the ancient wish of the Windblume, increasing ATK by 24% for 6s.",
            "After using an Elemental Skill, receive a boon from the ancient wish of the Windblume, increasing ATK by 28% for 6s.",
            "After using an Elemental Skill, receive a boon from the ancient wish of the Windblume, increasing ATK by 32% for 6s.",
        ]
    file: str = "wboe"
