from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TomeoftheEternalFlow(Catalyst):
    name: str = "Tome of the Eternal Flow"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_damage_perc, stat_data=19.2)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Aeon Wave"
    refi_list: list[str] = [
        "HP is increased by 16%. When current HP increases or decreases, Charged Attack DMG will be increased by 14% for 4s. Max 3 stacks, can be triggered once every 0.3s. When you have 3 stacks or refresh a third stack's duration, 8 Energy will be restored. This Energy restoration effect can be triggered once every 12s.",
        "HP is increased by 20%. When current HP increases or decreases, Charged Attack DMG will be increased by 18% for 4s. Max 3 stacks, can be triggered once every 0.3s. When you have 3 stacks or refresh a third stack's duration, 9 Energy will be restored. This Energy restoration effect can be triggered once every 12s.",
        "HP is increased by 24%. When current HP increases or decreases, Charged Attack DMG will be increased by 22% for 4s. Max 3 stacks, can be triggered once every 0.3s. When you have 3 stacks or refresh a third stack's duration, 10 Energy will be restored. This Energy restoration effect can be triggered once every 12s.",
        "HP is increased by 28%. When current HP increases or decreases, Charged Attack DMG will be increased by 26% for 4s. Max 3 stacks, can be triggered once every 0.3s. When you have 3 stacks or refresh a third stack's duration, 11 Energy will be restored. This Energy restoration effect can be triggered once every 12s.",
        "HP is increased by 32%. When current HP increases or decreases, Charged Attack DMG will be increased by 30% for 4s. Max 3 stacks, can be triggered once every 0.3s. When you have 3 stacks or refresh a third stack's duration, 12 Energy will be restored. This Energy restoration effect can be triggered once every 12s.",
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=16.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=20.5)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=24.0)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=28.5)],
        [WeaponStat(stat_name=WeaponStatType.health_points_perc, stat_data=32.0)],
    ]
    file: str = "toef"
