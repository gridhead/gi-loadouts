from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class ThrillingTalesofDragonSlayers(Catalyst):
    name: str = "Thrilling Tales of Dragon Slayers"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=7.7)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_3
    refi_name: str = "Heritage"
    refi_list: list[str] = [
        "When switching characters, the new character taking the field has their ATK increased by 24% for 10s. This effect can only occur once every 20s.",
        "When switching characters, the new character taking the field has their ATK increased by 30% for 10s. This effect can only occur once every 20s.",
        "When switching characters, the new character taking the field has their ATK increased by 36% for 10s. This effect can only occur once every 20s.",
        "When switching characters, the new character taking the field has their ATK increased by 42% for 10s. This effect can only occur once every 20s.",
        "When switching characters, the new character taking the field has their ATK increased by 48% for 10s. This effect can only occur once every 20s.",
    ]
    file: str = "ttds"
