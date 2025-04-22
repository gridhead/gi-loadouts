from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Halberd(Polearm):
    name: str = "Halberd"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=5.1)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_3
    refi_name: str = "Heavy"
    refi_list: list[str] = [
        "Normal Attacks deal an additional 160% DMG. Can only occur once every 10s.",
        "Normal Attacks deal an additional 200% DMG. Can only occur once every 10s.",
        "Normal Attacks deal an additional 240% DMG. Can only occur once every 10s.",
        "Normal Attacks deal an additional 280% DMG. Can only occur once every 10s.",
        "Normal Attacks deal an additional 320% DMG. Can only occur once every 10s.",
    ]
    file: str = "hlbd"
