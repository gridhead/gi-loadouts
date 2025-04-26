from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier

# Please consider the completion of the world quest for an increase in attack statistics.

class UltimateOverlordsMegaMagicSword(Claymore):
    name: str = "\"Ultimate Overlord's Mega Magic Sword\""
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=6.7)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Melussistance!"
    refi_list: list[str] = [
        "ATK increased by 12%. That's not all! The support from all Melusines you've helped in Merusea Village fills you with strength! Based on the number of them you've helped, your ATK is increased by up to an additional 12%.",
        "ATK increased by 15%. That's not all! The support from all Melusines you've helped in Merusea Village fills you with strength! Based on the number of them you've helped, your ATK is increased by up to an additional 15%.",
        "ATK increased by 18%. That's not all! The support from all Melusines you've helped in Merusea Village fills you with strength! Based on the number of them you've helped, your ATK is increased by up to an additional 18%.",
        "ATK increased by 21%. That's not all! The support from all Melusines you've helped in Merusea Village fills you with strength! Based on the number of them you've helped, your ATK is increased by up to an additional 21%.",
        "ATK increased by 24%. That's not all! The support from all Melusines you've helped in Merusea Village fills you with strength! Based on the number of them you've helped, your ATK is increased by up to an additional 24%.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=12.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=15.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=18.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=21.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=24.0)],
    ]
    file: str = "uoms"

