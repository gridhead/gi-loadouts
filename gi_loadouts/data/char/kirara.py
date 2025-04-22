from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Kirara(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.health_points_perc
    name: CharName = CharName.kirara
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=18.6984, defense=45.78, health_points=1021.2059)
    ascn: BaseStat = BaseStat(attack=66.904113769531, defense=163.8, health_points=3653.8564453125)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.dendro
    cons_name: str = "Arcella"
    afln: str = "Komaniya Express"
    head: str = "Cat Upon the Eaves"
