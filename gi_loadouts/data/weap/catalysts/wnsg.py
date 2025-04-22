from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class WineandSong(Catalyst):
    name: str = "Wine and Song"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.energy_recharge_perc, stat_data=6.7)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Ever-Changing"
    refi_list: list[str] = [
        "Hitting an opponent with a Normal Attack decreases the Stamina consumption of Sprint or Alternate Sprint by 14% for 5s. Additionally, using a Sprint or Alternate Sprint ability increases ATK by 20% for 5s.",
        "Hitting an opponent with a Normal Attack decreases the Stamina consumption of Sprint or Alternate Sprint by 16% for 5s. Additionally, using a Sprint or Alternate Sprint ability increases ATK by 25% for 5s.",
        "Hitting an opponent with a Normal Attack decreases the Stamina consumption of Sprint or Alternate Sprint by 18% for 5s. Additionally, using a Sprint or Alternate Sprint ability increases ATK by 30% for 5s.",
        "Hitting an opponent with a Normal Attack decreases the Stamina consumption of Sprint or Alternate Sprint by 20% for 5s. Additionally, using a Sprint or Alternate Sprint ability increases ATK by 35% for 5s.",
        "Hitting an opponent with a Normal Attack decreases the Stamina consumption of Sprint or Alternate Sprint by 22% for 5s. Additionally, using a Sprint or Alternate Sprint ability increases ATK by 40% for 5s.",
    ]
    file: str = "wnsg"
