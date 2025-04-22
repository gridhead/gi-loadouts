from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class AlleyHunter(Bow):
    name: str = "Alley Hunter"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Oppidan Ambush"
    refi_list: list[str] = [
        "While the character equipped with this weapon is in the party but not on the field, their DMG increases by 2% every second up to a max of 20%. When the character is on the field for more than 4s, the aforementioned DMG buff decreases by 4% per second until it reaches 0%.",
        "While the character equipped with this weapon is in the party but not on the field, their DMG increases by 2.5% every second up to a max of 25%. When the character is on the field for more than 4s, the aforementioned DMG buff decreases by 5% per second until it reaches 0%.",
        "While the character equipped with this weapon is in the party but not on the field, their DMG increases by 3% every second up to a max of 30%. When the character is on the field for more than 4s, the aforementioned DMG buff decreases by 6% per second until it reaches 0%.",
        "While the character equipped with this weapon is in the party but not on the field, their DMG increases by 3.5% every second up to a max of 35%. When the character is on the field for more than 4s, the aforementioned DMG buff decreases by 7% per second until it reaches 0%.",
        "While the character equipped with this weapon is in the party but not on the field, their DMG increases by 4% every second up to a max of 40%. When the character is on the field for more than 4s, the aforementioned DMG buff decreases by 8% per second until it reaches 0%.",
    ]
    file: str = "ayht"
