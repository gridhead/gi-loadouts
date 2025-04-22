from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Xiao(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.xiao
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=27.1852, defense=62.2232, health_points=991.4528)
    ascn: BaseStat = BaseStat(attack=111.628975, defense=255.528, health_points=4071.4412)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.anemo
    cons_name: str = "Alatus Nemeseos"
    afln: str = "Liyue Adeptus"
    head: str = "Vigilant Yaksha"
