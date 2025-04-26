from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class DodocoTales(Catalyst):
    name: str = "Dodoco Tales"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=12.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Dodoventure!"
    refi_list: list[str] = [
        "Normal Attack hits on opponents increase Charged Attack DMG by 16% for 6s. Charged Attack hits on opponents increase ATK by 8% for 6s.",
        "Normal Attack hits on opponents increase Charged Attack DMG by 20% for 6s. Charged Attack hits on opponents increase ATK by 10% for 6s.",
        "Normal Attack hits on opponents increase Charged Attack DMG by 24% for 6s. Charged Attack hits on opponents increase ATK by 12% for 6s.",
        "Normal Attack hits on opponents increase Charged Attack DMG by 28% for 6s. Charged Attack hits on opponents increase ATK by 14% for 6s.",
        "Normal Attack hits on opponents increase Charged Attack DMG by 32% for 6s. Charged Attack hits on opponents increase ATK by 16% for 6s.",
    ]
    file: str = "ddts"
