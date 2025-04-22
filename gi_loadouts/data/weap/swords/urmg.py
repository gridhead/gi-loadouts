from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class UrakuMisugiri(Sword):
    name: str = "Uraku Misugiri"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=19.2)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Brocade Bloom, Shrine Sword"
    refi_list: list[str] = [
        "Normal Attack DMG is increased by 16% and Elemental Skill DMG is increased by 24%. After a nearby active character deals Geo DMG, the aforementioned effects increase by 100% for 15s. Additionally, the wielder's DEF is increased by 20%.",
        "Normal Attack DMG is increased by 20% and Elemental Skill DMG is increased by 30%. After a nearby active character deals Geo DMG, the aforementioned effects increase by 100% for 15s. Additionally, the wielder's DEF is increased by 25%.",
        "Normal Attack DMG is increased by 24% and Elemental Skill DMG is increased by 36%. After a nearby active character deals Geo DMG, the aforementioned effects increase by 100% for 15s. Additionally, the wielder's DEF is increased by 30%.",
        "Normal Attack DMG is increased by 28% and Elemental Skill DMG is increased by 42%. After a nearby active character deals Geo DMG, the aforementioned effects increase by 100% for 15s. Additionally, the wielder's DEF is increased by 35%.",
        "Normal Attack DMG is increased by 32% and Elemental Skill DMG is increased by 48%. After a nearby active character deals Geo DMG, the aforementioned effects increase by 100% for 15s. Additionally, the wielder's DEF is increased by 40%.",
    ]
    file: str = "urmg"
