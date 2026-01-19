from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class NocturnesCurtainCall(Catalyst):
    name: str = "Nocturne's Curtain Call"
    seco_stat: WeaponStat = WeaponStat(
        stat_name=WeaponStatType.critical_damage_perc, stat_data=19.2
    )
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Ballad of the Crossroads"
    refi_list: list[str] = [
        "Max HP increases by 10%. When triggering Lunar reactions or inflicting Lunar Reaction DMG on opponents, the equipping character will recover 14 Energy, and receive the Bountiful Sea's Sacred Wine effect for 12s: Max HP increases by an additional 14%, CRIT DMG from Lunar Reaction DMG increases by 60%. The Energy recovery effect can be triggered at most once every 18s, and can be triggered even when the equipping character is off-field.",
        "Max HP increases by 12%. When triggering Lunar reactions or inflicting Lunar Reaction DMG on opponents, the equipping character will recover 15 Energy, and receive the Bountiful Sea's Sacred Wine effect for 12s: Max HP increases by an additional 16%, CRIT DMG from Lunar Reaction DMG increases by 80%. The Energy recovery effect can be triggered at most once every 18s, and can be triggered even when the equipping character is off-field.",
        "Max HP increases by 14%. When triggering Lunar reactions or inflicting Lunar Reaction DMG on opponents, the equipping character will recover 16 Energy, and receive the Bountiful Sea's Sacred Wine effect for 12s: Max HP increases by an additional 18%, CRIT DMG from Lunar Reaction DMG increases by 100%. The Energy recovery effect can be triggered at most once every 18s, and can be triggered even when the equipping character is off-field.",
        "Max HP increases by 16%. When triggering Lunar reactions or inflicting Lunar Reaction DMG on opponents, the equipping character will recover 17 Energy, and receive the Bountiful Sea's Sacred Wine effect for 12s: Max HP increases by an additional 20%, CRIT DMG from Lunar Reaction DMG increases by 120%. The Energy recovery effect can be triggered at most once every 18s, and can be triggered even when the equipping character is off-field.",
        "Max HP increases by 18%. When triggering Lunar reactions or inflicting Lunar Reaction DMG on opponents, the equipping character will recover 18 Energy, and receive the Bountiful Sea's Sacred Wine effect for 12s: Max HP increases by an additional 22%, CRIT DMG from Lunar Reaction DMG increases by 140%. The Energy recovery effect can be triggered at most once every 18s, and can be triggered even when the equipping character is off-field.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=10.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=12.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=14.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=16.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=18.0)],
    ]
    file: str = "nucc"
