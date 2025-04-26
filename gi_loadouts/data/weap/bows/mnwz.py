from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class MitternachtsWaltz(Bow):
    name: str = "Mitternachts Waltz"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.damage_bonus_physical_perc, stat_data=11.3)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Evernight Duet"
    refi_list: list[str] = [
        "Normal Attack hits on opponents increase Elemental Skill DMG by 20% for 5s. Elemental Skill hits on opponents increase Normal Attack DMG by 20% for 5s.",
        "Normal Attack hits on opponents increase Elemental Skill DMG by 25% for 5s. Elemental Skill hits on opponents increase Normal Attack DMG by 25% for 5s.",
        "Normal Attack hits on opponents increase Elemental Skill DMG by 30% for 5s. Elemental Skill hits on opponents increase Normal Attack DMG by 30% for 5s.",
        "Normal Attack hits on opponents increase Elemental Skill DMG by 35% for 5s. Elemental Skill hits on opponents increase Normal Attack DMG by 35% for 5s.",
        "Normal Attack hits on opponents increase Elemental Skill DMG by 40% for 5s. Elemental Skill hits on opponents increase Normal Attack DMG by 40% for 5s.",
    ]
    file: str = "mnwz"
