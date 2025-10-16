from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SerenitysCall(Sword):
    name: str = "Serenity's Call"
    seco_stat: WeaponStat = WeaponStat(
        stat_name=WeaponStatType.energy_recharge_perc, stat_data=13.33
    )
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Solemn Silence"
    refi_list: list[str] = [
        "Upon causing an Elemental Reaction, increases Max HP by 16% for 12s. Moonsign: Ascendant Gleam: Max HP from this effect is further increased by 16%. This effect can be triggered even if the equipping character is off-field.",
        "Upon causing an Elemental Reaction, increases Max HP by 20% for 12s. Moonsign: Ascendant Gleam: Max HP from this effect is further increased by 20%. This effect can be triggered even if the equipping character is off-field.",
        "Upon causing an Elemental Reaction, increases Max HP by 24% for 12s. Moonsign: Ascendant Gleam: Max HP from this effect is further increased by 24%. This effect can be triggered even if the equipping character is off-field.",
        "Upon causing an Elemental Reaction, increases Max HP by 28% for 12s. Moonsign: Ascendant Gleam: Max HP from this effect is further increased by 28%. This effect can be triggered even if the equipping character is off-field.",
        "Upon causing an Elemental Reaction, increases Max HP by 32% for 12s. Moonsign: Ascendant Gleam: Max HP from this effect is further increased by 32%. This effect can be triggered even if the equipping character is off-field.",
    ]
    file: str = "sncl"
