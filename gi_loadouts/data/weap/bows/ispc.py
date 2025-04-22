from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class IbisPiercer(Bow):
    name: str = "Ibis Piercer"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Secret Wisdom's Favor"
    refi_list: list[str] = [
        "The character's Elemental Mastery will increase by 40 within 6s after Charged Attacks hit opponents. Max 2 stacks. This effect can triggered once every 0.5s.",
        "The character's Elemental Mastery will increase by 50 within 6s after Charged Attacks hit opponents. Max 2 stacks. This effect can triggered once every 0.5s.",
        "The character's Elemental Mastery will increase by 60 within 6s after Charged Attacks hit opponents. Max 2 stacks. This effect can triggered once every 0.5s.",
        "The character's Elemental Mastery will increase by 70 within 6s after Charged Attacks hit opponents. Max 2 stacks. This effect can triggered once every 0.5s.",
        "The character's Elemental Mastery will increase by 80 within 6s after Charged Attacks hit opponents. Max 2 stacks. This effect can triggered once every 0.5s.",
    ]
    file: str = "ispc"
