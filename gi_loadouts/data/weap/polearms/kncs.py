from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class KitainCrossSpear(Polearm):
    name: str = "Kitain Cross Spear"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=24.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Samurai Conduct"
    refi_list: list[str] = [
        "Increases Elemental Skill DMG by 6%. After Elemental Skill hits an opponent, the character loses 3 Energy but regenerates 3 Energy every 2s for the next 6s. This effect can occur once every 10s. Can be triggered even when the character is not on the field.",
        "Increases Elemental Skill DMG by 7.5%. After Elemental Skill hits an opponent, the character loses 3 Energy but regenerates 3.5 Energy every 2s for the next 6s. This effect can occur once every 10s. Can be triggered even when the character is not on the field.",
        "Increases Elemental Skill DMG by 9%. After Elemental Skill hits an opponent, the character loses 3 Energy but regenerates 4 Energy every 2s for the next 6s. This effect can occur once every 10s. Can be triggered even when the character is not on the field.",
        "Increases Elemental Skill DMG by 10.5%. After Elemental Skill hits an opponent, the character loses 3 Energy but regenerates 4.5 Energy every 2s for the next 6s. This effect can occur once every 10s. Can be triggered even when the character is not on the field.",
        "Increases Elemental Skill DMG by 12%. After Elemental Skill hits an opponent, the character loses 3 Energy but regenerates 5 Energy every 2s for the next 6s. This effect can occur once every 10s. Can be triggered even when the character is not on the field.",
    ]
    file: str = "kncs"
