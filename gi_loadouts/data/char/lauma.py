from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Lauma(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 28.8, 3: 57.6, 4: 57.6, 5: 86.4, 6: 115.2}
    __statname__: STAT = STAT.elemental_mastery
    name: CharName = CharName.lauma
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=19.85, defense=52.05, health_points=829)
    ascn: BaseStat = BaseStat(attack=81.49085, defense=213.86244, health_points=3409.369)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.dendro
    cons_name: str = "Absent"
    afln: str = "Absent"
    head: str = "Absent"
