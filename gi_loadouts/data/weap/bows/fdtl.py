from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FadingTwilight(Bow):
    name: str = "Fading Twilight"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=6.7)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Radiance of the Deeps"
    refi_list: list[str] = [
        "Has three states, Evengleam, Afterglow, and Dawnblaze, which increase DMG dealt by 6%/10%/14% respectively. When attacks hit opponents, this weapon will switch to the next state. This weapon can change states once every 7s. The character equipping this weapon can still trigger the state switch while not on the field.",
        "Has three states, Evengleam, Afterglow, and Dawnblaze, which increase DMG dealt by 7.5%/12.5%/17.5% respectively. When attacks hit opponents, this weapon will switch to the next state. This weapon can change states once every 7s. The character equipping this weapon can still trigger the state switch while not on the field.",
        "Has three states, Evengleam, Afterglow, and Dawnblaze, which increase DMG dealt by 9%/15%/21% respectively. When attacks hit opponents, this weapon will switch to the next state. This weapon can change states once every 7s. The character equipping this weapon can still trigger the state switch while not on the field.",
        "Has three states, Evengleam, Afterglow, and Dawnblaze, which increase DMG dealt by 10.5%/17.5%/24.5% respectively. When attacks hit opponents, this weapon will switch to the next state. This weapon can change states once every 7s. The character equipping this weapon can still trigger the state switch while not on the field.",
        "Has three states, Evengleam, Afterglow, and Dawnblaze, which increase DMG dealt by 12%/20%/28% respectively. When attacks hit opponents, this weapon will switch to the next state. This weapon can change states once every 7s. The character equipping this weapon can still trigger the state switch while not on the field.",
    ]
    file: str = "fdtl"
