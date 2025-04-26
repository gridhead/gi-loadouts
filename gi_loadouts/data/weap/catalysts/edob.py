from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class EmeraldOrb(Catalyst):
    name: str = "Emerald Orb"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=20.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_3
    refi_name: str = "Rapids"
    refi_list: list[str] = [
        "Upon causing a Vaporize, Electro-Charged, Frozen, Bloom, or a Hydro-infused Swirl reaction, increases ATK by 20% for 12s.",
        "Upon causing a Vaporize, Electro-Charged, Frozen, Bloom, or a Hydro-infused Swirl reaction, increases ATK by 25% for 12s.",
        "Upon causing a Vaporize, Electro-Charged, Frozen, Bloom, or a Hydro-infused Swirl reaction, increases ATK by 30% for 12s.",
        "Upon causing a Vaporize, Electro-Charged, Frozen, Bloom, or a Hydro-infused Swirl reaction, increases ATK by 35% for 12s.",
        "Upon causing a Vaporize, Electro-Charged, Frozen, Bloom, or a Hydro-infused Swirl reaction, increases ATK by 40% for 12s.",
    ]
    file: str = "edob"
