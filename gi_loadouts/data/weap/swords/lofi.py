from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class LightofFoliarIncision(Sword):
    name: str = "Light of Foliar Incision"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=19.2)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Whitemoon Bristle"
    refi_list: list[str] = [
            "CRIT Rate is increased by 4%. After Normal Attacks deal Elemental DMG, the Foliar Incision effect will be obtained, increasing DMG dealt by Normal Attacks and Elemental Skills by 120% of Elemental Mastery. This effect will disappear after 28 DMG instances or 12s. You can obtain Foliar Incision once every 12s.",
            "CRIT Rate is increased by 5%. After Normal Attacks deal Elemental DMG, the Foliar Incision effect will be obtained, increasing DMG dealt by Normal Attacks and Elemental Skills by 150% of Elemental Mastery. This effect will disappear after 28 DMG instances or 12s. You can obtain Foliar Incision once every 12s.",
            "CRIT Rate is increased by 6%. After Normal Attacks deal Elemental DMG, the Foliar Incision effect will be obtained, increasing DMG dealt by Normal Attacks and Elemental Skills by 180% of Elemental Mastery. This effect will disappear after 28 DMG instances or 12s. You can obtain Foliar Incision once every 12s.",
            "CRIT Rate is increased by 7%. After Normal Attacks deal Elemental DMG, the Foliar Incision effect will be obtained, increasing DMG dealt by Normal Attacks and Elemental Skills by 210% of Elemental Mastery. This effect will disappear after 28 DMG instances or 12s. You can obtain Foliar Incision once every 12s.",
            "CRIT Rate is increased by 8%. After Normal Attacks deal Elemental DMG, the Foliar Incision effect will be obtained, increasing DMG dealt by Normal Attacks and Elemental Skills by 240% of Elemental Mastery. This effect will disappear after 28 DMG instances or 12s. You can obtain Foliar Incision once every 12s.",
        ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=4.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=5.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=7.0)],
        [WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=8.0)],
    ]
    file: str = "lofi"
