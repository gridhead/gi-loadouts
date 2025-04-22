from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class WavebreakersFin(Polearm):
    name: str = "Wavebreaker's Fin"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=3.0)
    tier: Tier = Tier.Tier_4
    rare: Rare = Rare.Star_4
    refi_name: str = "Watatsumi Wavewalker"
    refi_list: list[str] = [
        "For every point of the entire party's combined maximum Energy capacity, the Elemental Burst DMG of the character equipping this weapon is increased by 0.12%. A maximum of 40% increased Elemental Burst DMG can be achieved this way.",
        "For every point of the entire party's combined maximum Energy capacity, the Elemental Burst DMG of the character equipping this weapon is increased by 0.15%. A maximum of 50% increased Elemental Burst DMG can be achieved this way.",
        "For every point of the entire party's combined maximum Energy capacity, the Elemental Burst DMG of the character equipping this weapon is increased by 0.18%. A maximum of 60% increased Elemental Burst DMG can be achieved this way.",
        "For every point of the entire party's combined maximum Energy capacity, the Elemental Burst DMG of the character equipping this weapon is increased by 0.21%. A maximum of 70% increased Elemental Burst DMG can be achieved this way.",
        "For every point of the entire party's combined maximum Energy capacity, the Elemental Burst DMG of the character equipping this weapon is increased by 0.24%. A maximum of 80% increased Elemental Burst DMG can be achieved this way.",
    ]
    file: str = "wbfn"
