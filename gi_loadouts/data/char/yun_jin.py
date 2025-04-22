from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class YunJin(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.7, 3: 13.4, 4: 13.4, 5: 20.1, 6: 26.8}
    __statname__: STAT = STAT.energy_recharge_perc
    name: CharName = CharName.yun_jin
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=16.0272, defense=61.5741, health_points=893.5552)
    ascn: BaseStat = BaseStat(attack=57.34638, defense=220.311, health_points=3197.1245)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.geo
    cons_name: str = "Opera Grandis"
    afln: str = "Yun-Han Opera Troupe"
    head: str = "Stage Lucida"
