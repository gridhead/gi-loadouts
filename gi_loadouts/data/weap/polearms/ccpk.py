from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class CrescentPike(Polearm):
    name: str = "Crescent Pike"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.damage_bonus_physical_perc, stat_data=7.5)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Infusion Needle"
    refi_list: list[str] = [
        "After picking up an Elemental Orb/Particle, Normal and Charged Attacks deal an additional 20% ATK as DMG for 5s.",
        "After picking up an Elemental Orb/Particle, Normal and Charged Attacks deal an additional 25% ATK as DMG for 5s.",
        "After picking up an Elemental Orb/Particle, Normal and Charged Attacks deal an additional 30% ATK as DMG for 5s.",
        "After picking up an Elemental Orb/Particle, Normal and Charged Attacks deal an additional 35% ATK as DMG for 5s.",
        "After picking up an Elemental Orb/Particle, Normal and Charged Attacks deal an additional 40% ATK as DMG for 5s.",
    ]
    file: str = "ccpk"
