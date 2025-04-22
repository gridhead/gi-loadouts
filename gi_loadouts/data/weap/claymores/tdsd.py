from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TidalShadow(Claymore):
    name: str = "Tidal Shadow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "White Cruising Wave"
    refi_list: list[str] = [
        "After the wielder is healed, ATK will be increased by 24% for 8s. This can be triggered even when the character is not on the field.",
        "After the wielder is healed, ATK will be increased by 30% for 8s. This can be triggered even when the character is not on the field.",
        "After the wielder is healed, ATK will be increased by 36% for 8s. This can be triggered even when the character is not on the field.",
        "After the wielder is healed, ATK will be increased by 42% for 8s. This can be triggered even when the character is not on the field.",
        "After the wielder is healed, ATK will be increased by 48% for 8s. This can be triggered even when the character is not on the field.",
    ]
    file: str = "tdsd"
