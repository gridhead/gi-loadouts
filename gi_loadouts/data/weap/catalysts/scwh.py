from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class StarcallersWatch(Catalyst):
    name: str = "Starcaller's Watch"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=58.0)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Offering Unto Wind and Sun"
    refi_list: list[str] = [
        "Increases Elemental Mastery by 100. Gain the \"Mirror of Night\" effect within 15s after the equipping character creates a shield: The current active party member deals 28% increased DMG to nearby opponents. You can gain the \"Mirror of Night\" effect once every 14s.",
        "Increases Elemental Mastery by 125. Gain the \"Mirror of Night\" effect within 15s after the equipping character creates a shield: The current active party member deals 35% increased DMG to nearby opponents. You can gain the \"Mirror of Night\" effect once every 14s.",
        "Increases Elemental Mastery by 150. Gain the \"Mirror of Night\" effect within 15s after the equipping character creates a shield: The current active party member deals 42% increased DMG to nearby opponents. You can gain the \"Mirror of Night\" effect once every 14s.",
        "Increases Elemental Mastery by 175. Gain the \"Mirror of Night\" effect within 15s after the equipping character creates a shield: The current active party member deals 49% increased DMG to nearby opponents. You can gain the \"Mirror of Night\" effect once every 14s.",
        "Increases Elemental Mastery by 200. Gain the \"Mirror of Night\" effect within 15s after the equipping character creates a shield: The current active party member deals 56% increased DMG to nearby opponents. You can gain the \"Mirror of Night\" effect once every 14s.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=100.0)],
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=125.0)],
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=150.0)],
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=175.0)],
        [WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=200.0)],
    ]
    file: str = "scwh"
