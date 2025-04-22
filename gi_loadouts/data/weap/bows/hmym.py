from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Hamayumi(Bow):
    name: str = "Hamayumi"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=12.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Full Draw"
    refi_list: list[str] = [
        "Increases Normal Attack DMG by 16% and Charged Attack DMG by 12%. When the equipping character's Energy reaches 100%, this effect is increased by 100%.",
        "Increases Normal Attack DMG by 20% and Charged Attack DMG by 15%. When the equipping character's Energy reaches 100%, this effect is increased by 100%.",
        "Increases Normal Attack DMG by 24% and Charged Attack DMG by 18%. When the equipping character's Energy reaches 100%, this effect is increased by 100%.",
        "Increases Normal Attack DMG by 28% and Charged Attack DMG by 21%. When the equipping character's Energy reaches 100%, this effect is increased by 100%.",
        "Increases Normal Attack DMG by 32% and Charged Attack DMG by 24%. When the equipping character's Energy reaches 100%, this effect is increased by 100%.",
    ]
    file: str = "hmym"
