from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class BlackmarrowLantern(Catalyst):
    name: str = "Blackmarrow Lantern"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=48.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Token of Covenant"
    refi_list: list[str] = [
        "Bloom DMG is increased by 48%, and Lunar-Bloom DMG is increased by 12%. Moonsign: Ascendant Gleam: Lunar-Bloom DMG is increased by an additional 12%.",
        "Bloom DMG is increased by 60%, and Lunar-Bloom DMG is increased by 15%. Moonsign: Ascendant Gleam: Lunar-Bloom DMG is increased by an additional 15%.",
        "Bloom DMG is increased by 72%, and Lunar-Bloom DMG is increased by 18%. Moonsign: Ascendant Gleam: Lunar-Bloom DMG is increased by an additional 18%.",
        "Bloom DMG is increased by 84%, and Lunar-Bloom DMG is increased by 21%. Moonsign: Ascendant Gleam: Lunar-Bloom DMG is increased by an additional 21%.",
        "Bloom DMG is increased by 96%, and Lunar-Bloom DMG is increased by 24%. Moonsign: Ascendant Gleam: Lunar-Bloom DMG is increased by an additional 24%.",
    ]
    file: str = "bmln"
