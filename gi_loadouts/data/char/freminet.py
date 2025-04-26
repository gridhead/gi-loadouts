from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Freminet(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: CharName = CharName.freminet
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=21.369600296021, defense=59.399551391602, health_points=1012.0880126953)
    ascn: BaseStat = BaseStat(attack=76.461837768555, defense=212.53050231934, health_points=3621.2326660156)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.cryo
    cons_name: str = "Automaton"
    afln: str = "Hotel Bouffes d'ete"
    head: str = "Yearning for Unseen Depths"
