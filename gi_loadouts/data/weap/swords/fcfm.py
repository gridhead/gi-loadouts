from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FleuveCendreFerryman(Sword):
    name: str = "Fleuve Cendre Ferryman"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=10.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Ironbone"
    refi_list: list[str] = [
        "Increases Elemental Skill CRIT Rate by 8%. Additionally, increases Energy Recharge by 16% for 5s after using an Elemental Skill.",
        "Increases Elemental Skill CRIT Rate by 10%. Additionally, increases Energy Recharge by 20% for 5s after using an Elemental Skill.",
        "Increases Elemental Skill CRIT Rate by 12%. Additionally, increases Energy Recharge by 24% for 5s after using an Elemental Skill.",
        "Increases Elemental Skill CRIT Rate by 14%. Additionally, increases Energy Recharge by 28% for 5s after using an Elemental Skill.",
        "Increases Elemental Skill CRIT Rate by 16%. Additionally, increases Energy Recharge by 32% for 5s after using an Elemental Skill.",
    ]
    file: str = "fcfm"
