from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class ProspectorsShovel(Polearm):
    name: str = "Prospector's Shovel"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Swift and Sure"
    refi_list: list[str] = [
        "Electro-Charged DMG is increased by 48%, and Lunar-Charged DMG is increased by 12%. Moonsign: Ascendant Gleam: Lunar-Charged DMG is increased by an additional 12%.",
        "Electro-Charged DMG is increased by 60%, and Lunar-Charged DMG is increased by 15%. Moonsign: Ascendant Gleam: Lunar-Charged DMG is increased by an additional 15%.",
        "Electro-Charged DMG is increased by 72%, and Lunar-Charged DMG is increased by 18%. Moonsign: Ascendant Gleam: Lunar-Charged DMG is increased by an additional 18%.",
        "Electro-Charged DMG is increased by 84%, and Lunar-Charged DMG is increased by 21%. Moonsign: Ascendant Gleam: Lunar-Charged DMG is increased by an additional 21%.",
        "Electro-Charged DMG is increased by 96%, and Lunar-Charged DMG is increased by 24%. Moonsign: Ascendant Gleam: Lunar-Charged DMG is increased by an additional 24%.",
    ]
    file: str = "ppsv"
