from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Dahlia(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.health_points_perc
    name: CharName = CharName.dahlia
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=15.84912, defense=46.9245, health_points=1048.5597)
    ascn: BaseStat = BaseStat(attack=56.709198, defense=167.895, health_points=3751.7275)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.hydro
    cons_name: str = "Cantus Choralis"
    afln: str = "Church of Favonius"
    head: str = "Ode and Oblation"
