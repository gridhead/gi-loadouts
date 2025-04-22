from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SnowTombedStarsilver(Claymore):
    name: str = "Snow-Tombed Starsilver"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.damage_bonus_physical_perc, stat_data=7.5)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Frost Burial"
    refi_list: list[str] = [
        "Hitting an opponent with Normal and Charged Attacks has a 60% chance of forming and dropping an Everfrost Icicle above them, dealing AoE DMG equal to 80% of ATK. Opponents affected by Cryo are instead dealt DMG equal to 200% of ATK. Can only occur once every 10s.",
        "Hitting an opponent with Normal and Charged Attacks has a 70% chance of forming and dropping an Everfrost Icicle above them, dealing AoE DMG equal to 95% of ATK. Opponents affected by Cryo are instead dealt DMG equal to 240% of ATK. Can only occur once every 10s.",
        "Hitting an opponent with Normal and Charged Attacks has a 80% chance of forming and dropping an Everfrost Icicle above them, dealing AoE DMG equal to 110% of ATK. Opponents affected by Cryo are instead dealt DMG equal to 280% of ATK. Can only occur once every 10s.",
        "Hitting an opponent with Normal and Charged Attacks has a 90% chance of forming and dropping an Everfrost Icicle above them, dealing AoE DMG equal to 125% of ATK. Opponents affected by Cryo are instead dealt DMG equal to 320% of ATK. Can only occur once every 10s.",
        "Hitting an opponent with Normal and Charged Attacks has a 100% chance of forming and dropping an Everfrost Icicle above them, dealing AoE DMG equal to 140% of ATK. Opponents affected by Cryo are instead dealt DMG equal to 360% of ATK. Can only occur once every 10s.",
    ]
    file: str = "stss"
