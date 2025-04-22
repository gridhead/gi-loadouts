from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Nilou(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.health_points_perc
    name: CharName = CharName.nilou
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=17.8752, defense=56.71884, health_points=1182.1168)
    ascn: BaseStat = BaseStat(attack=73.39987, defense=232.9236, health_points=4854.4106)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.hydro
    cons_name: str = "Lotos Somno"
    afln: str = "Zubayr Theater"
    head: str = "Dance of Lotuslight"
