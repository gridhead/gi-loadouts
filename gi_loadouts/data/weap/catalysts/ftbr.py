from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Frostbearer(Catalyst):
    name: str = "Frostbearer"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=9.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Frost Burial"
    refi_list: list[str] = [
        "Hitting an opponent with Normal and Charged Attacks has a 60% chance of forming and dropping an Everfrost Icicle above them, dealing 80% AoE ATK DMG. Opponents affected by Cryo are dealt 200% ATK DMG instead by the icicle. Can only occur once every 10s.",
        "Hitting an opponent with Normal and Charged Attacks has a 70% chance of forming and dropping an Everfrost Icicle above them, dealing 95% AoE ATK DMG. Opponents affected by Cryo are dealt 240% ATK DMG instead by the icicle. Can only occur once every 10s.",
        "Hitting an opponent with Normal and Charged Attacks has a 80% chance of forming and dropping an Everfrost Icicle above them, dealing 110% AoE ATK DMG. Opponents affected by Cryo are dealt 280% ATK DMG instead by the icicle. Can only occur once every 10s.",
        "Hitting an opponent with Normal and Charged Attacks has a 90% chance of forming and dropping an Everfrost Icicle above them, dealing 125% AoE ATK DMG. Opponents affected by Cryo are dealt 320% ATK DMG instead by the icicle. Can only occur once every 10s.",
        "Hitting an opponent with Normal and Charged Attacks has a 100% chance of forming and dropping an Everfrost Icicle above them, dealing 140% AoE ATK DMG. Opponents affected by Cryo are dealt 360% ATK DMG instead by the icicle. Can only occur once every 10s.",
    ]
    file: str = "ftbr"
