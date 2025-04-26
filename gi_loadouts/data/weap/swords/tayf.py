from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TheAlleyFlash(Sword):
    name: str = "The Alley Flash"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=12.0)
    tier: Tier = Tier.Tier_4
    rare: Rare = Rare.Star_4
    refi_name: str = "Itinerant Hero"
    refi_list: list[str] = [
        "Increases DMG dealt by the character equipping this weapon by 12%. Taking DMG disables this effect for 5s.",
        "Increases DMG dealt by the character equipping this weapon by 15%. Taking DMG disables this effect for 5s.",
        "Increases DMG dealt by the character equipping this weapon by 18%. Taking DMG disables this effect for 5s.",
        "Increases DMG dealt by the character equipping this weapon by 21%. Taking DMG disables this effect for 5s.",
        "Increases DMG dealt by the character equipping this weapon by 24%. Taking DMG disables this effect for 5s.",
    ]
    file: str = "tayf"
