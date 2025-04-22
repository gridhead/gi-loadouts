from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class SkywardAtlas(Catalyst):
    name: str = "Skyward Atlas"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=7.2)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "Wandering Clouds"
    refi_list: list[str] = [
        "Increases Elemental DMG Bonus by 12%. Normal Attack hits have a 50% chance to earn the favor of the clouds which actively seek out nearby opponents to attack for 15s, dealing 160% ATK DMG. Can only occur once every 30s.",
        "Increases Elemental DMG Bonus by 15%. Normal Attack hits have a 50% chance to earn the favor of the clouds which actively seek out nearby opponents to attack for 15s, dealing 200% ATK DMG. Can only occur once every 30s.",
        "Increases Elemental DMG Bonus by 18%. Normal Attack hits have a 50% chance to earn the favor of the clouds which actively seek out nearby opponents to attack for 15s, dealing 240% ATK DMG. Can only occur once every 30s.",
        "Increases Elemental DMG Bonus by 21%. Normal Attack hits have a 50% chance to earn the favor of the clouds which actively seek out nearby opponents to attack for 15s, dealing 280% ATK DMG. Can only occur once every 30s.",
        "Increases Elemental DMG Bonus by 24%. Normal Attack hits have a 50% chance to earn the favor of the clouds which actively seek out nearby opponents to attack for 15s, dealing 320% ATK DMG. Can only occur once every 30s.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=12.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=12.0)],
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=15.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=15.0)],
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=18.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=18.0)],
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=21.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=21.0)],
        [WeaponStat(stat_name=WeaponStatType.damage_bonus_anemo_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_cryo_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_dendro_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_electro_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_geo_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_hydro_perc, stat_data=24.0),WeaponStat(stat_name=WeaponStatType.damage_bonus_pyro_perc, stat_data=24.0)],
    ]
    file: str = "swas"
