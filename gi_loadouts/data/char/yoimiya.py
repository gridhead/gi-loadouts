from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Yoimiya(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.yoimiya
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=25.137, defense=47.864, health_points=791.2556)
    ascn: BaseStat = BaseStat(attack=103.21857, defense=196.56, health_points=3249.3232)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.pyro
    cons_name: str = "Carassius Auratus"
    afln: str = "Naganohara Fireworks"
    head: str = "Frolicking Flames"
