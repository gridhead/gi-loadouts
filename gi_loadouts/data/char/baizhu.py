from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Baizhu(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.health_points_perc
    name: CharName = CharName.baizhu
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=14.9891, defense=38.8895, health_points=1039.1188)
    ascn: BaseStat = BaseStat(attack=61.54885, defense=159.705, health_points=4267.1836)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.dendro
    cons_name: str = "Lagenaria"
    afln: str = "Bubu Pharmacy"
    head: str = "Beyond Mortality"
