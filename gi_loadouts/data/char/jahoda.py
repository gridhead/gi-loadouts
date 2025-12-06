from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Jahoda(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.6, 3: 9.2, 4: 9.2, 5: 18.5, 6: 18.5}
    __statname__: STAT = STAT.healing_bonus_perc
    name: CharName = CharName.jahoda
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=18.6984, defense=48.64125, health_points=808.7586)
    ascn: BaseStat = BaseStat(attack=66.90411, defense=174.0375, health_points=2893.7239)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.anemo
    cons_name: str = "Fragum"
    afln: str = "Curatorium of Secrets"
    head: str = "Windthreading Shadow"
