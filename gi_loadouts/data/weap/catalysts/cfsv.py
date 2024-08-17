from typing import List

from gi_loadouts.type.rare import Rare
from gi_loadouts.type.weap import Catalyst, WeaponStat, WeaponStatType
from gi_loadouts.type.weap.base.tier import Tier


class CashflowSupervision(Catalyst):
    name: str = "Cashflow Supervision"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=4.8)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_list: List[str] = []
