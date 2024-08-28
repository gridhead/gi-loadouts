from enum import Enum

from pydantic import BaseModel


class RareType(BaseModel):
    name: str = ""
    qant: int = 0
    back: str = ""


class Rare(Enum):
    Star_0 = RareType(name="Star 0", qant=0, back=":rare/imgs/rare/star_1.webp")
    Star_1 = RareType(name="Star 1", qant=1, back=":rare/imgs/rare/star_1.webp")
    Star_2 = RareType(name="Star 2", qant=2, back=":rare/imgs/rare/star_2.webp")
    Star_3 = RareType(name="Star 3", qant=3, back=":rare/imgs/rare/star_3.webp")
    Star_4 = RareType(name="Star 4", qant=4, back=":rare/imgs/rare/star_4.webp")
    Star_5 = RareType(name="Star 5", qant=5, back=":rare/imgs/rare/star_5.webp")
