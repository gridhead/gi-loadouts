from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FilletBlade(Sword):
    name: str = "Fillet Blade"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=7.7)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_3
    refi_name: str = "Gash"
    refi_list: list[str] = [
        "On hit, has 50% chance to deal 240% ATK DMG to a single enemy. Can only occur once every 15s.",
        "On hit, has 50% chance to deal 280% ATK DMG to a single enemy. Can only occur once every 14s.",
        "On hit, has 50% chance to deal 320% ATK DMG to a single enemy. Can only occur once every 13s.",
        "On hit, has 50% chance to deal 360% ATK DMG to a single enemy. Can only occur once every 12s.",
        "On hit, has 50% chance to deal 400% ATK DMG to a single enemy. Can only occur once every 11s.",
    ]
    file: str = "flbd"
