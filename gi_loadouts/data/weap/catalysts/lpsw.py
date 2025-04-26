from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class LostPrayertotheSacredWinds(Catalyst):
    name: str = "Lost Prayer to the Sacred Winds"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=7.2)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Boundless Blessing"
    refi_list: list[str] = [
        "Increases Movement SPD by 10%. When in battle, gain an 8% Elemental DMG Bonus every 4s. Max 4 stacks. Lasts until the character falls or leaves combat.",
        "Increases Movement SPD by 10%. When in battle, gain an 10% Elemental DMG Bonus every 4s. Max 4 stacks. Lasts until the character falls or leaves combat.",
        "Increases Movement SPD by 10%. When in battle, gain an 12% Elemental DMG Bonus every 4s. Max 4 stacks. Lasts until the character falls or leaves combat.",
        "Increases Movement SPD by 10%. When in battle, gain an 14% Elemental DMG Bonus every 4s. Max 4 stacks. Lasts until the character falls or leaves combat.",
        "Increases Movement SPD by 10%. When in battle, gain an 16% Elemental DMG Bonus every 4s. Max 4 stacks. Lasts until the character falls or leaves combat.",
    ]
    file: str = "lpsw"
