from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FavoniusLance(Polearm):
    name: str = "Favonius Lance"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=6.7)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Windfall"
    refi_list: list[str] = [
        "CRIT Hits have a 60% chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every 12s.",
        "CRIT Hits have a 70% chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every 10.5s.",
        "CRIT Hits have a 80% chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every 9s.",
        "CRIT Hits have a 90% chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every 7.5s.",
        "CRIT Hits have a 100% chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every 6s.",
    ]
    file: str = "fnlc"
