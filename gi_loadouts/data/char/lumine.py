from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Lumine(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: str = "Lumine"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=17.808, defense=57.225, health_points=911.791)
    ascn: BaseStat = BaseStat(attack=56.75841, defense=182.38703, health_points=2905.032)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.none
    cons_name: str = "Viatrix"
    head: str = "Outlander"
