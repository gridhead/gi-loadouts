from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class CalamityQueller(Polearm):
    name: str = "Calamity Queller"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=3.6)
    tier: Tier = Tier.Tier_4
    rare: Rare = Rare.Star_5
    refi_name: str = "Extinguishing Precept"
    refi_list: list[str] = [
        "Gain 12% All Elemental DMG Bonus. Obtain Consummation for 20s after using an Elemental Skill, causing ATK to increase by 3.2% per second. This ATK increase has a maximum of 6 stacks. When the character equipped with this weapon is not on the field, Consummation's ATK increase is doubled.",
        "Gain 15% All Elemental DMG Bonus. Obtain Consummation for 20s after using an Elemental Skill, causing ATK to increase by 4% per second. This ATK increase has a maximum of 6 stacks. When the character equipped with this weapon is not on the field, Consummation's ATK increase is doubled.",
        "Gain 18% All Elemental DMG Bonus. Obtain Consummation for 20s after using an Elemental Skill, causing ATK to increase by 4.8% per second. This ATK increase has a maximum of 6 stacks. When the character equipped with this weapon is not on the field, Consummation's ATK increase is doubled.",
        "Gain 21% All Elemental DMG Bonus. Obtain Consummation for 20s after using an Elemental Skill, causing ATK to increase by 5.6% per second. This ATK increase has a maximum of 6 stacks. When the character equipped with this weapon is not on the field, Consummation's ATK increase is doubled.",
        "Gain 24% All Elemental DMG Bonus. Obtain Consummation for 20s after using an Elemental Skill, causing ATK to increase by 6.4% per second. This ATK increase has a maximum of 6 stacks. When the character equipped with this weapon is not on the field, Consummation's ATK increase is doubled.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=12.0)],
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=15.0)],
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=18.0)],
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=21.0)],
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=24.0)],
    ]
    file: str = "cmql"
