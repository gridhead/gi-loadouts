from pydantic import BaseModel

from ..rank import Rank
from ..rare import Rare


class AscnType(BaseModel):
    """
    Data class for mapping between quality and multiplier
    """
    rare: Rare = Rare.Star_1
    data: dict


Ascn = {
    Rare.Star_1: AscnType(
        rare=Rare.Star_1,
        data={
            Rank.Rank_0: 0.0,
            Rank.Rank_1: 11.7,
            Rank.Rank_2: 23.3,
            Rank.Rank_3: 35.0,
            Rank.Rank_4: 46.7,
            Rank.Rank_5: 0.0,
            Rank.Rank_6: 0.0
        },
    ),
    Rare.Star_2: AscnType(
        rare=Rare.Star_2,
        data={
            Rank.Rank_0: 0.0,
            Rank.Rank_1: 11.7,
            Rank.Rank_2: 23.3,
            Rank.Rank_3: 35.0,
            Rank.Rank_4: 46.7,
            Rank.Rank_5: 0.0,
            Rank.Rank_6: 0.0
        },
    ),
    Rare.Star_3: AscnType(
        rare=Rare.Star_3,
        data={
            Rank.Rank_0: 0.0,
            Rank.Rank_1: 19.5,
            Rank.Rank_2: 38.9,
            Rank.Rank_3: 58.4,
            Rank.Rank_4: 77.8,
            Rank.Rank_5: 97.3,
            Rank.Rank_6: 116.7
        },
    ),
    Rare.Star_4: AscnType(
        rare=Rare.Star_4,
        data={
            Rank.Rank_0: 0.0,
            Rank.Rank_1: 25.9,
            Rank.Rank_2: 51.9,
            Rank.Rank_3: 77.8,
            Rank.Rank_4: 103.7,
            Rank.Rank_5: 129.7,
            Rank.Rank_6: 155.6
        },
    ),
    Rare.Star_5: AscnType(
        rare=Rare.Star_5,
        data={
            Rank.Rank_0: 0.0,
            Rank.Rank_1: 31.1,
            Rank.Rank_2: 62.2,
            Rank.Rank_3: 93.4,
            Rank.Rank_4: 124.5,
            Rank.Rank_5: 155.6,
            Rank.Rank_6: 186.7
        }
    ),
}
