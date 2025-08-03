from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Ineffa(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.ineffa
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=25.6956, defense=64.43691, health_points=981.9196)
    ascn: BaseStat = BaseStat(attack=105.512314, defense=264.6189, health_points=4032.2927)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.electro
    cons_name: str = "Vanilla Planifolia"
    afln: str = "Clink-Clank Krumkake Craftshop"
    head: str = "Boom Boom Thunderwave"
