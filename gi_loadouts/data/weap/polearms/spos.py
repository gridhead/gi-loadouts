from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SymphonistofScents(Polearm):
    name: str = "Symphonist of Scents"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=14.4)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Seasoned Symphony"
    refi_list: list[str] = [
        "ATK is increased by 12%. When the equipping character is off-field, ATK is increased by an additional 12%. After initiating healing, the equipping character and the character(s) they have healed will obtain the \"Sweet Echoes\" effect, increasing their ATK by 32% for 3s. This effect can be triggered even if the equipping character is off-field.",
        "ATK is increased by 15%. When the equipping character is off-field, ATK is increased by an additional 15%. After initiating healing, the equipping character and the character(s) they have healed will obtain the \"Sweet Echoes\" effect, increasing their ATK by 40% for 3s. This effect can be triggered even if the equipping character is off-field.",
        "ATK is increased by 18%. When the equipping character is off-field, ATK is increased by an additional 18%. After initiating healing, the equipping character and the character(s) they have healed will obtain the \"Sweet Echoes\" effect, increasing their ATK by 40% for 3s. This effect can be triggered even if the equipping character is off-field.",
        "ATK is increased by 21%. When the equipping character is off-field, ATK is increased by an additional 21%. After initiating healing, the equipping character and the character(s) they have healed will obtain the \"Sweet Echoes\" effect, increasing their ATK by 56% for 3s. This effect can be triggered even if the equipping character is off-field.",
        "ATK is increased by 24%. When the equipping character is off-field, ATK is increased by an additional 24%. After initiating healing, the equipping character and the character(s) they have healed will obtain the \"Sweet Echoes\" effect, increasing their ATK by 64% for 3s. This effect can be triggered even if the equipping character is off-field.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=12.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=15.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=18.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=21.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=24.0)],
    ]
    file: str = "spos"
