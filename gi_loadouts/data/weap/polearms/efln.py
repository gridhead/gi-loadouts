from ....type.rare import Rare
from ....type.weap import Polearm, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier

# Dynamic calculation has not been implemented

class EngulfingLightning(Polearm):
    name: str = "Engulfing Lightning"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=12.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_5
    refi_name: str = "Timeless Dream: Eternal Stove"
    refi_list: list[str] = [
        "ATK increased by 28% of Energy Recharge over the base 100%. You can gain a maximum bonus of 80% ATK. Gain 30% Energy Recharge for 12s after using an Elemental Burst.",
        "ATK increased by 35% of Energy Recharge over the base 100%. You can gain a maximum bonus of 90% ATK. Gain 35% Energy Recharge for 12s after using an Elemental Burst.",
        "ATK increased by 42% of Energy Recharge over the base 100%. You can gain a maximum bonus of 100% ATK. Gain 40% Energy Recharge for 12s after using an Elemental Burst.",
        "ATK increased by 49% of Energy Recharge over the base 100%. You can gain a maximum bonus of 110% ATK. Gain 45% Energy Recharge for 12s after using an Elemental Burst.",
        "ATK increased by 56% of Energy Recharge over the base 100%. You can gain a maximum bonus of 120% ATK. Gain 50% Energy Recharge for 12s after using an Elemental Burst.",
    ]
    file: str = "efln"
