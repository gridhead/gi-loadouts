from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class IronSting(Sword):
    name: str = "Iron Sting"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=36.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Infusion Stinger"
    refi_list: list[str] = [
        "Dealing Elemental DMG increases all DMG by 6% for 6s. Max 2 stacks. Can only occur once every 1s.",
        "Dealing Elemental DMG increases all DMG by 7.5% for 6s. Max 2 stacks. Can only occur once every 1s.",
        "Dealing Elemental DMG increases all DMG by 9% for 6s. Max 2 stacks. Can only occur once every 1s.",
        "Dealing Elemental DMG increases all DMG by 10.5% for 6s. Max 2 stacks. Can only occur once every 1s.",
        "Dealing Elemental DMG increases all DMG by 12% for 6s. Max 2 stacks. Can only occur once every 1s.",
    ]
    file: str = "insg"
