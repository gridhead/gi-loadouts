from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SunnyMorningSleepIn(Catalyst):
    name: str = "Sunny Morning Sleep-In"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=58.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Bathhouses, Hawks, and Narukami"
    refi_list: list[str] = [
        "Elemental Mastery increases by 120 for 6s after triggering Swirl. Elemental Mastery increases by 96 for 9s after the wielder's Elemental Skill hits an opponent. Elemental Mastery increases by 32 for 30s after the wielder's Elemental Burst hits an opponent.",
        "Elemental Mastery increases by 150 for 6s after triggering Swirl. Elemental Mastery increases by 120 for 9s after the wielder's Elemental Skill hits an opponent. Elemental Mastery increases by 40 for 30s after the wielder's Elemental Burst hits an opponent.",
        "Elemental Mastery increases by 180 for 6s after triggering Swirl. Elemental Mastery increases by 144 for 9s after the wielder's Elemental Skill hits an opponent. Elemental Mastery increases by 48 for 30s after the wielder's Elemental Burst hits an opponent.",
        "Elemental Mastery increases by 210 for 6s after triggering Swirl. Elemental Mastery increases by 168 for 9s after the wielder's Elemental Skill hits an opponent. Elemental Mastery increases by 56 for 30s after the wielder's Elemental Burst hits an opponent.",
        "Elemental Mastery increases by 240 for 6s after triggering Swirl. Elemental Mastery increases by 192 for 9s after the wielder's Elemental Skill hits an opponent. Elemental Mastery increases by 64 for 30s after the wielder's Elemental Burst hits an opponent."
    ]
    file: str = "smsi"
