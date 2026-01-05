from ....type.rare import Rare
from ....type.weap import Bow, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class RainbowSerpentsRainBow(Bow):
    name: str = "Rainbow Serpent's Rain Bow"
    seco_stat: WeaponStat = WeaponStat(
        stat_name=WeaponStatType.energy_recharge_perc, stat_data=10.0
    )
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Astral Whispers Beyond the Sacred Throne"
    refi_list: list[str] = [
        "When the wielder's off-field characters' attacks hit an opponent, ATK is increased by 28% for 8s.",
        "When the wielder's off-field characters' attacks hit an opponent, ATK is increased by 35% for 8s.",
        "When the wielder's off-field characters' attacks hit an opponent, ATK is increased by 42% for 8s.",
        "When the wielder's off-field characters' attacks hit an opponent, ATK is increased by 49% for 8s.",
        "When the wielder's off-field characters' attacks hit an opponent, ATK is increased by 56% for 8s.",
    ]
    file: str = "rsrb"
