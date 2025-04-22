from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class ChainBreaker(Bow):
    name: str = "Chain Breaker"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Flower—Feather Song"
    refi_list: list[str] = [
        "For every party member from Natlan or who has a different Elemental Type from the equipping character, the equipping character gains 4.8% increased ATK. When there are no less than 3 of the aforementioned characters, the equipping character gains 24 Elemental Mastery.",
        "For every party member from Natlan or who has a different Elemental Type from the equipping character, the equipping character gains 6% increased ATK. When there are no less than 3 of the aforementioned characters, the equipping character gains 30 Elemental Mastery.",
        "For every party member from Natlan or who has a different Elemental Type from the equipping character, the equipping character gains 7.2% increased ATK. When there are no less than 3 of the aforementioned characters, the equipping character gains 36 Elemental Mastery.",
        "For every party member from Natlan or who has a different Elemental Type from the equipping character, the equipping character gains 8.4% increased ATK. When there are no less than 3 of the aforementioned characters, the equipping character gains 42 Elemental Mastery.",
        "For every party member from Natlan or who has a different Elemental Type from the equipping character, the equipping character gains 9.6% increased ATK. When there are no less than 3 of the aforementioned characters, the equipping character gains 48 Elemental Mastery.",
    ]
    file: str = "cnbr"
