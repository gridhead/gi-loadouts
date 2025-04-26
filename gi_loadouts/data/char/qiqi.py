from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Qiqi(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 5.5, 3: 11.0, 4: 11.0, 5: 16.5, 6: 22.0}
    __statname__: STAT = STAT.healing_bonus_perc
    name: CharName = CharName.qiqi
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=22.344, defense=71.796, health_points=962.8532)
    ascn: BaseStat = BaseStat(attack=91.74984, defense=294.84, health_points=3953.9958)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.cryo
    cons_name: str = "Pristina Nola"
    afln: str = "Bubu Pharmacy"
    head: str = "Icy Resurrection"
