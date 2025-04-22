from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class RightfulReward(Polearm):
    name: str = "Rightful Reward"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Tip of the Spear"
    refi_list: list[str] = [
        "When the wielder is healed, restore 8 Energy. This effect can triggered once every 10s, and can occur even when the character is not on the field.",
        "When the wielder is healed, restore 10 Energy. This effect can triggered once every 10s, and can occur even when the character is not on the field.",
        "When the wielder is healed, restore 12 Energy. This effect can triggered once every 10s, and can occur even when the character is not on the field.",
        "When the wielder is healed, restore 14 Energy. This effect can triggered once every 10s, and can occur even when the character is not on the field.",
        "When the wielder is healed, restore 16 Energy. This effect can triggered once every 10s, and can occur even when the character is not on the field.",
    ]
    file: str = "rtrw"
