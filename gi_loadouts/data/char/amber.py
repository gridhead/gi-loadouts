from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Amber(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: CharName = CharName.amber
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=18.6984, defense=50.358, health_points=793.2582)
    ascn: BaseStat = BaseStat(attack=66.90411, defense=180.18, health_points=2838.2634)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.pyro
    cons_name: str = "Lepus"
    afln: str = "Knights of Favonius"
    head: str = "Gliding Champion"
