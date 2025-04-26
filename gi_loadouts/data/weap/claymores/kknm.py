from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class KatsuragikiriNagamasa(Claymore):
    name: str = "Katsuragikiri Nagamasa"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=10.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Samurai Conduct"
    refi_list: list[str] = [
        "Increases Elemental Skill DMG by 6%. After Elemental Skill hits an opponent, the character loses 3 Energy but regenerates 3 Energy every 2s for the next 6s. This effect can occur once every 10s. Can be triggered even when the character is not on the field.",
        "Increases Elemental Skill DMG by 7.5%. After Elemental Skill hits an opponent, the character loses 3 Energy but regenerates 3.5 Energy every 2s for the next 6s. This effect can occur once every 10s. Can be triggered even when the character is not on the field.",
        "Increases Elemental Skill DMG by 9%. After Elemental Skill hits an opponent, the character loses 3 Energy but regenerates 4 Energy every 2s for the next 6s. This effect can occur once every 10s. Can be triggered even when the character is not on the field.",
        "Increases Elemental Skill DMG by 10.5%. After Elemental Skill hits an opponent, the character loses 3 Energy but regenerates 4.5 Energy every 2s for the next 6s. This effect can occur once every 10s. Can be triggered even when the character is not on the field.",
        "Increases Elemental Skill DMG by 12%. After Elemental Skill hits an opponent, the character loses 3 Energy but regenerates 5 Energy every 2s for the next 6s. This effect can occur once every 10s. Can be triggered even when the character is not on the field.",
    ]
    file: str = "kknm"
