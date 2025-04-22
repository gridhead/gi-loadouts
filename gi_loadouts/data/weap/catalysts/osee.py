from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class OathswornEye(Catalyst):
    name: str = "Oathsworn Eye"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "People of the Faltering Light"
    refi_list: list[str] = [
        "Increases Energy Recharge by 24% for 10s after using an Elemental Skill.",
        "Increases Energy Recharge by 30% for 10s after using an Elemental Skill.",
        "Increases Energy Recharge by 36% for 10s after using an Elemental Skill.",
        "Increases Energy Recharge by 42% for 10s after using an Elemental Skill.",
        "Increases Energy Recharge by 48% for 10s after using an Elemental Skill.",
    ]
    file: str = "osee"
