from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Shenhe(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.attack_perc
    name: CharName = CharName.shenhe
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=23.6474, defense=64.6164, health_points=1011.47253)
    ascn: BaseStat = BaseStat(attack=97.10191, defense=265.356, health_points=4153.653)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.cryo
    cons_name: str = "Crista Doloris"
    afln: str = "Cloud Retainer's Abode"
    head: str = "Lonesome Transcendence"
