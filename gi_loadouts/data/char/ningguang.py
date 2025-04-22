from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Ningguang(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.damage_bonus_geo_perc
    name: CharName = CharName.ningguang
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=17.808, defense=48.069, health_points=820.6119)
    ascn: BaseStat = BaseStat(attack=63.7182, defense=171.99, health_points=2936.1348)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.geo
    cons_name: str = "Opus Aequilibrium"
    afln: str = "Liyue Qixing"
    head: str = "Eclipsing Star"
