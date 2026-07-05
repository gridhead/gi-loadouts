from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class ATeaspoonOfTranscendence(Claymore):
    name: str = "A Teaspoon of Transcendence"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=9.6)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "White Fairy's Queening"
    refi_list: list[str] = [
        'ATK increased by 28%. Additionally, each time the equipping character hits an opponent with their Charged Attack, they attain "Surmount" for a short time: their Stellar-Conduct DMG is increased by 16% for 5s. This effect can stack once every 0.2s, max 3 stacks.',
        'ATK increased by 35%. Additionally, each time the equipping character hits an opponent with their Charged Attack, they attain "Surmount" for a short time: their Stellar-Conduct DMG is increased by 20% for 5s. This effect can stack once every 0.2s, max 3 stacks.',
        'ATK increased by 42%. Additionally, each time the equipping character hits an opponent with their Charged Attack, they attain "Surmount" for a short time: their Stellar-Conduct DMG is increased by 24% for 5s. This effect can stack once every 0.2s, max 3 stacks.',
        'ATK increased by 49%. Additionally, each time the equipping character hits an opponent with their Charged Attack, they attain "Surmount" for a short time: their Stellar-Conduct DMG is increased by 28% for 5s. This effect can stack once every 0.2s, max 3 stacks.',
        'ATK increased by 56%. Additionally, each time the equipping character hits an opponent with their Charged Attack, they attain "Surmount" for a short time: their Stellar-Conduct DMG is increased by 32% for 5s. This effect can stack once every 0.2s, max 3 stacks.',
    ]
    refi_stat: list[list[WeaponStat]] = [
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=28.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=35.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=42.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=49.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=56.0)],
    ]
    file: str = "atot"
