from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Messenger(Bow):
    name: str = "Messenger"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=6.8)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_3
    refi_name: str = "Archer's Message"
    refi_list: list[str] = [
        "Charged Attack hits on weak spots deal an additional 100% ATK DMG as CRIT DMG. Can only occur once every 10s.",
        "Charged Attack hits on weak spots deal an additional 125% ATK DMG as CRIT DMG. Can only occur once every 10s.",
        "Charged Attack hits on weak spots deal an additional 150% ATK DMG as CRIT DMG. Can only occur once every 10s.",
        "Charged Attack hits on weak spots deal an additional 175% ATK DMG as CRIT DMG. Can only occur once every 10s.",
        "Charged Attack hits on weak spots deal an additional 200% ATK DMG as CRIT DMG. Can only occur once every 10s.",
    ]
    file: str = "msgr"
