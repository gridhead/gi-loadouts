from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Nahida(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 28.8, 3: 57.6, 4: 57.6, 5: 86.4, 6: 115.2}
    __statname__: STAT = STAT.elemental_mastery
    name: CharName = CharName.nahida
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=23.275, defense=49.0606, health_points=806.5087)
    ascn: BaseStat = BaseStat(attack=95.57275, defense=201.474, health_points=3311.961)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.dendro
    cons_name: str = "Sapientia Oromasdis"
    afln: str = "Sumeru City"
    head: str = "Physic of Purity"
