from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Ifa(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 24.0, 3: 48.0, 4: 48.0, 5: 72.0, 6: 96.0}
    __statname__: STAT = STAT.elemental_mastery
    name: CharName = CharName.ifa
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=14.95872, defense=50.758575, health_points=845.2303)
    ascn: BaseStat = BaseStat(attack=53.52329, defense=181.61325, health_points=3024.2188)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.anemo
    cons_name: str = "Catena Opele"
    afln: str = "Tlalocan"
    head: str = "In the Wake of Wandering Winds"
