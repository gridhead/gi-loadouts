from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class KingsSquire(Bow):
    name: str = "King's Squire"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=12.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Labyrinth Lord's Instruction"
    refi_list: list[str] = [
        "Obtain the Teachings of the Forest effect when unleashing Elemental Skills and Elemental Burst, increasing Elemental Mastery by 60 for 12s. This effect will be removed when switching characters. When the Teachings of the Forest effect ends or is removed, it will deal 100% of ATK as DMG to 1 nearby opponent. The Teachings of the Forest effect can be triggered once every 20s.",
        "Obtain the Teachings of the Forest effect when unleashing Elemental Skills and Elemental Burst, increasing Elemental Mastery by 80 for 12s. This effect will be removed when switching characters. When the Teachings of the Forest effect ends or is removed, it will deal 120% of ATK as DMG to 1 nearby opponent. The Teachings of the Forest effect can be triggered once every 20s.",
        "Obtain the Teachings of the Forest effect when unleashing Elemental Skills and Elemental Burst, increasing Elemental Mastery by 100 for 12s. This effect will be removed when switching characters. When the Teachings of the Forest effect ends or is removed, it will deal 140% of ATK as DMG to 1 nearby opponent. The Teachings of the Forest effect can be triggered once every 20s.",
        "Obtain the Teachings of the Forest effect when unleashing Elemental Skills and Elemental Burst, increasing Elemental Mastery by 120 for 12s. This effect will be removed when switching characters. When the Teachings of the Forest effect ends or is removed, it will deal 160% of ATK as DMG to 1 nearby opponent. The Teachings of the Forest effect can be triggered once every 20s.",
        "Obtain the Teachings of the Forest effect when unleashing Elemental Skills and Elemental Burst, increasing Elemental Mastery by 140 for 12s. This effect will be removed when switching characters. When the Teachings of the Forest effect ends or is removed, it will deal 180% of ATK as DMG to 1 nearby opponent. The Teachings of the Forest effect can be triggered once every 20s.",
    ]
    file: str = "kgsr"
