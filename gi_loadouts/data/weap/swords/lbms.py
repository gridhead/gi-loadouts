from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class LightbearingMoonshard(Sword):
    name: str = "Lightbearing Moonshard"
    seco_stat: WeaponStat = WeaponStat(
        stat_name=WeaponStatType.critical_damage_perc, stat_data=19.2
    )
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Legacy of Lang-Gan"
    refi_list: list[str] = [
        "Increases DEF by 20%. DMG inflicted by Lunar-Crystallize reactions increases by 64% for 5s after the equipping character uses an Elemental Skill.",
        "Increases DEF by 25%. DMG inflicted by Lunar-Crystallize reactions increases by 80% for 5s after the equipping character uses an Elemental Skill.",
        "Increases DEF by 30%. DMG inflicted by Lunar-Crystallize reactions increases by 96% for 5s after the equipping character uses an Elemental Skill.",
        "Increases DEF by 35%. DMG inflicted by Lunar-Crystallize reactions increases by 112% for 5s after the equipping character uses an Elemental Skill.",
        "Increases DEF by 40%. DMG inflicted by Lunar-Crystallize reactions increases by 128% for 5s after the equipping character uses an Elemental Skill.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=25.0)],
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=30.0)],
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=35.0)],
        [WeaponStat(stat_name=WeaponStatType.defense_perc, stat_data=40.0)],
    ]
    file: str = "lbms"
