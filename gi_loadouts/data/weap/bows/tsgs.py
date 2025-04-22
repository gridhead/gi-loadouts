from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TheStringless(Bow):
    name: str = "The Stringless"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=36.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Arrowless Song"
    refi_list: list[str] = [
            "Increases Elemental Skill and Elemental Burst DMG by 24%.",
            "Increases Elemental Skill and Elemental Burst DMG by 30%.",
            "Increases Elemental Skill and Elemental Burst DMG by 36%.",
            "Increases Elemental Skill and Elemental Burst DMG by 42%.",
            "Increases Elemental Skill and Elemental Burst DMG by 48%.",
        ]
    file: str = "tsgs"
