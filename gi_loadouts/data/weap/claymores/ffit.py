from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class FlameForgedInsight(Claymore):
    name: str = "Flame-Forged Insight"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=36.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Mind in Bloom"
    refi_list: list[str] = [
        "When Electro-Charged, Lunar-Charged, or Bloom is triggered, restore 12 Elemental Energy and increase Elemental Mastery by 60 for 15 seconds. This effect can be triggered once every 15s and can be triggered even when the equipping character is off-field.",
        "When Electro-Charged, Lunar-Charged, or Bloom is triggered, restore 15 Elemental Energy and increase Elemental Mastery by 75 for 15 seconds. This effect can be triggered once every 15s and can be triggered even when the equipping character is off-field.",
        "When Electro-Charged, Lunar-Charged, or Bloom is triggered, restore 18 Elemental Energy and increase Elemental Mastery by 90 for 15 seconds. This effect can be triggered once every 15s and can be triggered even when the equipping character is off-field.",
        "When Electro-Charged, Lunar-Charged, or Bloom is triggered, restore 21 Elemental Energy and increase Elemental Mastery by 105 for 15 seconds. This effect can be triggered once every 15s and can be triggered even when the equipping character is off-field.",
        "When Electro-Charged, Lunar-Charged, or Bloom is triggered, restore 24 Elemental Energy and increase Elemental Mastery by 120 for 15 seconds. This effect can be triggered once every 15s and can be triggered even when the equipping character is off-field.",
    ]
    file: str = "ffit"
