from enum import Enum

__rank__ = {
    "Rank 0": 0,
    "Rank 1": 1,
    "Rank 2": 2,
    "Rank 3": 3,
    "Rank 4": 4,
    "Rank 5": 5,
    "Rank 6": 6
}


Rank = Enum(
    "Rank",
    {
        item.replace(" ", "_"): data for item, data in __rank__.items()
    }
)
