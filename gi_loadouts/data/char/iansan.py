from gi_loadouts.type.char import BaseStat, Char, CharName
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Iansan(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: CharName = CharName.iansan
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=0.00, defense=0.00, health_points=0.00)
    ascn: BaseStat = BaseStat(attack=0.00, defense=0.00, health_points=0.00)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.electro
    cons_name: str = "Carnotaurus"
    afln: str = "Teteocan"
    head: str = "Tempered in Molten Stone"
