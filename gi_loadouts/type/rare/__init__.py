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


__rarecolour__ = {
    Rare.Star_0: ":rare/imgs/rare/star_1.webp",
    Rare.Star_1: ":rare/imgs/rare/star_1.webp",
    Rare.Star_2: ":rare/imgs/rare/star_2.webp",
    Rare.Star_3: ":rare/imgs/rare/star_3.webp",
    Rare.Star_4: ":rare/imgs/rare/star_4.webp",
    Rare.Star_5: ":rare/imgs/rare/star_5.webp",
}
