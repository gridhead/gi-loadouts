from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class YaeMiko(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: CharName = CharName.yae_miko
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.4404, defense=44.2742, health_points=807.46204)
    ascn: BaseStat = BaseStat(attack=108.57064, defense=181.818, health_points=3315.8757)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.electro
    cons_name: str = "Divina Vulpes"
    afln: str = "Grand Narukami Shrine"
    head: str = "Astute Amusement"
