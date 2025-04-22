from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class TalkingStick(Claymore):
    name: str = "Talking Stick"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=4.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "\"The Silver Tongue\""
    refi_list: list[str] = [
        "ATK will be increased by 16% for 15s after being affected by Pyro. This effect can be triggered once every 12s. All Elemental DMG Bonus will be increased by 12% for 15s after being affected by Hydro, Cryo, Electro, or Dendro. This effect can be triggered once every 12s.",
        "ATK will be increased by 20% for 15s after being affected by Pyro. This effect can be triggered once every 12s. All Elemental DMG Bonus will be increased by 15% for 15s after being affected by Hydro, Cryo, Electro, or Dendro. This effect can be triggered once every 12s.",
        "ATK will be increased by 24% for 15s after being affected by Pyro. This effect can be triggered once every 12s. All Elemental DMG Bonus will be increased by 18% for 15s after being affected by Hydro, Cryo, Electro, or Dendro. This effect can be triggered once every 12s.",
        "ATK will be increased by 28% for 15s after being affected by Pyro. This effect can be triggered once every 12s. All Elemental DMG Bonus will be increased by 21% for 15s after being affected by Hydro, Cryo, Electro, or Dendro. This effect can be triggered once every 12s.",
        "ATK will be increased by 32% for 15s after being affected by Pyro. This effect can be triggered once every 12s. All Elemental DMG Bonus will be increased by 24% for 15s after being affected by Hydro, Cryo, Electro, or Dendro. This effect can be triggered once every 12s.",
    ]
    file: str = "tgsk"
