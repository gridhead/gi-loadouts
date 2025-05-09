from enum import Enum

from pydantic import BaseModel

from ..levl import Level
from ..rare import Rare
from ..stat import ATTR, STAT
from ..vson import Vision
from ..weap import WeaponType
from .cons import Cons
from .mult import Mult, Secs


class CharName(str, Enum):
    """
    Set of characters possible
    """
    aether = "Aether"
    albedo = "Albedo"
    alhaitham = "Alhaitham"
    aloy = "Aloy"
    amber = "Amber"
    arataki_itto = "Arataki Itto"
    arlecchino = "Arlecchino"
    baizhu = "Baizhu"
    barbara = "Barbara"
    beidou = "Beidou"
    bennett = "Bennett"
    candace = "Candace"
    charlotte = "Charlotte"
    chasca = "Chasca"
    chevreuse = "Chevreuse"
    chiori = "Chiori"
    chongyun = "Chongyun"
    citlali = "Citlali"
    clorinde = "Clorinde"
    collei = "Collei"
    cyno = "Cyno"
    dehya = "Dehya"
    diluc = "Diluc"
    diona = "Diona"
    dori = "Dori"
    emilie = "Emilie"
    escoffier = "Escoffier"
    eula = "Eula"
    faruzan = "Faruzan"
    fischl = "Fischl"
    freminet = "Freminet"
    furina = "Furina"
    gaming = "Gaming"
    ganyu = "Ganyu"
    gorou = "Gorou"
    hu_tao = "Hu Tao"
    iansan = "Iansan"
    ifa = 'Ifa'
    jean = "Jean"
    kachina = "Kachina"
    kaedehara_kazuha = "Kaedehara Kazuha"
    kamisato_ayaka = "Kamisato Ayaka"
    kamisato_ayato = "Kamisato Ayato"
    kaeya = "Kaeya"
    kaveh = "Kaveh"
    keqing = "Keqing"
    kinich = "Kinich"
    kirara = "Kirara"
    klee = "Klee"
    kujou_sara = "Kujou Sara"
    kuki_shinobu = "Kuki Shinobu"
    lan_yan = "Lan Yan"
    layla = "Layla"
    lisa = "Lisa"
    lumine = "Lumine"
    lynette = "Lynette"
    lyney = "Lyney"
    mavuika = "Mavuika"
    mika = "Mika"
    mona = "Mona"
    mualani = "Mualani"
    nahida = "Nahida"
    navia = "Navia"
    neuvillette = "Neuvillette"
    nilou = "Nilou"
    ningguang = "Ningguang"
    noelle = "Noelle"
    ororon = "Ororon"
    qiqi = "Qiqi"
    raiden_shogun = "Raiden Shogun"
    razor = "Razor"
    rosaria = "Rosaria"
    sangonomiya_kokomi = "Sangonomiya Kokomi"
    sayu = "Sayu"
    sethos = "Sethos"
    shenhe = "Shenhe"
    shikanoin_heizou = "Shikanoin Heizou"
    sigewinne = "Sigewinne"
    sucrose = "Sucrose"
    tartaglia = "Tartaglia"
    thoma = "Thoma"
    tighnari = "Tighnari"
    varesa = "Varesa"
    venti = "Venti"
    wanderer = "Wanderer"
    wriothesley = "Wriothesley"
    xiangling = "Xiangling"
    xianyun = "Xianyun"
    xiao = "Xiao"
    xilonen = "Xilonen"
    xingqiu = "Xingqiu"
    xinyan = "Xinyan"
    yae_miko = "Yae Miko"
    yanfei = "Yanfei"
    yaoyao  = "Yaoyao"
    yelan = "Yelan"
    yoimiya = "Yoimiya"
    yumemizuki_mizuki = "Yumemizuki Mizuki"
    yun_jin = "Yun Jin"
    zhongli = "Zhongli"


class SecoStat(BaseModel):
    """
    Data class for secondary stat of a character
    """
    stat_name: STAT = STAT.none
    stat_data: float = 0.0


class Char(BaseModel):
    """
    Character primitive
    """
    __statname__: STAT = STAT.none
    __statdata__: dict = {}
    rare: Rare = Rare.Star_4
    name: CharName = CharName.lumine
    levl: Level = Level.Level_01_20_Rank_0
    cons: Cons = Cons.Constellation_1
    vision: Vision = Vision.none
    weapon: WeaponType = WeaponType.none
    cons_name: str = ""
    afln: str = ""
    head: str = ""

    def _calc_stat(self, base_stat: float, ascension_stat: float, stat_type: STAT) -> ATTR:
        """
        Generalized stat calculation method for attack, defense, and health points.

        :param base_stat: BaseStat value for the character (attack, defense, or health).
        :param ascension_stat: Ascension value for the given stat.
        :param stat_type: Type of the stat (STAT.attack, STAT.defense, or STAT.health_points).
        :return: ATTR instance with calculated stat value.
        """
        stat_data = base_stat * Mult[self.levl.value.qant][self.rare] + Secs[self.levl.value.rank] * ascension_stat

        return ATTR(stat_name=stat_type, stat_data=stat_data)

    @property
    def attack(self) -> ATTR:
        """
        Calculate the statistics associated with the attack potential of a character based on their level, rank and ascension value

        :return: Attack potential associated with the character
        """
        return self._calc_stat(self.base.attack, self.ascn.attack, STAT.attack)

    @property
    def defense(self) -> ATTR:
        """
        Calculate the statistics associated with the defense potential of a character based on their level, rank and ascension value

        :return: Defense potential associated with the character
        """
        return self._calc_stat(self.base.defense, self.ascn.defense, STAT.defense)

    @property
    def health_points(self) -> ATTR:
        """
        Calculate the statistics associated with the health points potential of a character based on their level, rank and ascension value

        :return: Health points potential associated with the character
        """
        return self._calc_stat(self.base.health_points, self.ascn.health_points, STAT.health_points)

    @property
    def seco(self) -> SecoStat:
        """
        Calculate the statistics associated with the health points potential of a character based on their rank

        :return: Secondary statistics associated with the character
        """
        return SecoStat(
            stat_name=self.__statname__,
            stat_data=self.__statdata__[self.levl.value.rank.value]
        )


class MainChar(Char):
    """
    Main character primitive
    """

    def _calc_stat(self, base_stat: float, ascension_stat: float, stat_type: STAT) -> ATTR:
        """
        `Aether` and `Lumine` are special characters. Although they are 5-Star quality
        characters which use the 5-Star Level Multiplier values, they actually use 4-Star
        Level Multipliers. Although this is an anti-pattern and we do not generally
        support such kinds of development, we have implemented this specific calculation
        to ensure the displayed values are accurate for users.

        :param base_stat: BaseStat value for the character (attack, defense, or health).
        :param ascension_stat: Ascension value for the given stat.
        :param stat_type: Type of the stat (STAT.attack, STAT.defense, or STAT.health_points).
        :return: ATTR instance with calculated stat value.
        """
        stat_data = base_stat * Mult[self.levl.value.qant][Rare.Star_4] + Secs[self.levl.value.rank] * ascension_stat

        return ATTR(stat_name=stat_type, stat_data=stat_data)


class BaseStat(BaseModel):
    """
    Base stats of a character
    """
    attack: float = 0.0
    defense: float = 0.0
    health_points: float = 0.0
