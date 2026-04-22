from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Linnea(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.linnea
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=11.172, defense=70.5994, health_points=770.28253)
    ascn: BaseStat = BaseStat(attack=45.87492, defense=289.926, health_points=3163.1965)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.geo
    cons_name: str = "Alcyon"
    afln: str = "Adventurer's Guild"
    head: str = "Augur of Wonders"
