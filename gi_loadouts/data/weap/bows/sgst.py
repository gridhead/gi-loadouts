from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class Slingshot(Bow):
    name: str = "Slingshot"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.8)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_3
    refi_name: str = "Slingshot"
    refi_list: list[str] = [
            "If a Normal or Charged Attack hits a target within 0.3s of being fired, increases DMG by 36%. Otherwise, decreases DMG by 10%.",
            "If a Normal or Charged Attack hits a target within 0.3s of being fired, increases DMG by 42%. Otherwise, decreases DMG by 10%.",
            "If a Normal or Charged Attack hits a target within 0.3s of being fired, increases DMG by 48%. Otherwise, decreases DMG by 10%.",
            "If a Normal or Charged Attack hits a target within 0.3s of being fired, increases DMG by 54%. Otherwise, decreases DMG by 10%.",
            "If a Normal or Charged Attack hits a target within 0.3s of being fired, increases DMG by 60%. Otherwise, decreases DMG by 10%.",
        ]
    file: str = "sgst"
