from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class DialoguesoftheDesertSages(Polearm):
    name: str = "Dialogues of the Desert Sages"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Principle of Equilibrium"
    refi_list: list[str] = [
        "When the wielder performs healing, restore 8 Energy. This effect can be triggered once every 10s and can occur even when the character is not on the field.",
        "When the wielder performs healing, restore 10 Energy. This effect can be triggered once every 10s and can occur even when the character is not on the field.",
        "When the wielder performs healing, restore 12 Energy. This effect can be triggered once every 10s and can occur even when the character is not on the field.",
        "When the wielder performs healing, restore 14 Energy. This effect can be triggered once every 10s and can occur even when the character is not on the field.",
        "When the wielder performs healing, restore 16 Energy. This effect can be triggered once every 10s and can occur even when the character is not on the field.",
    ]
    file: str = "dtds"
