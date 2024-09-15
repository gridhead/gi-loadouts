from enum import Enum

__tier__ = {
    "Tier 1": {
        "qant": 1,
        "rare": {
            3: 37.6075,
            4: 41.0671,
            5: 44.3358,
        }
    },
    "Tier 2": {
        "qant": 2,
        "rare": {
            1: 23.2450,
            2: 32.9300,
            3: 38.7413,
            4: 42.4010,
            5: 45.9364,
        }
    },
    "Tier 3": {
        "qant": 3,
        "rare": {
            3: 39.8751,
            4: 43.7349,
            5: 47.5370,
        }
    },
    "Tier 4": {
        "qant": 4,
        "rare": {
            4: 45.0687,
            5: 49.1377,
        }
    },
}


Tier = Enum(
    "Tier",
    {
        item.replace(" ", "_"): data for item, data in __tier__.items()
    }
)
