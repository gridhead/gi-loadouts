from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Chasca(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.chasca
    rare: Rare = Rare.Star_5
    """
    TODO: Change the default values after the values are updated in Genshin Impact Wiki
    """
    base: BaseStat = BaseStat(attack=26.999, defense=47.864, health_points=762.656)
    ascn: BaseStat = BaseStat(attack=110.86439, defense=196.56, health_points=3131.878)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.anemo
    cons_name: str = "Vultur Gryphus"
    afln: str = "Flower-Feather Clan"
    head: str = "Skyborne Arbiter"
