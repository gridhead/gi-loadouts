from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TheWidsith(Catalyst):
    name: str = "The Widsith"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=12.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Debut"
    refi_list: list[str] = [
        "When a character takes the field, they will gain a random theme song for 10s. This can only occur once every 30s. Recitative: ATK is increased by 60%. Aria: Increases all Elemental DMG by 48%. Interlude: Elemental Mastery is increased by 240.",
        "When a character takes the field, they will gain a random theme song for 10s. This can only occur once every 30s. Recitative: ATK is increased by 75%. Aria: Increases all Elemental DMG by 60%. Interlude: Elemental Mastery is increased by 300.",
        "When a character takes the field, they will gain a random theme song for 10s. This can only occur once every 30s. Recitative: ATK is increased by 90%. Aria: Increases all Elemental DMG by 72%. Interlude: Elemental Mastery is increased by 360.",
        "When a character takes the field, they will gain a random theme song for 10s. This can only occur once every 30s. Recitative: ATK is increased by 105%. Aria: Increases all Elemental DMG by 84%. Interlude: Elemental Mastery is increased by 420.",
        "When a character takes the field, they will gain a random theme song for 10s. This can only occur once every 30s. Recitative: ATK is increased by 120%. Aria: Increases all Elemental DMG by 96%. Interlude: Elemental Mastery is increased by 480.",
    ]
    file: str = "twsh"
