from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Tartaglia(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.damage_bonus_hydro_perc
    name: CharName = CharName.tartaglia
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=23.4612, defense=63.4198, health_points=1020.0524)
    ascn: BaseStat = BaseStat(attack=96.33733, defense=260.442, health_points=4188.8867)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.hydro
    cons_name: str = "Monoceros Caeli"
    afln: str = "Fatui"
    head: str = "Childe"
