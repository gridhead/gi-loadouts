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
    base: BaseStat = BaseStat(attack=19.84892, defense=52.0521, health_points=829.3884)
    ascn: BaseStat = BaseStat(attack=81.50444, defense=213.759, health_points=3405.9172)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.dendro
    cons_name: str = "Cerva Nivea"
    afln: str = "Frostmoon Scions"
    head: str = "Evermoon's Sacrament Song"
