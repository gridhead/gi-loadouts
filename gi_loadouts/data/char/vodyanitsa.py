from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Vodyanitsa(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.health_points_perc
    name: CharName = CharName.vodyanitsa
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=8.379, defense=37.6929, health_points=1153.5172)
    ascn: BaseStat = BaseStat(attack=34.40619, defense=154.791, health_points=4736.9653)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.hydro
    cons_name: str = "Piscicula Aurea"
    afln: str = "Korolevskiy Troupe"
    head: str = "Lingering Siren-Song"
