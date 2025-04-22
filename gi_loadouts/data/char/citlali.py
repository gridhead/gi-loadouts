from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Citlali(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 28.8, 3: 57.6, 4: 57.6, 5: 86.4, 6: 115.2}
    __statname__: STAT = STAT.elemental_mastery
    name: CharName = CharName.citlali
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=9.87, defense=59.41, health_points=906)
    ascn: BaseStat = BaseStat(attack=40.50607, defense=243.98601, health_points=3716.46600)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.cryo
    cons_name: str = "Patina Anavatlaca"
    afln: str = "Mictlan"
    head: str = "Obsidian Opalstar"
