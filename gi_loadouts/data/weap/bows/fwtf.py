from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FlowerWreathedFeathers(Bow):
    name: str = "Flower-Wreathed Feathers"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Inflorescence Unattainable"
    refi_list: list[str] = [
        "Decreases Gliding Stamina consumption by 15%. When using Aimed Shots, the DMG dealt by Charged Attacks increases by 6% every 0.5s. This effect can stack up to 6 times and will be removed 10s after leaving Aiming Mode.",
        "Decreases Gliding Stamina consumption by 15%. When using Aimed Shots, the DMG dealt by Charged Attacks increases by 7.5% every 0.5s. This effect can stack up to 6 times and will be removed 10s after leaving Aiming Mode.",
        "Decreases Gliding Stamina consumption by 15%. When using Aimed Shots, the DMG dealt by Charged Attacks increases by 9% every 0.5s. This effect can stack up to 6 times and will be removed 10s after leaving Aiming Mode.",
        "Decreases Gliding Stamina consumption by 15%. When using Aimed Shots, the DMG dealt by Charged Attacks increases by 10.5% every 0.5s. This effect can stack up to 6 times and will be removed 10s after leaving Aiming Mode.",
        "Decreases Gliding Stamina consumption by 15%. When using Aimed Shots, the DMG dealt by Charged Attacks increases by 12% every 0.5s. This effect can stack up to 6 times and will be removed 10s after leaving Aiming Mode.",
    ]
    file: str = "fwtf"
