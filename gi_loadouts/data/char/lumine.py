from ...type.char import BaseStat, CharName, MainChar
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Lumine(MainChar):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: CharName = CharName.lumine
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=17.808, defense=57.225, health_points=911.791)
    ascn: BaseStat = BaseStat(attack=63.7182, defense=204.75, health_points=3262.3718)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.none
    cons_name: str = "Viatrix"
    head: str = "Outlander"
