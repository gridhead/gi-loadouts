from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TheBlackSword(Sword):
    name: str = "The Black Sword"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Justice"
    refi_list: list[str] = [
        "Increases DMG dealt by Normal and Charged Attacks by 20%. Additionally, regenerates 60% of ATK as HP when Normal and Charged Attacks score a CRIT Hit. This effect can occur once every 5s.",
        "Increases DMG dealt by Normal and Charged Attacks by 25%. Additionally, regenerates 70% of ATK as HP when Normal and Charged Attacks score a CRIT Hit. This effect can occur once every 5s.",
        "Increases DMG dealt by Normal and Charged Attacks by 30%. Additionally, regenerates 80% of ATK as HP when Normal and Charged Attacks score a CRIT Hit. This effect can occur once every 5s.",
        "Increases DMG dealt by Normal and Charged Attacks by 35%. Additionally, regenerates 90% of ATK as HP when Normal and Charged Attacks score a CRIT Hit. This effect can occur once every 5s.",
        "Increases DMG dealt by Normal and Charged Attacks by 40%. Additionally, regenerates 100% of ATK as HP when Normal and Charged Attacks score a CRIT Hit. This effect can occur once every 5s.",
    ]
    file: str = "tbsd"
