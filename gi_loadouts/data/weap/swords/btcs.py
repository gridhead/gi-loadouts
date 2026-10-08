from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class BeyondTheChrysalis(Sword):
    name: str = "Beyond the Chrysalis"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=9.6)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "Dance of Wings Unbound"
    refi_list: list[str] = [
        "Each time the equipping character uses their Elemental Skill or Elemental Burst, they gain one of the following three effects in sequence:\nWinds of Devotion: Increases the equipping character's CRIT DMG by 56% for 10s;\nWinds of Defiance: Increases Stellar Swirl reaction DMG dealt by the equipping character by 36% for 10s; and\nWinds of Plenty: Regenerates 5 Elemental Energy for the equipping character. Up to 5 Elemental Energy can be regenerated in this way every 4s.\nThe aforementioned effects are removed and the sequence is reset when the equipping character leaves the field.",
        "Each time the equipping character uses their Elemental Skill or Elemental Burst, they gain one of the following three effects in sequence:\nWinds of Devotion: Increases the equipping character's CRIT DMG by 72% for 10s;\nWinds of Defiance: Increases Stellar Swirl reaction DMG dealt by the equipping character by 45% for 10s; and\nWinds of Plenty: Regenerates 5.5 Elemental Energy for the equipping character. Up to 5.5 Elemental Energy can be regenerated in this way every 4s.\nThe aforementioned effects are removed and the sequence is reset when the equipping character leaves the field.",
        "Each time the equipping character uses their Elemental Skill or Elemental Burst, they gain one of the following three effects in sequence:\nWinds of Devotion: Increases the equipping character's CRIT DMG by 88% for 10s;\nWinds of Defiance: Increases Stellar Swirl reaction DMG dealt by the equipping character by 54% for 10s; and\nWinds of Plenty: Regenerates 6 Elemental Energy for the equipping character. Up to 6 Elemental Energy can be regenerated in this way every 4s.\nThe aforementioned effects are removed and the sequence is reset when the equipping character leaves the field.",
        "Each time the equipping character uses their Elemental Skill or Elemental Burst, they gain one of the following three effects in sequence:\nWinds of Devotion: Increases the equipping character's CRIT DMG by 104% for 10s;\nWinds of Defiance: Increases Stellar Swirl reaction DMG dealt by the equipping character by 63% for 10s; and\nWinds of Plenty: Regenerates 6.5 Elemental Energy for the equipping character. Up to 6.5 Elemental Energy can be regenerated in this way every 4s.\nThe aforementioned effects are removed and the sequence is reset when the equipping character leaves the field.",
        "Each time the equipping character uses their Elemental Skill or Elemental Burst, they gain one of the following three effects in sequence:\nWinds of Devotion: Increases the equipping character's CRIT DMG by 120% for 10s;\nWinds of Defiance: Increases Stellar Swirl reaction DMG dealt by the equipping character by 72% for 10s; and\nWinds of Plenty: Regenerates 7 Elemental Energy for the equipping character. Up to 7 Elemental Energy can be regenerated in this way every 4s.\nThe aforementioned effects are removed and the sequence is reset when the equipping character leaves the field.",
    ]
    file: str = "btcs"
