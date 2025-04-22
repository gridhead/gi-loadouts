from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class JadefallsSplendor(Catalyst):
    name: str = "Jadefall's Splendor"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=10.8)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Primordial Jade Regalia"
    refi_list: list[str] = [
        "For 3s after using an Elemental Burst or creating a shield, the equipping character can gain the Primordial Jade Regalia effect: Restore 4.5 Energy every 2.5s, and gain 0.3% Elemental DMG Bonus for their corresponding Elemental Type for every 1,000 Max HP they possess, up to 12%. Primordial Jade Regalia will still take effect even if the equipping character is not on the field.",
        "For 3s after using an Elemental Burst or creating a shield, the equipping character can gain the Primordial Jade Regalia effect: Restore 5 Energy every 2.5s, and gain 0.5% Elemental DMG Bonus for their corresponding Elemental Type for every 1,000 Max HP they possess, up to 20%. Primordial Jade Regalia will still take effect even if the equipping character is not on the field.",
        "For 3s after using an Elemental Burst or creating a shield, the equipping character can gain the Primordial Jade Regalia effect: Restore 5.5 Energy every 2.5s, and gain 0.7% Elemental DMG Bonus for their corresponding Elemental Type for every 1,000 Max HP they possess, up to 28%. Primordial Jade Regalia will still take effect even if the equipping character is not on the field.",
        "For 3s after using an Elemental Burst or creating a shield, the equipping character can gain the Primordial Jade Regalia effect: Restore 6 Energy every 2.5s, and gain 0.9% Elemental DMG Bonus for their corresponding Elemental Type for every 1,000 Max HP they possess, up to 36%. Primordial Jade Regalia will still take effect even if the equipping character is not on the field.",
        "For 3s after using an Elemental Burst or creating a shield, the equipping character can gain the Primordial Jade Regalia effect: Restore 6.5 Energy every 2.5s, and gain 1.1% Elemental DMG Bonus for their corresponding Elemental Type for every 1,000 Max HP they possess, up to 44%. Primordial Jade Regalia will still take effect even if the equipping character is not on the field.",
    ]
    file: str = "jfsd"
