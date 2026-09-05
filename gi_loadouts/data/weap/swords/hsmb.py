from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class HereticsMoltenBlade(Sword):
    name: str = "Heretic's Molten Blade"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Lone Light's Blessing"
    refi_list: list[str] = [
        "After the equipping character uses their Elemental Skill, they gain \"Gleam of First Light.\" While active, Gleam of First Light tracks their distance traveled. Each second, the equipping character gains an ATK Bonus ranging from 18% to 36% based on the distance traveled during the previous second. Gleam of First Light lasts 14s, can be triggered once every 14s, and is removed when the equipping character leaves the field.",
        "After the equipping character uses their Elemental Skill, they gain \"Gleam of First Light.\" While active, Gleam of First Light tracks their distance traveled. Each second, the equipping character gains an ATK Bonus ranging from 22.5% to 45% based on the distance traveled during the previous second. Gleam of First Light lasts 14s, can be triggered once every 14s, and is removed when the equipping character leaves the field.",
        "After the equipping character uses their Elemental Skill, they gain \"Gleam of First Light.\" While active, Gleam of First Light tracks their distance traveled. Each second, the equipping character gains an ATK Bonus ranging from 27% to 54% based on the distance traveled during the previous second. Gleam of First Light lasts 14s, can be triggered once every 14s, and is removed when the equipping character leaves the field.",
        "After the equipping character uses their Elemental Skill, they gain \"Gleam of First Light.\" While active, Gleam of First Light tracks their distance traveled. Each second, the equipping character gains an ATK Bonus ranging from 31.5% to 63% based on the distance traveled during the previous second. Gleam of First Light lasts 14s, can be triggered once every 14s, and is removed when the equipping character leaves the field.",
        "After the equipping character uses their Elemental Skill, they gain \"Gleam of First Light.\" While active, Gleam of First Light tracks their distance traveled. Each second, the equipping character gains an ATK Bonus ranging from 36% to 72% based on the distance traveled during the previous second. Gleam of First Light lasts 14s, can be triggered once every 14s, and is removed when the equipping character leaves the field.",
    ]
    file: str = "hsmb"
