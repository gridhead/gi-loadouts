from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class BeaconOfTheReedSea(Claymore):
    name: str = "Beacon of the Reed Sea"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=7.2)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Desert Watch"
    refi_list: list[str] = [
        "After the character's Elemental Skill hits an opponent, their ATK will be increased by 20% for 8s. After the character takes DMG, their ATK will be increased by 20% for 8s. The 2 aforementioned effects can be triggered even when the character is not on the field. Additionally, when not protected by a shield, the character's Max HP will be increased by 32%.",
        "After the character's Elemental Skill hits an opponent, their ATK will be increased by 25% for 8s. After the character takes DMG, their ATK will be increased by 25% for 8s. The 2 aforementioned effects can be triggered even when the character is not on the field. Additionally, when not protected by a shield, the character's Max HP will be increased by 40%.",
        "After the character's Elemental Skill hits an opponent, their ATK will be increased by 30% for 8s. After the character takes DMG, their ATK will be increased by 30% for 8s. The 2 aforementioned effects can be triggered even when the character is not on the field. Additionally, when not protected by a shield, the character's Max HP will be increased by 48%.",
        "After the character's Elemental Skill hits an opponent, their ATK will be increased by 35% for 8s. After the character takes DMG, their ATK will be increased by 35% for 8s. The 2 aforementioned effects can be triggered even when the character is not on the field. Additionally, when not protected by a shield, the character's Max HP will be increased by 56%.",
        "After the character's Elemental Skill hits an opponent, their ATK will be increased by 40% for 8s. After the character takes DMG, their ATK will be increased by 40% for 8s. The 2 aforementioned effects can be triggered even when the character is not on the field. Additionally, when not protected by a shield, the character's Max HP will be increased by 64%.",
    ]
    file: str = "bors"
