from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class LanYan(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: CharName = CharName.lan_yan
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=21.01344, defense=48.64125, health_points=775.02234)
    ascn: BaseStat = BaseStat(attack=75.18748, defense=174.0375, health_points=2773.016)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.anemo
    cons_name: str = "Hirundo Lazuli"
    afln: str = "Chenyu Vale Artisans Association"
    head: str = "Spring Woven From Jade"
