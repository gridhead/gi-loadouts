from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Yanfei(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.damage_bonus_pyro_perc
    name: CharName = CharName.yanfei
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=20.12304, defense=49.2135, health_points=784.14026)
    ascn: BaseStat = BaseStat(attack=72.001564, defense=176.085, health_points=2805.64)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.pyro
    cons_name: str = "Bestia Iustitia"
    afln: str = "Yanfei Legal Consultancy"
    head: str = "Wise Innocence"
