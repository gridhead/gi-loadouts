from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FavoniusGreatsword(Claymore):
    name: str = "Favonius Greatsword"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=13.3)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Windfall"
    refi_list: list[str] = [
        "CRIT hits have a 60% chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every 12s.",
        "CRIT hits have a 70% chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every 10.5s.",
        "CRIT hits have a 80% chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every 9s.",
        "CRIT hits have a 90% chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every 7.5s.",
        "CRIT hits have a 100% chance to generate a small amount of Elemental Particles, which will regenerate 6 Energy for the character. Can only occur once every 6s.",
    ]
    file: str = "fngs"
