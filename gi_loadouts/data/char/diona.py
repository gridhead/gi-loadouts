from ...type.char import BaseStat, Char, CharName
from ...type.rare import Rare
from ...type.stat import STAT
from ...type.vson import Vision
from ...type.weap import WeaponType


class Diona(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.damage_bonus_cryo_perc
    name: CharName = CharName.diona
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=17.808, defense=50.358, health_points=802.3761)
    ascn: BaseStat = BaseStat(attack=63.7182, defense=180.18, health_points=2870.8872)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.cryo
    cons_name: str = "Feles"
    afln: str = "The Cat's Tail"
    head: str = "Kätzlein Cocktail"
