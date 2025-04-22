from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TheBell(Claymore):
    name: str = "The Bell"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Rebellious Guardian"
    refi_list: list[str] = [
        "Taking DMG generates a shield which absorbs DMG up to 20% of max HP. This shield lasts for 10s or until broken, and can only be triggered once every 45s. While protected by a shield, the character gains 12% increased DMG.",
        "Taking DMG generates a shield which absorbs DMG up to 23% of max HP. This shield lasts for 10s or until broken, and can only be triggered once every 45s. While protected by a shield, the character gains 15% increased DMG.",
        "Taking DMG generates a shield which absorbs DMG up to 26% of max HP. This shield lasts for 10s or until broken, and can only be triggered once every 45s. While protected by a shield, the character gains 18% increased DMG.",
        "Taking DMG generates a shield which absorbs DMG up to 29% of max HP. This shield lasts for 10s or until broken, and can only be triggered once every 45s. While protected by a shield, the character gains 21% increased DMG.",
        "Taking DMG generates a shield which absorbs DMG up to 32% of max HP. This shield lasts for 10s or until broken, and can only be triggered once every 45s. While protected by a shield, the character gains 24% increased DMG.",
    ]
    file: str = "tbll"
