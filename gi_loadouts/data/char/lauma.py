from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Lauma(Char):
    # Lauma has 200 Elemental Mastery in her base statistics
    __statdata__: dict = {0: 200.0, 1: 200.0, 2: 228.8, 3: 257.6, 4: 257.6, 5: 286.4, 6: 315.2}
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
