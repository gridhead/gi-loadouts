from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class CalamityOfEshu(Sword):
    name: str = "Calamity of Eshu"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Diffusing Boundary"
    refi_list: list[str] = [
        "While characters are protected by a Shield, DMG dealt by Normal and Charged Attacks is increased by 20%, and Normal and Charged Attack CRIT Rate is increased by 8%.",
        "While characters are protected by a Shield, DMG dealt by Normal and Charged Attacks is increased by 25%, and Normal and Charged Attack CRIT Rate is increased by 10%.",
        "While characters are protected by a Shield, DMG dealt by Normal and Charged Attacks is increased by 30%, and Normal and Charged Attack CRIT Rate is increased by 12%.",
        "While characters are protected by a Shield, DMG dealt by Normal and Charged Attacks is increased by 35%, and Normal and Charged Attack CRIT Rate is increased by 14%.",
        "While characters are protected by a Shield, DMG dealt by Normal and Charged Attacks is increased by 40%, and Normal and Charged Attack CRIT Rate is increased by 16%.",
    ]
    file: str = "cmoe"
