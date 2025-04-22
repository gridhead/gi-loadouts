from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier

# TODO - Check if the increase DMG is elemental DMG bonus or not

class SkywardPride(Claymore):
    name: str = "Skyward Pride"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=8.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_5
    refi_name: str = "Sky-ripping Dragon Spine"
    refi_list: list[str] = [
        "Increases all DMG by 8%. After using an Elemental Burst, a vacuum blade that does 80% of ATK as DMG to opponents along its path will be created when Normal or Charged Attacks hit. Lasts for 20s or 8 vacuum blades.",
        "Increases all DMG by 10%. After using an Elemental Burst, a vacuum blade that does 100% of ATK as DMG to opponents along its path will be created when Normal or Charged Attacks hit. Lasts for 20s or 8 vacuum blades.",
        "Increases all DMG by 12%. After using an Elemental Burst, a vacuum blade that does 120% of ATK as DMG to opponents along its path will be created when Normal or Charged Attacks hit. Lasts for 20s or 8 vacuum blades.",
        "Increases all DMG by 14%. After using an Elemental Burst, a vacuum blade that does 140% of ATK as DMG to opponents along its path will be created when Normal or Charged Attacks hit. Lasts for 20s or 8 vacuum blades.",
        "Increases all DMG by 16%. After using an Elemental Burst, a vacuum blade that does 160% of ATK as DMG to opponents along its path will be created when Normal or Charged Attacks hit. Lasts for 20s or 8 vacuum blades.",
    ]
    file: str = "swpr"
