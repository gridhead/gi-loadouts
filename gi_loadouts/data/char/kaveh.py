from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Kaveh(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 24.0, 3: 48.0, 4: 48.0, 5: 72.0, 6: 96.0}
    __statname__: STAT = STAT.elemental_mastery
    name: CharName = CharName.kaveh
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=19.5888, defense=62.9475, health_points=1002.9701)
    ascn: BaseStat = BaseStat(attack=70.09002, defense=225.225, health_points=3588.6091)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.dendro
    cons_name: str = "Paradisaea"
    afln: str = "Independent Design Studio"
    head: str = "Empyrean Reflection"
