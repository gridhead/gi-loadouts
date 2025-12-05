from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Durin(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: CharName = CharName.durin
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.999, defense=64.0181, health_points=967.6198)
    ascn: BaseStat = BaseStat(attack=110.86439, defense=262.899, health_points=3973.57)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.pyro
    cons_name: str = "Draco Rubedo"
    afln: str = "Hexenzirkel"
    head: str = "The Undying Fire"
