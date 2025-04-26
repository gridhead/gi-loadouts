from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Charlotte(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: CharName = CharName.charlotte
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=14.513520240784, defense=45.78, health_points=902.67309570312)
    ascn: BaseStat = BaseStat(attack=51.930332183838, defense=163.8, health_points=3229.748046875)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.cryo
    cons_name: str = "Hualina Veritas"
    afln: str = "The Steambird"
    head: str = "Lens of Verity"
