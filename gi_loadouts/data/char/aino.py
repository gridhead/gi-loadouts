from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Aino(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 24.0, 3: 48.0, 4: 48.0, 5: 72.0, 6: 96.0}
    __statname__: STAT = STAT.elemental_mastery
    name: CharName = CharName.aino
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=20.30112, defense=50.93025, health_points=939.1447)
    ascn: BaseStat = BaseStat(attack=72.63875, defense=182.2275, health_points=3360.243)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.hydro
    cons_name: str = "Cistellula Mira"
    afln: str = "Clink-Clank Krumkake Craftshop"
    head: str = "Whimsical Craftsmith"
