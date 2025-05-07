from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Escoffier(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.escoffier
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.999, defense=56.95816, health_points=1039.1188)
    ascn: BaseStat = BaseStat(attack=110.86439, defense=233.9064, health_points=4267.1836)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.cryo
    cons_name: str = "Dulciaria Structura"
    afln: str = "Fontaine"
    head: str = "Tasteful Excellence"
