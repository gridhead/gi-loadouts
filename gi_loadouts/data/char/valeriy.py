from ...type.char import BaseStat, Char
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Valeriy(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: str = "Valeriy"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=21.3696, defense=58.9417, health_points=838.8477)
    ascn: BaseStat = BaseStat(attack=76.4618, defense=210.8925, health_points=3001.3820)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.electro
    cons_name: str = "Ursus Magnus"
    afln: str = "Fatui Grenadier Guards First Regiment"
    head: str = "Fort Fulguration"
