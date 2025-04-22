from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Venti(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 8.0, 3: 16.0, 4: 16.0, 5: 24.0, 6: 32.0}
    __statname__: STAT = STAT.energy_recharge_perc
    name: CharName = CharName.venti
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=20.482, defense=52.0521, health_points=819.8552)
    ascn: BaseStat = BaseStat(attack=84.10402, defense=213.759, health_points=3366.7688)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.anemo
    cons_name: str = "Carmen Dei"
    afln: str = "Mondstadt"
    head: str = "Windborne Bard"
