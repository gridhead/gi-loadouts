from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Iansan(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: CharName = CharName.iansan
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=21.54768, defense=53.505375, health_points=893.5552)
    ascn: BaseStat = BaseStat(attack=77.09902, defense=191.44125, health_points=3197.1245)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.electro
    cons_name: str = "Carnotaurus"
    afln: str = "Teteocan"
    head: str = "Tempered in Molten Stone"
