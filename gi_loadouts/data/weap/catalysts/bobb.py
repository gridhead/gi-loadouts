from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class BalladoftheBoundlessBlue(Catalyst):
    name: str = "Ballad of the Boundless Blue"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=6.7)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Azure Skies"
    refi_list: list[str] = [
        "Within 6s after Normal or Charged Attacks hit an opponent, Normal Attack DMG will be increased by 8% and Charged Attack DMG will be increased by 6%. Max 3 stacks. This effect can be triggered once every 0.3s.",
        "Within 6s after Normal or Charged Attacks hit an opponent, Normal Attack DMG will be increased by 10% and Charged Attack DMG will be increased by 7.5%. Max 3 stacks. This effect can be triggered once every 0.3s.",
        "Within 6s after Normal or Charged Attacks hit an opponent, Normal Attack DMG will be increased by 12% and Charged Attack DMG will be increased by 9%. Max 3 stacks. This effect can be triggered once every 0.3s.",
        "Within 6s after Normal or Charged Attacks hit an opponent, Normal Attack DMG will be increased by 14% and Charged Attack DMG will be increased by 10.5%. Max 3 stacks. This effect can be triggered once every 0.3s.",
        "Within 6s after Normal or Charged Attacks hit an opponent, Normal Attack DMG will be increased by 16% and Charged Attack DMG will be increased by 12%. Max 3 stacks. This effect can be triggered once every 0.3s.",
    ]
    file: str = "bobb"
