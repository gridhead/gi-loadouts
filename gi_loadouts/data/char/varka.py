from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Varka(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: CharName = CharName.varka
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=27.4645, defense=61.92405, health_points=981.9196)
    ascn: BaseStat = BaseStat(attack=112.77585, defense=254.2995, health_points=4032.2927)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.anemo
    cons_name: str = "Lupus Majoris"
    afln: str = "Knights of Favonius"
    head: str = "Knight of Boreas"
