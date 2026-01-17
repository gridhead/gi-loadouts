from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Columbina(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.columbina
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=7.448, defense=40.0861, health_points=1143.984)
    ascn: BaseStat = BaseStat(attack=30.58328, defense=164.619, health_points=4697.817)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.hydro
    cons_name: str = "Columbina Hyposelenia"
    afln: str = "Frost Moon"
    head: str = "Welkin Moon's Homecoming"
