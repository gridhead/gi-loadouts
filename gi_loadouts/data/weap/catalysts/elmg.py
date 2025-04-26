from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class EverlastingMoonglow(Catalyst):
    name: str = "Everlasting Moonglow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=10.8)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Byakuya Kougetsu"
    refi_list: list[str] = [
        "Healing Bonus increased by 10%, Normal Attack DMG is increased by 1% of the Max HP of the character equipping this weapon. For 12s after using an Elemental Burst, Normal Attacks that hit opponents will restore 0.6 Energy. Energy can be restored this way once every 0.1s.",
        "Healing Bonus increased by 12.5%, Normal Attack DMG is increased by 1.5% of the Max HP of the character equipping this weapon. For 12s after using an Elemental Burst, Normal Attacks that hit opponents will restore 0.6 Energy. Energy can be restored this way once every 0.1s.",
        "Healing Bonus increased by 15%, Normal Attack DMG is increased by 2.0% of the Max HP of the character equipping this weapon. For 12s after using an Elemental Burst, Normal Attacks that hit opponents will restore 0.6 Energy. Energy can be restored this way once every 0.1s.",
        "Healing Bonus increased by 17.5%, Normal Attack DMG is increased by 2.5% of the Max HP of the character equipping this weapon. For 12s after using an Elemental Burst, Normal Attacks that hit opponents will restore 0.6 Energy. Energy can be restored this way once every 0.1s.",
        "Healing Bonus increased by 20%, Normal Attack DMG is increased by 3.0% of the Max HP of the character equipping this weapon. For 12s after using an Elemental Burst, Normal Attacks that hit opponents will restore 0.6 Energy. Energy can be restored this way once every 0.1s.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.healing_bonus_perc, stat_data=10.0)],
        [WeaponStat(stat_name=WeaponStatType.healing_bonus_perc, stat_data=12.5)],
        [WeaponStat(stat_name=WeaponStatType.healing_bonus_perc, stat_data=15.0)],
        [WeaponStat(stat_name=WeaponStatType.healing_bonus_perc, stat_data=17.5)],
        [WeaponStat(stat_name=WeaponStatType.healing_bonus_perc, stat_data=20.0)],
    ]
    file: str = "elmg"
