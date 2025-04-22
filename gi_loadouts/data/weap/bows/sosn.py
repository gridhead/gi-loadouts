from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SongofStillness(Bow):
    name: str = "Song of Stillness"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Benthic Pulse"
    refi_list: list[str] = [
            "After the wielder is healed, they will deal 16% more DMG for 8s. This can be triggered even when the character is not on the field.",
            "After the wielder is healed, they will deal 20% more DMG for 8s. This can be triggered even when the character is not on the field.",
            "After the wielder is healed, they will deal 24% more DMG for 8s. This can be triggered even when the character is not on the field.",
            "After the wielder is healed, they will deal 28% more DMG for 8s. This can be triggered even when the character is not on the field.",
            "After the wielder is healed, they will deal 32% more DMG for 8s. This can be triggered even when the character is not on the field.",
        ]
    file: str = "sosn"
