from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TamayurateiNoOhanashi(Polearm):
    name: str = "Tamayuratei no Ohanashi"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=6.7)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Busybody's Running Light"
    refi_list: list[str] = [
        "Increase ATK by 20% and Movement SPD by 10% for 10s when using an Elemental Skill.",
        "Increase ATK by 25% and Movement SPD by 10% for 10s when using an Elemental Skill.",
        "Increase ATK by 30% and Movement SPD by 10% for 10s when using an Elemental Skill.",
        "Increase ATK by 35% and Movement SPD by 10% for 10s when using an Elemental Skill.",
        "Increase ATK by 40% and Movement SPD by 10% for 10s when using an Elemental Skill.",
    ]
    file: str = "tyno"
