from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Catalyst, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.tier import Tier


class MappaMare(Catalyst):
    name: str = "Mappa Mare"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=24.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Infusion Scroll"
    refi_list: list[str] = [
        "Triggering an Elemental reaction grants a 8% Elemental DMG Bonus for 10s. Max 2 stacks.",
        "Triggering an Elemental reaction grants a 10% Elemental DMG Bonus for 10s. Max 2 stacks.",
        "Triggering an Elemental reaction grants a 12% Elemental DMG Bonus for 10s. Max 2 stacks.",
        "Triggering an Elemental reaction grants a 14% Elemental DMG Bonus for 10s. Max 2 stacks.",
        "Triggering an Elemental reaction grants a 16% Elemental DMG Bonus for 10s. Max 2 stacks.",
    ]
    file: str = "mama"
