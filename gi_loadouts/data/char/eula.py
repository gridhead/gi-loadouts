from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Eula(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: CharName = CharName.eula
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.6266, defense=58.45391, health_points=1029.5856)
    ascn: BaseStat = BaseStat(attack=109.33523, defense=240.0489, health_points=4228.035)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.cryo
    cons_name: str = "Aphros Delos"
    afln: str = "Knights of Favonius"
    head: str = "Dance of the Shimmering Wave"
