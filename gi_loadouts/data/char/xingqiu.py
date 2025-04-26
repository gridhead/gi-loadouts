from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Xingqiu(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: CharName = CharName.xingqiu
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=16.9176, defense=63.51975, health_points=857.08356)
    ascn: BaseStat = BaseStat(attack=60.53229, defense=227.2725, health_points=3066.6296)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.hydro
    cons_name: str = "Fabulae Textile"
    afln: str = "Feiyun Commerce Guild"
    head: str = "Juvenile Galant"
