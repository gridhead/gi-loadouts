from enum import Enum

from pydantic import BaseModel

from ..rank import Rank


class LevelType(BaseModel):
    """
    Data class for level specification of weapons and characters
    """
    name: str
    qant: int
    rank: Rank


__level__ = {
    "Level 01/20 (Rank 0)": LevelType(qant=1, rank=Rank.Rank_0, name="Level 01/20 (Rank 0)"),
    "Level 02/20 (Rank 0)": LevelType(qant=2, rank=Rank.Rank_0, name="Level 02/20 (Rank 0)"),
    "Level 03/20 (Rank 0)": LevelType(qant=3, rank=Rank.Rank_0, name="Level 03/20 (Rank 0)"),
    "Level 04/20 (Rank 0)": LevelType(qant=4, rank=Rank.Rank_0, name="Level 04/20 (Rank 0)"),
    "Level 05/20 (Rank 0)": LevelType(qant=5, rank=Rank.Rank_0, name="Level 05/20 (Rank 0)"),
    "Level 06/20 (Rank 0)": LevelType(qant=6, rank=Rank.Rank_0, name="Level 06/20 (Rank 0)"),
    "Level 07/20 (Rank 0)": LevelType(qant=7, rank=Rank.Rank_0, name="Level 07/20 (Rank 0)"),
    "Level 08/20 (Rank 0)": LevelType(qant=8, rank=Rank.Rank_0, name="Level 08/20 (Rank 0)"),
    "Level 09/20 (Rank 0)": LevelType(qant=9, rank=Rank.Rank_0, name="Level 09/20 (Rank 0)"),
    "Level 10/20 (Rank 0)": LevelType(qant=10, rank=Rank.Rank_0, name="Level 10/20 (Rank 0)"),
    "Level 11/20 (Rank 0)": LevelType(qant=11, rank=Rank.Rank_0, name="Level 11/20 (Rank 0)"),
    "Level 12/20 (Rank 0)": LevelType(qant=12, rank=Rank.Rank_0, name="Level 12/20 (Rank 0)"),
    "Level 13/20 (Rank 0)": LevelType(qant=13, rank=Rank.Rank_0, name="Level 13/20 (Rank 0)"),
    "Level 14/20 (Rank 0)": LevelType(qant=14, rank=Rank.Rank_0, name="Level 14/20 (Rank 0)"),
    "Level 15/20 (Rank 0)": LevelType(qant=15, rank=Rank.Rank_0, name="Level 15/20 (Rank 0)"),
    "Level 16/20 (Rank 0)": LevelType(qant=16, rank=Rank.Rank_0, name="Level 16/20 (Rank 0)"),
    "Level 17/20 (Rank 0)": LevelType(qant=17, rank=Rank.Rank_0, name="Level 17/20 (Rank 0)"),
    "Level 18/20 (Rank 0)": LevelType(qant=18, rank=Rank.Rank_0, name="Level 18/20 (Rank 0)"),
    "Level 19/20 (Rank 0)": LevelType(qant=19, rank=Rank.Rank_0, name="Level 19/20 (Rank 0)"),
    "Level 20/20 (Rank 0)": LevelType(qant=20, rank=Rank.Rank_0, name="Level 20/20 (Rank 0)"),
    "Level 20/40 (Rank 1)": LevelType(qant=20, rank=Rank.Rank_1, name="Level 20/40 (Rank 1)"),
    "Level 21/40 (Rank 1)": LevelType(qant=21, rank=Rank.Rank_1, name="Level 21/40 (Rank 1)"),
    "Level 22/40 (Rank 1)": LevelType(qant=22, rank=Rank.Rank_1, name="Level 22/40 (Rank 1)"),
    "Level 23/40 (Rank 1)": LevelType(qant=23, rank=Rank.Rank_1, name="Level 23/40 (Rank 1)"),
    "Level 24/40 (Rank 1)": LevelType(qant=24, rank=Rank.Rank_1, name="Level 24/40 (Rank 1)"),
    "Level 25/40 (Rank 1)": LevelType(qant=25, rank=Rank.Rank_1, name="Level 25/40 (Rank 1)"),
    "Level 26/40 (Rank 1)": LevelType(qant=26, rank=Rank.Rank_1, name="Level 26/40 (Rank 1)"),
    "Level 27/40 (Rank 1)": LevelType(qant=27, rank=Rank.Rank_1, name="Level 27/40 (Rank 1)"),
    "Level 28/40 (Rank 1)": LevelType(qant=28, rank=Rank.Rank_1, name="Level 28/40 (Rank 1)"),
    "Level 29/40 (Rank 1)": LevelType(qant=29, rank=Rank.Rank_1, name="Level 29/40 (Rank 1)"),
    "Level 30/40 (Rank 1)": LevelType(qant=30, rank=Rank.Rank_1, name="Level 30/40 (Rank 1)"),
    "Level 31/40 (Rank 1)": LevelType(qant=31, rank=Rank.Rank_1, name="Level 31/40 (Rank 1)"),
    "Level 32/40 (Rank 1)": LevelType(qant=32, rank=Rank.Rank_1, name="Level 32/40 (Rank 1)"),
    "Level 33/40 (Rank 1)": LevelType(qant=33, rank=Rank.Rank_1, name="Level 33/40 (Rank 1)"),
    "Level 34/40 (Rank 1)": LevelType(qant=34, rank=Rank.Rank_1, name="Level 34/40 (Rank 1)"),
    "Level 35/40 (Rank 1)": LevelType(qant=35, rank=Rank.Rank_1, name="Level 35/40 (Rank 1)"),
    "Level 36/40 (Rank 1)": LevelType(qant=36, rank=Rank.Rank_1, name="Level 36/40 (Rank 1)"),
    "Level 37/40 (Rank 1)": LevelType(qant=37, rank=Rank.Rank_1, name="Level 37/40 (Rank 1)"),
    "Level 38/40 (Rank 1)": LevelType(qant=38, rank=Rank.Rank_1, name="Level 38/40 (Rank 1)"),
    "Level 39/40 (Rank 1)": LevelType(qant=39, rank=Rank.Rank_1, name="Level 39/40 (Rank 1)"),
    "Level 40/40 (Rank 1)": LevelType(qant=40, rank=Rank.Rank_1, name="Level 40/40 (Rank 1)"),
    "Level 40/50 (Rank 2)": LevelType(qant=40, rank=Rank.Rank_2, name="Level 40/50 (Rank 2)"),
    "Level 41/50 (Rank 2)": LevelType(qant=41, rank=Rank.Rank_2, name="Level 41/50 (Rank 2)"),
    "Level 42/50 (Rank 2)": LevelType(qant=42, rank=Rank.Rank_2, name="Level 42/50 (Rank 2)"),
    "Level 43/50 (Rank 2)": LevelType(qant=43, rank=Rank.Rank_2, name="Level 43/50 (Rank 2)"),
    "Level 44/50 (Rank 2)": LevelType(qant=44, rank=Rank.Rank_2, name="Level 44/50 (Rank 2)"),
    "Level 45/50 (Rank 2)": LevelType(qant=45, rank=Rank.Rank_2, name="Level 45/50 (Rank 2)"),
    "Level 46/50 (Rank 2)": LevelType(qant=46, rank=Rank.Rank_2, name="Level 46/50 (Rank 2)"),
    "Level 47/50 (Rank 2)": LevelType(qant=47, rank=Rank.Rank_2, name="Level 47/50 (Rank 2)"),
    "Level 48/50 (Rank 2)": LevelType(qant=48, rank=Rank.Rank_2, name="Level 48/50 (Rank 2)"),
    "Level 49/50 (Rank 2)": LevelType(qant=49, rank=Rank.Rank_2, name="Level 49/50 (Rank 2)"),
    "Level 50/50 (Rank 2)": LevelType(qant=50, rank=Rank.Rank_2, name="Level 50/50 (Rank 2)"),
    "Level 50/60 (Rank 3)": LevelType(qant=50, rank=Rank.Rank_3, name="Level 50/60 (Rank 3)"),
    "Level 51/60 (Rank 3)": LevelType(qant=51, rank=Rank.Rank_3, name="Level 51/60 (Rank 3)"),
    "Level 52/60 (Rank 3)": LevelType(qant=52, rank=Rank.Rank_3, name="Level 52/60 (Rank 3)"),
    "Level 53/60 (Rank 3)": LevelType(qant=53, rank=Rank.Rank_3, name="Level 53/60 (Rank 3)"),
    "Level 54/60 (Rank 3)": LevelType(qant=54, rank=Rank.Rank_3, name="Level 54/60 (Rank 3)"),
    "Level 55/60 (Rank 3)": LevelType(qant=55, rank=Rank.Rank_3, name="Level 55/60 (Rank 3)"),
    "Level 56/60 (Rank 3)": LevelType(qant=56, rank=Rank.Rank_3, name="Level 56/60 (Rank 3)"),
    "Level 57/60 (Rank 3)": LevelType(qant=57, rank=Rank.Rank_3, name="Level 57/60 (Rank 3)"),
    "Level 58/60 (Rank 3)": LevelType(qant=58, rank=Rank.Rank_3, name="Level 58/60 (Rank 3)"),
    "Level 59/60 (Rank 3)": LevelType(qant=59, rank=Rank.Rank_3, name="Level 59/60 (Rank 3)"),
    "Level 60/60 (Rank 3)": LevelType(qant=60, rank=Rank.Rank_3, name="Level 60/60 (Rank 3)"),
    "Level 60/70 (Rank 4)": LevelType(qant=60, rank=Rank.Rank_4, name="Level 60/70 (Rank 4)"),
    "Level 61/70 (Rank 4)": LevelType(qant=61, rank=Rank.Rank_4, name="Level 61/70 (Rank 4)"),
    "Level 62/70 (Rank 4)": LevelType(qant=62, rank=Rank.Rank_4, name="Level 62/70 (Rank 4)"),
    "Level 63/70 (Rank 4)": LevelType(qant=63, rank=Rank.Rank_4, name="Level 63/70 (Rank 4)"),
    "Level 64/70 (Rank 4)": LevelType(qant=64, rank=Rank.Rank_4, name="Level 64/70 (Rank 4)"),
    "Level 65/70 (Rank 4)": LevelType(qant=65, rank=Rank.Rank_4, name="Level 65/70 (Rank 4)"),
    "Level 66/70 (Rank 4)": LevelType(qant=66, rank=Rank.Rank_4, name="Level 66/70 (Rank 4)"),
    "Level 67/70 (Rank 4)": LevelType(qant=67, rank=Rank.Rank_4, name="Level 67/70 (Rank 4)"),
    "Level 68/70 (Rank 4)": LevelType(qant=68, rank=Rank.Rank_4, name="Level 68/70 (Rank 4)"),
    "Level 69/70 (Rank 4)": LevelType(qant=69, rank=Rank.Rank_4, name="Level 69/70 (Rank 4)"),
    "Level 70/70 (Rank 4)": LevelType(qant=70, rank=Rank.Rank_4, name="Level 70/70 (Rank 4)"),
    "Level 70/80 (Rank 5)": LevelType(qant=70, rank=Rank.Rank_5, name="Level 70/80 (Rank 5)"),
    "Level 71/80 (Rank 5)": LevelType(qant=71, rank=Rank.Rank_5, name="Level 71/80 (Rank 5)"),
    "Level 72/80 (Rank 5)": LevelType(qant=72, rank=Rank.Rank_5, name="Level 72/80 (Rank 5)"),
    "Level 73/80 (Rank 5)": LevelType(qant=73, rank=Rank.Rank_5, name="Level 73/80 (Rank 5)"),
    "Level 74/80 (Rank 5)": LevelType(qant=74, rank=Rank.Rank_5, name="Level 74/80 (Rank 5)"),
    "Level 75/80 (Rank 5)": LevelType(qant=75, rank=Rank.Rank_5, name="Level 75/80 (Rank 5)"),
    "Level 76/80 (Rank 5)": LevelType(qant=76, rank=Rank.Rank_5, name="Level 76/80 (Rank 5)"),
    "Level 77/80 (Rank 5)": LevelType(qant=77, rank=Rank.Rank_5, name="Level 77/80 (Rank 5)"),
    "Level 78/80 (Rank 5)": LevelType(qant=78, rank=Rank.Rank_5, name="Level 78/80 (Rank 5)"),
    "Level 79/80 (Rank 5)": LevelType(qant=79, rank=Rank.Rank_5, name="Level 79/80 (Rank 5)"),
    "Level 80/80 (Rank 5)": LevelType(qant=80, rank=Rank.Rank_5, name="Level 80/80 (Rank 5)"),
    "Level 80/90 (Rank 6)": LevelType(qant=80, rank=Rank.Rank_6, name="Level 80/90 (Rank 6)"),
    "Level 81/90 (Rank 6)": LevelType(qant=81, rank=Rank.Rank_6, name="Level 81/90 (Rank 6)"),
    "Level 82/90 (Rank 6)": LevelType(qant=82, rank=Rank.Rank_6, name="Level 82/90 (Rank 6)"),
    "Level 83/90 (Rank 6)": LevelType(qant=83, rank=Rank.Rank_6, name="Level 83/90 (Rank 6)"),
    "Level 84/90 (Rank 6)": LevelType(qant=84, rank=Rank.Rank_6, name="Level 84/90 (Rank 6)"),
    "Level 85/90 (Rank 6)": LevelType(qant=85, rank=Rank.Rank_6, name="Level 85/90 (Rank 6)"),
    "Level 86/90 (Rank 6)": LevelType(qant=86, rank=Rank.Rank_6, name="Level 86/90 (Rank 6)"),
    "Level 87/90 (Rank 6)": LevelType(qant=87, rank=Rank.Rank_6, name="Level 87/90 (Rank 6)"),
    "Level 88/90 (Rank 6)": LevelType(qant=88, rank=Rank.Rank_6, name="Level 88/90 (Rank 6)"),
    "Level 89/90 (Rank 6)": LevelType(qant=89, rank=Rank.Rank_6, name="Level 89/90 (Rank 6)"),
    "Level 90/90 (Rank 6)": LevelType(qant=90, rank=Rank.Rank_6, name="Level 90/90 (Rank 6)"),
}


Level = Enum(
    "Level", {
        item.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"): data for item, data in __level__.items()
    }
)
