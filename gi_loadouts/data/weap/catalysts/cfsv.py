from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class CashflowSupervision(Catalyst):
    name: str = "Cashflow Supervision"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=4.8)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "Golden Blood-Tide"
    refi_list: list[str] = [
        "ATK is increased by 16%. When current HP increases or decreases, Normal Attack DMG will be increased by 16% and Charged Attack DMG will be increased by 14% for 4s. Max 3 stacks. This effect can be triggered once every 0.3s. When the wielder has 3 stacks, ATK SPD will be increased by 8%.",
        "ATK is increased by 20%. When current HP increases or decreases, Normal Attack DMG will be increased by 20% and Charged Attack DMG will be increased by 17.5% for 4s. Max 3 stacks. This effect can be triggered once every 0.3s. When the wielder has 3 stacks, ATK SPD will be increased by 10%.",
        "ATK is increased by 24%. When current HP increases or decreases, Normal Attack DMG will be increased by 24% and Charged Attack DMG will be increased by 21% for 4s. Max 3 stacks. This effect can be triggered once every 0.3s. When the wielder has 3 stacks, ATK SPD will be increased by 12%.",
        "ATK is increased by 28%. When current HP increases or decreases, Normal Attack DMG will be increased by 28% and Charged Attack DMG will be increased by 24.5% for 4s. Max 3 stacks. This effect can be triggered once every 0.3s. When the wielder has 3 stacks, ATK SPD will be increased by 14%.",
        "ATK is increased by 32%. When current HP increases or decreases, Normal Attack DMG will be increased by 32% and Charged Attack DMG will be increased by 28% for 4s. Max 3 stacks. This effect can be triggered once every 0.3s. When the wielder has 3 stacks, ATK SPD will be increased by 16%."
    ]
    refi_stat: list[WeaponStat] = [
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=16.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=20.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=24.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=28.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=32.0)],
    ]
    file: str = "cfsv"
