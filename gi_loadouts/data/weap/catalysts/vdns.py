from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class VividNotions(Catalyst):
    name: str = "Vivid Notions"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=9.6)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "Falling Rainbow's Wish"
    refi_list: list[str] = [
        "ATK is increased by 28%. When you use a Plunging Attack, you will gain the \"Dawn's First Hue\" effect: Plunging Attack CRIT DMG is increased by 28%. When you use an Elemental Skill or Burst, you will gain the \"Twilight's Splendor\" effect: Plunging Attack CRIT DMG is increased by 40%. The two effects above each last for 15s, and will be canceled 0.1s after the ground impact hits a target.",
        "ATK is increased by 35%. When you use a Plunging Attack, you will gain the \"Dawn's First Hue\" effect: Plunging Attack CRIT DMG is increased by 35%. When you use an Elemental Skill or Burst, you will gain the \"Twilight's Splendor\" effect: Plunging Attack CRIT DMG is increased by 50%. The two effects above each last for 15s, and will be canceled 0.1s after the ground impact hits a target.",
        "ATK is increased by 42%. When you use a Plunging Attack, you will gain the \"Dawn's First Hue\" effect: Plunging Attack CRIT DMG is increased by 42%. When you use an Elemental Skill or Burst, you will gain the \"Twilight's Splendor\" effect: Plunging Attack CRIT DMG is increased by 60%. The two effects above each last for 15s, and will be canceled 0.1s after the ground impact hits a target.",
        "ATK is increased by 49%. When you use a Plunging Attack, you will gain the \"Dawn's First Hue\" effect: Plunging Attack CRIT DMG is increased by 49%. When you use an Elemental Skill or Burst, you will gain the \"Twilight's Splendor\" effect: Plunging Attack CRIT DMG is increased by 70%. The two effects above each last for 15s, and will be canceled 0.1s after the ground impact hits a target.",
        "ATK is increased by 56%. When you use a Plunging Attack, you will gain the \"Dawn's First Hue\" effect: Plunging Attack CRIT DMG is increased by 56%. When you use an Elemental Skill or Burst, you will gain the \"Twilight's Splendor\" effect: Plunging Attack CRIT DMG is increased by 80%. The two effects above each last for 15s, and will be canceled 0.1s after the ground impact hits a target."
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=28.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=35.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=42.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=49.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=56.0)],
    ]
    file: str = "vdns"
