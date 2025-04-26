from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class HuntersPath(Bow):
    name: str = "Hunter's Path"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=9.6)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "At the End of the Beast-Paths"
    refi_list: list[str] = [
        "Gain 12% All Elemental DMG Bonus. Obtain the Tireless Hunt effect after hitting an opponent with a Charged Attack. This effect increases Charged Attack DMG by 160% of Elemental Mastery. This effect will be removed after 12 Charged Attacks or 10s. Only 1 instance of Tireless Hunt can be gained every 12s.",
        "Gain 15% All Elemental DMG Bonus. Obtain the Tireless Hunt effect after hitting an opponent with a Charged Attack. This effect increases Charged Attack DMG by 200% of Elemental Mastery. This effect will be removed after 12 Charged Attacks or 10s. Only 1 instance of Tireless Hunt can be gained every 12s.",
        "Gain 18% All Elemental DMG Bonus. Obtain the Tireless Hunt effect after hitting an opponent with a Charged Attack. This effect increases Charged Attack DMG by 240% of Elemental Mastery. This effect will be removed after 12 Charged Attacks or 10s. Only 1 instance of Tireless Hunt can be gained every 12s.",
        "Gain 21% All Elemental DMG Bonus. Obtain the Tireless Hunt effect after hitting an opponent with a Charged Attack. This effect increases Charged Attack DMG by 280% of Elemental Mastery. This effect will be removed after 12 Charged Attacks or 10s. Only 1 instance of Tireless Hunt can be gained every 12s.",
        "Gain 24% All Elemental DMG Bonus. Obtain the Tireless Hunt effect after hitting an opponent with a Charged Attack. This effect increases Charged Attack DMG by 320% of Elemental Mastery. This effect will be removed after 12 Charged Attacks or 10s. Only 1 instance of Tireless Hunt can be gained every 12s.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=12.0)],
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=15.0)],
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=18.0)],
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=21.0)],
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=24.0)],
    ]
    file: str = "htpt"
