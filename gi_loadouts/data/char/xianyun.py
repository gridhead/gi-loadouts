from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Xianyun(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.attack_perc
    name: CharName = CharName.xianyun
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.068000793457, defense=44.573348999023, health_points=810.32202148438)
    ascn: BaseStat = BaseStat(attack=107.04148101807, defense=183.04649353027, health_points=3327.6201171875)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.anemo
    cons_name: str = "Grus Serena"
    afln: str = "Mt. Aocang"
    head: str = "Passerine Herald"
