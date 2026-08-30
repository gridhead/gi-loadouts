from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class CovenantOfFrostAndSnow(Bow):
    name: str = "Covenant of Frost and Snow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=11.3)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "The Law's Equilibrium"
    refi_list: list[str] = [
        "For 12s after the equipping character uses an Elemental Skill, their Elemental Mastery is increased by 120.",
        "For 12s after the equipping character uses an Elemental Skill, their Elemental Mastery is increased by 150.",
        "For 12s after the equipping character uses an Elemental Skill, their Elemental Mastery is increased by 180.",
        "For 12s after the equipping character uses an Elemental Skill, their Elemental Mastery is increased by 210.",
        "For 12s after the equipping character uses an Elemental Skill, their Elemental Mastery is increased by 240.",
    ]
    file: str = "cofs"
