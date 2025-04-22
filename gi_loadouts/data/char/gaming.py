from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Gaming(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: CharName = CharName.gaming
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=25.287359237671, defense=58.941749572754, health_points=957.38055419922)
    ascn: BaseStat = BaseStat(attack=90.479843139648, defense=210.89250183105, health_points=3425.4904785156)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.pyro
    cons_name: str = "Leo Expergiscens"
    afln: str = "Sword and Strongbox Secure Transport Agency (Faction)"
    head: str = "Leonine Vanguard"
