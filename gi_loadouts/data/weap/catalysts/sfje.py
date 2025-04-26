from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SacrificialJade(Catalyst):
    name: str = "Sacrificial Jade"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=8.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Jade Circulation"
    refi_list: list[str] = [
        "When not on the field for more than 5s, Max HP will be increased by 32% and Elemental Mastery will be increased by 40. These effects will be canceled after the wielder has been on the field for 10s.",
        "When not on the field for more than 5s, Max HP will be increased by 40% and Elemental Mastery will be increased by 50. These effects will be canceled after the wielder has been on the field for 10s.",
        "When not on the field for more than 5s, Max HP will be increased by 48% and Elemental Mastery will be increased by 60. These effects will be canceled after the wielder has been on the field for 10s.",
        "When not on the field for more than 5s, Max HP will be increased by 56% and Elemental Mastery will be increased by 70. These effects will be canceled after the wielder has been on the field for 10s.",
        "When not on the field for more than 5s, Max HP will be increased by 64% and Elemental Mastery will be increased by 80. These effects will be canceled after the wielder has been on the field for 10s.",
    ]
    file: str = "sfje"
