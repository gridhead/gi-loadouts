from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class BloodsoakedRuins(Polearm):
    name: str = "Bloodsoaked Ruins"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=4.8)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "Mournful Tribute"
    refi_list: list[str] = [
        "For 3.5s after using an Elemental Burst, the equipping character's Lunar-Charged DMG dealt to opponents is increased by 36%. After triggering a Lunar-Charged reaction, CRIT DMG increases by 28% for 6s. Regains 12 Elemental Energy (once every 14s).",
        "For 3.5s after using an Elemental Burst, the equipping character's Lunar-Charged DMG dealt to opponents is increased by 45%. After triggering a Lunar-Charged reaction, CRIT DMG increases by 35% for 6s. Regains 15 Elemental Energy (once every 14s).",
        "For 3.5s after using an Elemental Burst, the equipping character's Lunar-Charged DMG dealt to opponents is increased by 54%. After triggering a Lunar-Charged reaction, CRIT DMG increases by 42% for 6s. Regains 18 Elemental Energy (once every 14s).",
        "For 3.5s after using an Elemental Burst, the equipping character's Lunar-Charged DMG dealt to opponents is increased by 63%. After triggering a Lunar-Charged reaction, CRIT DMG increases by 49% for 6s. Regains 21 Elemental Energy (once every 14s).",
        "For 3.5s after using an Elemental Burst, the equipping character's Lunar-Charged DMG dealt to opponents is increased by 72%. After triggering a Lunar-Charged reaction, CRIT DMG increases by 56% for 6s. Regains 24 Elemental Energy (once every 14s).",
    ]
    file: str = "bsrs"
