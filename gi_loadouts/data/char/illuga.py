from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Illuga(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 24.0, 3: 48.0, 4: 48.0, 5: 72.0, 6: 96.0}
    __statname__: STAT = STAT.elemental_mastery
    name: CharName = CharName.illuga
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=16.0272, defense=68.2122, health_points=1002.9701)
    ascn: BaseStat = BaseStat(attack=57.34638, defense=244.062, health_points=3588.6091)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.geo
    cons_name: str = "Oriolus"
    afln: str = "Lightkeepers"
    head: str = "Nightmare's Burning Heart"
