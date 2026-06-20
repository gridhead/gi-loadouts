from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Nicole(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.attack_perc
    name: CharName = CharName.nicole
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.6266, defense=43.79556, health_points=810.322)
    ascn: BaseStat = BaseStat(attack=109.33523, defense=179.8524, health_points=3327.62)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.pyro
    cons_name: str = "Reliquiarium"
    afln: str = "Hexenzirkel"
    head: str = "Clamor Within"
