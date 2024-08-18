from enum import Enum

__rare__ = {
    "Star 0": 0,
    "Star 1": 1,
    "Star 2": 2,
    "Star 3": 3,
    "Star 4": 4,
    "Star 5": 5,
}


Rare = Enum(
    "Rare",
    {
        item.replace(" ", "_"): data for item, data in __rare__.items()
    }
)
