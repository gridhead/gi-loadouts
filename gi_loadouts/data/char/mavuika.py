from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Mavuika(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: CharName = CharName.mavuika
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=27.93, defense=61.62, health_points=977.00)
    ascn: BaseStat = BaseStat(attack=114.68973, defense=253.11282, health_points=4013.99700)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.pyro
    cons_name: str = "Sol Invictus"
    afln: str = "Huitztlan"
    head: str = "Night-Igniting Flame"
