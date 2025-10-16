from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SnareHook(Bow):
    name: str = "Snare Hook"
    seco_stat: WeaponStat = WeaponStat(
        stat_name=WeaponStatType.energy_recharge_perc, stat_data=13.33
    )
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_4
    refi_name: str = "Phantom Flash"
    refi_list: list[str] = [
        "Upon causing an Elemental Reaction, increases Elemental Mastery by 60 for 12s. Moonsign: Ascendant Gleam: Elemental Mastery from this effect is further increased by 60. This effect can be triggered even if the equipping character is off-field.",
        "Upon causing an Elemental Reaction, increases Elemental Mastery by 75 for 12s. Moonsign: Ascendant Gleam: Elemental Mastery from this effect is further increased by 75. This effect can be triggered even if the equipping character is off-field.",
        "Upon causing an Elemental Reaction, increases Elemental Mastery by 90 for 12s. Moonsign: Ascendant Gleam: Elemental Mastery from this effect is further increased by 90. This effect can be triggered even if the equipping character is off-field.",
        "Upon causing an Elemental Reaction, increases Elemental Mastery by 105 for 12s. Moonsign: Ascendant Gleam: Elemental Mastery from this effect is further increased by 105. This effect can be triggered even if the equipping character is off-field.",
        "Upon causing an Elemental Reaction, increases Elemental Mastery by 120 for 12s. Moonsign: Ascendant Gleam: Elemental Mastery from this effect is further increased by 120. This effect can be triggered even if the equipping character is off-field.",
    ]
    file: str = "sehk"
