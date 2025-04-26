from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class AmosBow(Bow):
    name: str = "Amos' Bow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=10.8)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Strong-Willed"
    refi_list: list[str] = [
        "Increases Normal Attack and Charged Attack DMG by 12%. After a Normal or Charged Attack is fired, DMG dealt increases by a further 8% every 0.1 seconds the arrow is in the air for up to 5 times.",
        "Increases Normal Attack and Charged Attack DMG by 15%. After a Normal or Charged Attack is fired, DMG dealt increases by a further 10% every 0.1 seconds the arrow is in the air for up to 5 times.",
        "Increases Normal Attack and Charged Attack DMG by 18%. After a Normal or Charged Attack is fired, DMG dealt increases by a further 12% every 0.1 seconds the arrow is in the air for up to 5 times.",
        "Increases Normal Attack and Charged Attack DMG by 21%. After a Normal or Charged Attack is fired, DMG dealt increases by a further 14% every 0.1 seconds the arrow is in the air for up to 5 times.",
        "Increases Normal Attack and Charged Attack DMG by 24%. After a Normal or Charged Attack is fired, DMG dealt increases by a further 16% every 0.1 seconds the arrow is in the air for up to 5 times.",
    ]
    file: str = "asbw"
