from pydantic import BaseModel

from ..rare import Rare
from .tier import Tier


class MultTier(BaseModel):
    """
    Data class for mapping between multiplier and tier
    """
    levl: int
    data: dict


MultSeco = {
    0: 1,
    1: 1,
    5: 1.162,
    10: 1.363,
    15: 1.565,
    20: 1.767,
    25: 1.969,
    30: 2.171,
    35: 2.373,
    40: 2.575,
    45: 2.777,
    50: 2.979,
    55: 3.181,
    60: 3.383,
    65: 3.585,
    70: 3.786,
    75: 3.988,
    80: 4.19,
    85: 4.392,
    90: 4.594
}

Mult = {
    Rare.Star_3: {
        1: MultTier(
            levl=1,
            data={
                Tier.Tier_1: 1,
                Tier.Tier_2: 1,
                Tier.Tier_3: 1,
            }
        ),
        2: MultTier(
            levl=2,
            data={
                Tier.Tier_1: 1.071,
                Tier.Tier_2: 1.076,
                Tier.Tier_3: 1.081,
            }
        ),
        3: MultTier(
            levl=3,
            data={
                Tier.Tier_1: 1.141,
                Tier.Tier_2: 1.152,
                Tier.Tier_3: 1.162,
            }
        ),
        4: MultTier(
            levl=4,
            data={
                Tier.Tier_1: 1.211,
                Tier.Tier_2: 1.228,
                Tier.Tier_3: 1.244,
            }
        ),
        5: MultTier(
            levl=5,
            data={
                Tier.Tier_1: 1.28,
                Tier.Tier_2: 1.303,
                Tier.Tier_3: 1.325,
            }
        ),
        6: MultTier(
            levl=6,
            data={
                Tier.Tier_1: 1.349,
                Tier.Tier_2: 1.379,
                Tier.Tier_3: 1.407,
            }
        ),
        7: MultTier(
            levl=7,
            data={
                Tier.Tier_1: 1.417,
                Tier.Tier_2: 1.454,
                Tier.Tier_3: 1.489,
            }
        ),
        8: MultTier(
            levl=8,
            data={
                Tier.Tier_1: 1.486,
                Tier.Tier_2: 1.529,
                Tier.Tier_3: 1.57,
            }
        ),
        9: MultTier(
            levl=9,
            data={
                Tier.Tier_1: 1.553,
                Tier.Tier_2: 1.604,
                Tier.Tier_3: 1.652,
            }
        ),
        10: MultTier(
            levl=10,
            data={
                Tier.Tier_1: 1.621,
                Tier.Tier_2: 1.679,
                Tier.Tier_3: 1.734,
            }
        ),
        11: MultTier(
            levl=11,
            data={
                Tier.Tier_1: 1.688,
                Tier.Tier_2: 1.754,
                Tier.Tier_3: 1.816,
            }
        ),
        12: MultTier(
            levl=12,
            data={
                Tier.Tier_1: 1.754,
                Tier.Tier_2: 1.828,
                Tier.Tier_3: 1.898,
            }
        ),
        13: MultTier(
            levl=13,
            data={
                Tier.Tier_1: 1.82,
                Tier.Tier_2: 1.903,
                Tier.Tier_3: 1.981,
            }
        ),
        14: MultTier(
            levl=14,
            data={
                Tier.Tier_1: 1.886,
                Tier.Tier_2: 1.977,
                Tier.Tier_3: 2.063,
            }
        ),
        15: MultTier(
            levl=15,
            data={
                Tier.Tier_1: 1.952,
                Tier.Tier_2: 2.051,
                Tier.Tier_3: 2.145,
            }
        ),
        16: MultTier(
            levl=16,
            data={
                Tier.Tier_1: 2.017,
                Tier.Tier_2: 2.125,
                Tier.Tier_3: 2.227,
            }
        ),
        17: MultTier(
            levl=17,
            data={
                Tier.Tier_1: 2.082,
                Tier.Tier_2: 2.199,
                Tier.Tier_3: 2.31,
            }
        ),
        18: MultTier(
            levl=18,
            data={
                Tier.Tier_1: 2.147,
                Tier.Tier_2: 2.273,
                Tier.Tier_3: 2.392,
            }
        ),
        19: MultTier(
            levl=19,
            data={
                Tier.Tier_1: 2.211,
                Tier.Tier_2: 2.347,
                Tier.Tier_3: 2.474,
            }
        ),
        20: MultTier(
            levl=20,
            data={
                Tier.Tier_1: 2.275,
                Tier.Tier_2: 2.42,
                Tier.Tier_3: 2.557,
            }
        ),
        21: MultTier(
            levl=21,
            data={
                Tier.Tier_1: 2.339,
                Tier.Tier_2: 2.493,
                Tier.Tier_3: 2.639,
            }
        ),
        22: MultTier(
            levl=22,
            data={
                Tier.Tier_1: 2.402,
                Tier.Tier_2: 2.567,
                Tier.Tier_3: 2.722,
            }
        ),
        23: MultTier(
            levl=23,
            data={
                Tier.Tier_1: 2.466,
                Tier.Tier_2: 2.64,
                Tier.Tier_3: 2.804,
            }
        ),
        24: MultTier(
            levl=24,
            data={
                Tier.Tier_1: 2.529,
                Tier.Tier_2: 2.713,
                Tier.Tier_3: 2.887,
            }
        ),
        25: MultTier(
            levl=25,
            data={
                Tier.Tier_1: 2.591,
                Tier.Tier_2: 2.786,
                Tier.Tier_3: 2.969,
            }
        ),
        26: MultTier(
            levl=26,
            data={
                Tier.Tier_1: 2.654,
                Tier.Tier_2: 2.859,
                Tier.Tier_3: 3.052,
            }
        ),
        27: MultTier(
            levl=27,
            data={
                Tier.Tier_1: 2.716,
                Tier.Tier_2: 2.931,
                Tier.Tier_3: 3.134,
            }
        ),
        28: MultTier(
            levl=28,
            data={
                Tier.Tier_1: 2.778,
                Tier.Tier_2: 3.004,
                Tier.Tier_3: 3.217,
            }
        ),
        29: MultTier(
            levl=29,
            data={
                Tier.Tier_1: 2.84,
                Tier.Tier_2: 3.076,
                Tier.Tier_3: 3.299,
            }
        ),
        30: MultTier(
            levl=30,
            data={
                Tier.Tier_1: 2.901,
                Tier.Tier_2: 3.148,
                Tier.Tier_3: 3.382,
            }
        ),
        31: MultTier(
            levl=31,
            data={
                Tier.Tier_1: 2.962,
                Tier.Tier_2: 3.221,
                Tier.Tier_3: 3.464,
            }
        ),
        32: MultTier(
            levl=32,
            data={
                Tier.Tier_1: 3.023,
                Tier.Tier_2: 3.293,
                Tier.Tier_3: 3.547,
            }
        ),
        33: MultTier(
            levl=33,
            data={
                Tier.Tier_1: 3.084,
                Tier.Tier_2: 3.365,
                Tier.Tier_3: 3.629,
            }
        ),
        34: MultTier(
            levl=34,
            data={
                Tier.Tier_1: 3.145,
                Tier.Tier_2: 3.437,
                Tier.Tier_3: 3.712,
            }
        ),
        35: MultTier(
            levl=35,
            data={
                Tier.Tier_1: 3.205,
                Tier.Tier_2: 3.508,
                Tier.Tier_3: 3.794,
            }
        ),
        36: MultTier(
            levl=36,
            data={
                Tier.Tier_1: 3.265,
                Tier.Tier_2: 3.58,
                Tier.Tier_3: 3.877,
            }
        ),
        37: MultTier(
            levl=37,
            data={
                Tier.Tier_1: 3.325,
                Tier.Tier_2: 3.652,
                Tier.Tier_3: 3.959,
            }
        ),
        38: MultTier(
            levl=38,
            data={
                Tier.Tier_1: 3.385,
                Tier.Tier_2: 3.723,
                Tier.Tier_3: 4.042,
            }
        ),
        39: MultTier(
            levl=39,
            data={
                Tier.Tier_1: 3.445,
                Tier.Tier_2: 3.794,
                Tier.Tier_3: 4.124,
            }
        ),
        40: MultTier(
            levl=40,
            data={
                Tier.Tier_1: 3.504,
                Tier.Tier_2: 3.866,
                Tier.Tier_3: 4.206,
            }
        ),
        41: MultTier(
            levl=41,
            data={
                Tier.Tier_1: 3.564,
                Tier.Tier_2: 3.937,
                Tier.Tier_3: 4.289,
            }
        ),
        42: MultTier(
            levl=42,
            data={
                Tier.Tier_1: 3.623,
                Tier.Tier_2: 4.008,
                Tier.Tier_3: 4.371,
            }
        ),
        43: MultTier(
            levl=43,
            data={
                Tier.Tier_1: 3.682,
                Tier.Tier_2: 4.079,
                Tier.Tier_3: 4.454,
            }
        ),
        44: MultTier(
            levl=44,
            data={
                Tier.Tier_1: 3.741,
                Tier.Tier_2: 4.15,
                Tier.Tier_3: 4.536,
            }
        ),
        45: MultTier(
            levl=45,
            data={
                Tier.Tier_1: 3.799,
                Tier.Tier_2: 4.221,
                Tier.Tier_3: 4.618,
            }
        ),
        46: MultTier(
            levl=46,
            data={
                Tier.Tier_1: 3.858,
                Tier.Tier_2: 4.291,
                Tier.Tier_3: 4.701,
            }
        ),
        47: MultTier(
            levl=47,
            data={
                Tier.Tier_1: 3.916,
                Tier.Tier_2: 4.362,
                Tier.Tier_3: 4.783,
            }
        ),
        48: MultTier(
            levl=48,
            data={
                Tier.Tier_1: 3.974,
                Tier.Tier_2: 4.433,
                Tier.Tier_3: 4.865,
            }
        ),
        49: MultTier(
            levl=49,
            data={
                Tier.Tier_1: 4.032,
                Tier.Tier_2: 4.503,
                Tier.Tier_3: 4.948,
            }
        ),
        50: MultTier(
            levl=50,
            data={
                Tier.Tier_1: 4.09,
                Tier.Tier_2: 4.574,
                Tier.Tier_3: 5.03,
            }
        ),
        51: MultTier(
            levl=51,
            data={
                Tier.Tier_1: 4.148,
                Tier.Tier_2: 4.644,
                Tier.Tier_3: 5.112,
            }
        ),
        52: MultTier(
            levl=52,
            data={
                Tier.Tier_1: 4.205,
                Tier.Tier_2: 4.714,
                Tier.Tier_3: 5.194,
            }
        ),
        53: MultTier(
            levl=53,
            data={
                Tier.Tier_1: 4.263,
                Tier.Tier_2: 4.784,
                Tier.Tier_3: 5.277,
            }
        ),
        54: MultTier(
            levl=54,
            data={
                Tier.Tier_1: 4.32,
                Tier.Tier_2: 4.855,
                Tier.Tier_3: 5.359,
            }
        ),
        55: MultTier(
            levl=55,
            data={
                Tier.Tier_1: 4.377,
                Tier.Tier_2: 4.925,
                Tier.Tier_3: 5.441,
            }
        ),
        56: MultTier(
            levl=56,
            data={
                Tier.Tier_1: 4.434,
                Tier.Tier_2: 4.995,
                Tier.Tier_3: 5.523,
            }
        ),
        57: MultTier(
            levl=57,
            data={
                Tier.Tier_1: 4.491,
                Tier.Tier_2: 5.065,
                Tier.Tier_3: 5.605,
            }
        ),
        58: MultTier(
            levl=58,
            data={
                Tier.Tier_1: 4.548,
                Tier.Tier_2: 5.134,
                Tier.Tier_3: 5.688,
            }
        ),
        59: MultTier(
            levl=59,
            data={
                Tier.Tier_1: 4.605,
                Tier.Tier_2: 5.204,
                Tier.Tier_3: 5.77,
            }
        ),
        60: MultTier(
            levl=60,
            data={
                Tier.Tier_1: 4.661,
                Tier.Tier_2: 5.274,
                Tier.Tier_3: 5.852,
            }
        ),
        61: MultTier(
            levl=61,
            data={
                Tier.Tier_1: 4.718,
                Tier.Tier_2: 5.344,
                Tier.Tier_3: 5.934,
            }
        ),
        62: MultTier(
            levl=62,
            data={
                Tier.Tier_1: 4.774,
                Tier.Tier_2: 5.413,
                Tier.Tier_3: 6.016,
            }
        ),
        63: MultTier(
            levl=63,
            data={
                Tier.Tier_1: 4.83,
                Tier.Tier_2: 5.483,
                Tier.Tier_3: 6.098,
            }
        ),
        64: MultTier(
            levl=64,
            data={
                Tier.Tier_1: 4.887,
                Tier.Tier_2: 5.552,
                Tier.Tier_3: 6.18,
            }
        ),
        65: MultTier(
            levl=65,
            data={
                Tier.Tier_1: 4.943,
                Tier.Tier_2: 5.622,
                Tier.Tier_3: 6.262,
            }
        ),
        66: MultTier(
            levl=66,
            data={
                Tier.Tier_1: 4.999,
                Tier.Tier_2: 5.691,
                Tier.Tier_3: 6.344,
            }
        ),
        67: MultTier(
            levl=67,
            data={
                Tier.Tier_1: 5.054,
                Tier.Tier_2: 5.761,
                Tier.Tier_3: 6.427,
            }
        ),
        68: MultTier(
            levl=68,
            data={
                Tier.Tier_1: 5.11,
                Tier.Tier_2: 5.83,
                Tier.Tier_3: 6.509,
            }
        ),
        69: MultTier(
            levl=69,
            data={
                Tier.Tier_1: 5.166,
                Tier.Tier_2: 5.899,
                Tier.Tier_3: 6.591,
            }
        ),
        70: MultTier(
            levl=70,
            data={
                Tier.Tier_1: 5.222,
                Tier.Tier_2: 5.968,
                Tier.Tier_3: 6.673,
            }
        ),
        71: MultTier(
            levl=71,
            data={
                Tier.Tier_1: 5.277,
                Tier.Tier_2: 6.038,
                Tier.Tier_3: 6.755,
            }
        ),
        72: MultTier(
            levl=72,
            data={
                Tier.Tier_1: 5.333,
                Tier.Tier_2: 6.107,
                Tier.Tier_3: 6.837,
            }
        ),
        73: MultTier(
            levl=73,
            data={
                Tier.Tier_1: 5.388,
                Tier.Tier_2: 6.176,
                Tier.Tier_3: 6.919,
            }
        ),
        74: MultTier(
            levl=74,
            data={
                Tier.Tier_1: 5.443,
                Tier.Tier_2: 6.245,
                Tier.Tier_3: 7.001,
            }
        ),
        75: MultTier(
            levl=75,
            data={
                Tier.Tier_1: 5.498,
                Tier.Tier_2: 6.314,
                Tier.Tier_3: 7.083,
            }
        ),
        76: MultTier(
            levl=76,
            data={
                Tier.Tier_1: 5.554,
                Tier.Tier_2: 6.383,
                Tier.Tier_3: 7.165,
            }
        ),
        77: MultTier(
            levl=77,
            data={
                Tier.Tier_1: 5.609,
                Tier.Tier_2: 6.452,
                Tier.Tier_3: 7.247,
            }
        ),
        78: MultTier(
            levl=78,
            data={
                Tier.Tier_1: 5.664,
                Tier.Tier_2: 6.521,
                Tier.Tier_3: 7.329,
            }
        ),
        79: MultTier(
            levl=79,
            data={
                Tier.Tier_1: 5.719,
                Tier.Tier_2: 6.59,
                Tier.Tier_3: 7.411,
            }
        ),
        80: MultTier(
            levl=80,
            data={
                Tier.Tier_1: 5.774,
                Tier.Tier_2: 6.659,
                Tier.Tier_3: 7.493,
            }
        ),
        81: MultTier(
            levl=81,
            data={
                Tier.Tier_1: 5.828,
                Tier.Tier_2: 6.727,
                Tier.Tier_3: 7.575,
            }
        ),
        82: MultTier(
            levl=82,
            data={
                Tier.Tier_1: 5.883,
                Tier.Tier_2: 6.796,
                Tier.Tier_3: 7.657,
            }
        ),
        83: MultTier(
            levl=83,
            data={
                Tier.Tier_1: 5.938,
                Tier.Tier_2: 6.865,
                Tier.Tier_3: 7.739,
            }
        ),
        84: MultTier(
            levl=84,
            data={
                Tier.Tier_1: 5.993,
                Tier.Tier_2: 6.934,
                Tier.Tier_3: 7.821,
            }
        ),
        85: MultTier(
            levl=85,
            data={
                Tier.Tier_1: 6.047,
                Tier.Tier_2: 7.003,
                Tier.Tier_3: 7.904,
            }
        ),
        86: MultTier(
            levl=86,
            data={
                Tier.Tier_1: 6.102,
                Tier.Tier_2: 7.071,
                Tier.Tier_3: 7.986,
            }
        ),
        87: MultTier(
            levl=87,
            data={
                Tier.Tier_1: 6.156,
                Tier.Tier_2: 7.14,
                Tier.Tier_3: 8.068,
            }
        ),
        88: MultTier(
            levl=88,
            data={
                Tier.Tier_1: 6.211,
                Tier.Tier_2: 7.209,
                Tier.Tier_3: 8.15,
            }
        ),
        89: MultTier(
            levl=89,
            data={
                Tier.Tier_1: 6.265,
                Tier.Tier_2: 7.277,
                Tier.Tier_3: 8.232,
            }
        ),
        90: MultTier(
            levl=90,
            data={
                Tier.Tier_1: 6.32,
                Tier.Tier_2: 7.346,
                Tier.Tier_3: 8.314,
            }
        ),
    },
    Rare.Star_4: {
        1: MultTier(
            levl=1,
            data={
                Tier.Tier_1: 1,
                Tier.Tier_2: 1,
                Tier.Tier_3: 1,
                Tier.Tier_4: 1,
            }
        ),
        2: MultTier(
            levl=2,
            data={
                Tier.Tier_1: 1.077,
                Tier.Tier_2: 1.083,
                Tier.Tier_3: 1.088,
                Tier.Tier_4: 1.093,
            }
        ),
        3: MultTier(
            levl=3,
            data={
                Tier.Tier_1: 1.154,
                Tier.Tier_2: 1.165,
                Tier.Tier_3: 1.176,
                Tier.Tier_4: 1.186,
            }
        ),
        4: MultTier(
            levl=4,
            data={
                Tier.Tier_1: 1.23,
                Tier.Tier_2: 1.248,
                Tier.Tier_3: 1.264,
                Tier.Tier_4: 1.28,
            }
        ),
        5: MultTier(
            levl=5,
            data={
                Tier.Tier_1: 1.306,
                Tier.Tier_2: 1.33,
                Tier.Tier_3: 1.353,
                Tier.Tier_4: 1.374,
            }
        ),
        6: MultTier(
            levl=6,
            data={
                Tier.Tier_1: 1.382,
                Tier.Tier_2: 1.413,
                Tier.Tier_3: 1.442,
                Tier.Tier_4: 1.469,
            }
        ),
        7: MultTier(
            levl=7,
            data={
                Tier.Tier_1: 1.457,
                Tier.Tier_2: 1.495,
                Tier.Tier_3: 1.531,
                Tier.Tier_4: 1.565,
            }
        ),
        8: MultTier(
            levl=8,
            data={
                Tier.Tier_1: 1.533,
                Tier.Tier_2: 1.578,
                Tier.Tier_3: 1.621,
                Tier.Tier_4: 1.661,
            }
        ),
        9: MultTier(
            levl=9,
            data={
                Tier.Tier_1: 1.607,
                Tier.Tier_2: 1.661,
                Tier.Tier_3: 1.71,
                Tier.Tier_4: 1.757,
            }
        ),
        10: MultTier(
            levl=10,
            data={
                Tier.Tier_1: 1.682,
                Tier.Tier_2: 1.743,
                Tier.Tier_3: 1.8,
                Tier.Tier_4: 1.854,
            }
        ),
        11: MultTier(
            levl=11,
            data={
                Tier.Tier_1: 1.757,
                Tier.Tier_2: 1.826,
                Tier.Tier_3: 1.891,
                Tier.Tier_4: 1.952,
            }
        ),
        12: MultTier(
            levl=12,
            data={
                Tier.Tier_1: 1.831,
                Tier.Tier_2: 1.908,
                Tier.Tier_3: 1.981,
                Tier.Tier_4: 2.049,
            }
        ),
        13: MultTier(
            levl=13,
            data={
                Tier.Tier_1: 1.905,
                Tier.Tier_2: 1.991,
                Tier.Tier_3: 2.072,
                Tier.Tier_4: 2.147,
            }
        ),
        14: MultTier(
            levl=14,
            data={
                Tier.Tier_1: 1.979,
                Tier.Tier_2: 2.073,
                Tier.Tier_3: 2.162,
                Tier.Tier_4: 2.246,
            }
        ),
        15: MultTier(
            levl=15,
            data={
                Tier.Tier_1: 2.052,
                Tier.Tier_2: 2.156,
                Tier.Tier_3: 2.253,
                Tier.Tier_4: 2.345,
            }
        ),
        16: MultTier(
            levl=16,
            data={
                Tier.Tier_1: 2.126,
                Tier.Tier_2: 2.239,
                Tier.Tier_3: 2.345,
                Tier.Tier_4: 2.444,
            }
        ),
        17: MultTier(
            levl=17,
            data={
                Tier.Tier_1: 2.199,
                Tier.Tier_2: 2.321,
                Tier.Tier_3: 2.436,
                Tier.Tier_4: 2.544,
            }
        ),
        18: MultTier(
            levl=18,
            data={
                Tier.Tier_1: 2.272,
                Tier.Tier_2: 2.404,
                Tier.Tier_3: 2.527,
                Tier.Tier_4: 2.644,
            }
        ),
        19: MultTier(
            levl=19,
            data={
                Tier.Tier_1: 2.345,
                Tier.Tier_2: 2.486,
                Tier.Tier_3: 2.619,
                Tier.Tier_4: 2.744,
            }
        ),
        20: MultTier(
            levl=20,
            data={
                Tier.Tier_1: 2.417,
                Tier.Tier_2: 2.569,
                Tier.Tier_3: 2.711,
                Tier.Tier_4: 2.845,
            }
        ),
        21: MultTier(
            levl=21,
            data={
                Tier.Tier_1: 2.49,
                Tier.Tier_2: 2.651,
                Tier.Tier_3: 2.803,
                Tier.Tier_4: 2.946,
            }
        ),
        22: MultTier(
            levl=22,
            data={
                Tier.Tier_1: 2.562,
                Tier.Tier_2: 2.734,
                Tier.Tier_3: 2.895,
                Tier.Tier_4: 3.047,
            }
        ),
        23: MultTier(
            levl=23,
            data={
                Tier.Tier_1: 2.634,
                Tier.Tier_2: 2.817,
                Tier.Tier_3: 2.987,
                Tier.Tier_4: 3.148,
            }
        ),
        24: MultTier(
            levl=24,
            data={
                Tier.Tier_1: 2.707,
                Tier.Tier_2: 2.899,
                Tier.Tier_3: 3.08,
                Tier.Tier_4: 3.25,
            }
        ),
        25: MultTier(
            levl=25,
            data={
                Tier.Tier_1: 2.778,
                Tier.Tier_2: 2.982,
                Tier.Tier_3: 3.172,
                Tier.Tier_4: 3.352,
            }
        ),
        26: MultTier(
            levl=26,
            data={
                Tier.Tier_1: 2.85,
                Tier.Tier_2: 3.064,
                Tier.Tier_3: 3.265,
                Tier.Tier_4: 3.454,
            }
        ),
        27: MultTier(
            levl=27,
            data={
                Tier.Tier_1: 2.922,
                Tier.Tier_2: 3.147,
                Tier.Tier_3: 3.358,
                Tier.Tier_4: 3.557,
            }
        ),
        28: MultTier(
            levl=28,
            data={
                Tier.Tier_1: 2.993,
                Tier.Tier_2: 3.229,
                Tier.Tier_3: 3.451,
                Tier.Tier_4: 3.66,
            }
        ),
        29: MultTier(
            levl=29,
            data={
                Tier.Tier_1: 3.065,
                Tier.Tier_2: 3.312,
                Tier.Tier_3: 3.544,
                Tier.Tier_4: 3.762,
            }
        ),
        30: MultTier(
            levl=30,
            data={
                Tier.Tier_1: 3.136,
                Tier.Tier_2: 3.394,
                Tier.Tier_3: 3.637,
                Tier.Tier_4: 3.866,
            }
        ),
        31: MultTier(
            levl=31,
            data={
                Tier.Tier_1: 3.207,
                Tier.Tier_2: 3.477,
                Tier.Tier_3: 3.731,
                Tier.Tier_4: 3.969,
            }
        ),
        32: MultTier(
            levl=32,
            data={
                Tier.Tier_1: 3.278,
                Tier.Tier_2: 3.56,
                Tier.Tier_3: 3.824,
                Tier.Tier_4: 4.073,
            }
        ),
        33: MultTier(
            levl=33,
            data={
                Tier.Tier_1: 3.349,
                Tier.Tier_2: 3.642,
                Tier.Tier_3: 3.918,
                Tier.Tier_4: 4.177,
            }
        ),
        34: MultTier(
            levl=34,
            data={
                Tier.Tier_1: 3.42,
                Tier.Tier_2: 3.725,
                Tier.Tier_3: 4.011,
                Tier.Tier_4: 4.281,
            }
        ),
        35: MultTier(
            levl=35,
            data={
                Tier.Tier_1: 3.49,
                Tier.Tier_2: 3.807,
                Tier.Tier_3: 4.105,
                Tier.Tier_4: 4.385,
            }
        ),
        36: MultTier(
            levl=36,
            data={
                Tier.Tier_1: 3.561,
                Tier.Tier_2: 3.89,
                Tier.Tier_3: 4.199,
                Tier.Tier_4: 4.489,
            }
        ),
        37: MultTier(
            levl=37,
            data={
                Tier.Tier_1: 3.632,
                Tier.Tier_2: 3.972,
                Tier.Tier_3: 4.293,
                Tier.Tier_4: 4.594,
            }
        ),
        38: MultTier(
            levl=38,
            data={
                Tier.Tier_1: 3.702,
                Tier.Tier_2: 4.055,
                Tier.Tier_3: 4.387,
                Tier.Tier_4: 4.699,
            }
        ),
        39: MultTier(
            levl=39,
            data={
                Tier.Tier_1: 3.772,
                Tier.Tier_2: 4.138,
                Tier.Tier_3: 4.481,
                Tier.Tier_4: 4.803,
            }
        ),
        40: MultTier(
            levl=40,
            data={
                Tier.Tier_1: 3.842,
                Tier.Tier_2: 4.22,
                Tier.Tier_3: 4.575,
                Tier.Tier_4: 4.909,
            }
        ),
        41: MultTier(
            levl=41,
            data={
                Tier.Tier_1: 3.913,
                Tier.Tier_2: 4.303,
                Tier.Tier_3: 4.669,
                Tier.Tier_4: 5.014,
            }
        ),
        42: MultTier(
            levl=42,
            data={
                Tier.Tier_1: 3.983,
                Tier.Tier_2: 4.385,
                Tier.Tier_3: 4.763,
                Tier.Tier_4: 5.119,
            }
        ),
        43: MultTier(
            levl=43,
            data={
                Tier.Tier_1: 4.053,
                Tier.Tier_2: 4.468,
                Tier.Tier_3: 4.858,
                Tier.Tier_4: 5.225,
            }
        ),
        44: MultTier(
            levl=44,
            data={
                Tier.Tier_1: 4.122,
                Tier.Tier_2: 4.55,
                Tier.Tier_3: 4.952,
                Tier.Tier_4: 5.33,
            }
        ),
        45: MultTier(
            levl=45,
            data={
                Tier.Tier_1: 4.192,
                Tier.Tier_2: 4.633,
                Tier.Tier_3: 5.047,
                Tier.Tier_4: 5.436,
            }
        ),
        46: MultTier(
            levl=46,
            data={
                Tier.Tier_1: 4.262,
                Tier.Tier_2: 4.716,
                Tier.Tier_3: 5.142,
                Tier.Tier_4: 5.542,
            }
        ),
        47: MultTier(
            levl=47,
            data={
                Tier.Tier_1: 4.332,
                Tier.Tier_2: 4.798,
                Tier.Tier_3: 5.236,
                Tier.Tier_4: 5.648,
            }
        ),
        48: MultTier(
            levl=48,
            data={
                Tier.Tier_1: 4.401,
                Tier.Tier_2: 4.881,
                Tier.Tier_3: 5.331,
                Tier.Tier_4: 5.755,
            }
        ),
        49: MultTier(
            levl=49,
            data={
                Tier.Tier_1: 4.471,
                Tier.Tier_2: 4.963,
                Tier.Tier_3: 5.426,
                Tier.Tier_4: 5.861,
            }
        ),
        50: MultTier(
            levl=50,
            data={
                Tier.Tier_1: 4.54,
                Tier.Tier_2: 5.046,
                Tier.Tier_3: 5.521,
                Tier.Tier_4: 5.968,
            }
        ),
        51: MultTier(
            levl=51,
            data={
                Tier.Tier_1: 4.609,
                Tier.Tier_2: 5.128,
                Tier.Tier_3: 5.616,
                Tier.Tier_4: 6.074,
            }
        ),
        52: MultTier(
            levl=52,
            data={
                Tier.Tier_1: 4.679,
                Tier.Tier_2: 5.211,
                Tier.Tier_3: 5.711,
                Tier.Tier_4: 6.181,
            }
        ),
        53: MultTier(
            levl=53,
            data={
                Tier.Tier_1: 4.748,
                Tier.Tier_2: 5.294,
                Tier.Tier_3: 5.806,
                Tier.Tier_4: 6.288,
            }
        ),
        54: MultTier(
            levl=54,
            data={
                Tier.Tier_1: 4.817,
                Tier.Tier_2: 5.376,
                Tier.Tier_3: 5.901,
                Tier.Tier_4: 6.395,
            }
        ),
        55: MultTier(
            levl=55,
            data={
                Tier.Tier_1: 4.886,
                Tier.Tier_2: 5.459,
                Tier.Tier_3: 5.996,
                Tier.Tier_4: 6.502,
            }
        ),
        56: MultTier(
            levl=56,
            data={
                Tier.Tier_1: 4.955,
                Tier.Tier_2: 5.541,
                Tier.Tier_3: 6.092,
                Tier.Tier_4: 6.609,
            }
        ),
        57: MultTier(
            levl=57,
            data={
                Tier.Tier_1: 5.024,
                Tier.Tier_2: 5.624,
                Tier.Tier_3: 6.187,
                Tier.Tier_4: 6.717,
            }
        ),
        58: MultTier(
            levl=58,
            data={
                Tier.Tier_1: 5.093,
                Tier.Tier_2: 5.706,
                Tier.Tier_3: 6.282,
                Tier.Tier_4: 6.824,
            }
        ),
        59: MultTier(
            levl=59,
            data={
                Tier.Tier_1: 5.162,
                Tier.Tier_2: 5.789,
                Tier.Tier_3: 6.378,
                Tier.Tier_4: 6.932,
            }
        ),
        60: MultTier(
            levl=60,
            data={
                Tier.Tier_1: 5.231,
                Tier.Tier_2: 5.872,
                Tier.Tier_3: 6.473,
                Tier.Tier_4: 7.039,
            }
        ),
        61: MultTier(
            levl=61,
            data={
                Tier.Tier_1: 5.3,
                Tier.Tier_2: 5.954,
                Tier.Tier_3: 6.569,
                Tier.Tier_4: 7.147,
            }
        ),
        62: MultTier(
            levl=62,
            data={
                Tier.Tier_1: 5.368,
                Tier.Tier_2: 6.037,
                Tier.Tier_3: 6.664,
                Tier.Tier_4: 7.255,
            }
        ),
        63: MultTier(
            levl=63,
            data={
                Tier.Tier_1: 5.437,
                Tier.Tier_2: 6.119,
                Tier.Tier_3: 6.76,
                Tier.Tier_4: 7.363,
            }
        ),
        64: MultTier(
            levl=64,
            data={
                Tier.Tier_1: 5.506,
                Tier.Tier_2: 6.202,
                Tier.Tier_3: 6.856,
                Tier.Tier_4: 7.471,
            }
        ),
        65: MultTier(
            levl=65,
            data={
                Tier.Tier_1: 5.574,
                Tier.Tier_2: 6.284,
                Tier.Tier_3: 6.951,
                Tier.Tier_4: 7.579,
            }
        ),
        66: MultTier(
            levl=66,
            data={
                Tier.Tier_1: 5.643,
                Tier.Tier_2: 6.367,
                Tier.Tier_3: 7.047,
                Tier.Tier_4: 7.687,
            }
        ),
        67: MultTier(
            levl=67,
            data={
                Tier.Tier_1: 5.711,
                Tier.Tier_2: 6.45,
                Tier.Tier_3: 7.143,
                Tier.Tier_4: 7.795,
            }
        ),
        68: MultTier(
            levl=68,
            data={
                Tier.Tier_1: 5.78,
                Tier.Tier_2: 6.532,
                Tier.Tier_3: 7.239,
                Tier.Tier_4: 7.904,
            }
        ),
        69: MultTier(
            levl=69,
            data={
                Tier.Tier_1: 5.848,
                Tier.Tier_2: 6.615,
                Tier.Tier_3: 7.335,
                Tier.Tier_4: 8.012,
            }
        ),
        70: MultTier(
            levl=70,
            data={
                Tier.Tier_1: 5.916,
                Tier.Tier_2: 6.697,
                Tier.Tier_3: 7.431,
                Tier.Tier_4: 8.12,
            }
        ),
        71: MultTier(
            levl=71,
            data={
                Tier.Tier_1: 5.985,
                Tier.Tier_2: 6.78,
                Tier.Tier_3: 7.527,
                Tier.Tier_4: 8.229,
            }
        ),
        72: MultTier(
            levl=72,
            data={
                Tier.Tier_1: 6.053,
                Tier.Tier_2: 6.862,
                Tier.Tier_3: 7.623,
                Tier.Tier_4: 8.338,
            }
        ),
        73: MultTier(
            levl=73,
            data={
                Tier.Tier_1: 6.121,
                Tier.Tier_2: 6.945,
                Tier.Tier_3: 7.719,
                Tier.Tier_4: 8.446,
            }
        ),
        74: MultTier(
            levl=74,
            data={
                Tier.Tier_1: 6.189,
                Tier.Tier_2: 7.028,
                Tier.Tier_3: 7.815,
                Tier.Tier_4: 8.555,
            }
        ),
        75: MultTier(
            levl=75,
            data={
                Tier.Tier_1: 6.257,
                Tier.Tier_2: 7.11,
                Tier.Tier_3: 7.911,
                Tier.Tier_4: 8.664,
            }
        ),
        76: MultTier(
            levl=76,
            data={
                Tier.Tier_1: 6.326,
                Tier.Tier_2: 7.193,
                Tier.Tier_3: 8.007,
                Tier.Tier_4: 8.773,
            }
        ),
        77: MultTier(
            levl=77,
            data={
                Tier.Tier_1: 6.394,
                Tier.Tier_2: 7.275,
                Tier.Tier_3: 8.103,
                Tier.Tier_4: 8.882,
            }
        ),
        78: MultTier(
            levl=78,
            data={
                Tier.Tier_1: 6.462,
                Tier.Tier_2: 7.358,
                Tier.Tier_3: 8.199,
                Tier.Tier_4: 8.991,
            }
        ),
        79: MultTier(
            levl=79,
            data={
                Tier.Tier_1: 6.53,
                Tier.Tier_2: 7.44,
                Tier.Tier_3: 8.296,
                Tier.Tier_4: 9.1,
            }
        ),
        80: MultTier(
            levl=80,
            data={
                Tier.Tier_1: 6.598,
                Tier.Tier_2: 7.523,
                Tier.Tier_3: 8.392,
                Tier.Tier_4: 9.209,
            }
        ),
        81: MultTier(
            levl=81,
            data={
                Tier.Tier_1: 6.665,
                Tier.Tier_2: 7.606,
                Tier.Tier_3: 8.488,
                Tier.Tier_4: 9.319,
            }
        ),
        82: MultTier(
            levl=82,
            data={
                Tier.Tier_1: 6.733,
                Tier.Tier_2: 7.688,
                Tier.Tier_3: 8.585,
                Tier.Tier_4: 9.428,
            }
        ),
        83: MultTier(
            levl=83,
            data={
                Tier.Tier_1: 6.801,
                Tier.Tier_2: 7.771,
                Tier.Tier_3: 8.681,
                Tier.Tier_4: 9.537,
            }
        ),
        84: MultTier(
            levl=84,
            data={
                Tier.Tier_1: 6.869,
                Tier.Tier_2: 7.853,
                Tier.Tier_3: 8.777,
                Tier.Tier_4: 9.647,
            }
        ),
        85: MultTier(
            levl=85,
            data={
                Tier.Tier_1: 6.937,
                Tier.Tier_2: 7.936,
                Tier.Tier_3: 8.874,
                Tier.Tier_4: 9.756,
            }
        ),
        86: MultTier(
            levl=86,
            data={
                Tier.Tier_1: 7.005,
                Tier.Tier_2: 8.018,
                Tier.Tier_3: 8.97,
                Tier.Tier_4: 9.866,
            }
        ),
        87: MultTier(
            levl=87,
            data={
                Tier.Tier_1: 7.072,
                Tier.Tier_2: 8.101,
                Tier.Tier_3: 9.067,
                Tier.Tier_4: 9.975,
            }
        ),
        88: MultTier(
            levl=88,
            data={
                Tier.Tier_1: 7.14,
                Tier.Tier_2: 8.183,
                Tier.Tier_3: 9.163,
                Tier.Tier_4: 10.085,
            }
        ),
        89: MultTier(
            levl=89,
            data={
                Tier.Tier_1: 7.208,
                Tier.Tier_2: 8.266,
                Tier.Tier_3: 9.26,
                Tier.Tier_4: 10.195,
            }
        ),
        90: MultTier(
            levl=90,
            data={
                Tier.Tier_1: 7.275,
                Tier.Tier_2: 8.349,
                Tier.Tier_3: 9.356,
                Tier.Tier_4: 10.305,
            }
        ),
    },
    Rare.Star_5: {
        1: MultTier(
            levl=1,
            data={
                Tier.Tier_1: 1,
                Tier.Tier_2: 1,
                Tier.Tier_3: 1,
                Tier.Tier_4: 1,
            }
        ),
        2: MultTier(
            levl=2,
            data={
                Tier.Tier_1: 1.079,
                Tier.Tier_2: 1.086,
                Tier.Tier_3: 1.091,
                Tier.Tier_4: 1.097,
            }
        ),
        3: MultTier(
            levl=3,
            data={
                Tier.Tier_1: 1.159,
                Tier.Tier_2: 1.171,
                Tier.Tier_3: 1.183,
                Tier.Tier_4: 1.194,
            }
        ),
        4: MultTier(
            levl=4,
            data={
                Tier.Tier_1: 1.238,
                Tier.Tier_2: 1.257,
                Tier.Tier_3: 1.275,
                Tier.Tier_4: 1.292,
            }
        ),
        5: MultTier(
            levl=5,
            data={
                Tier.Tier_1: 1.317,
                Tier.Tier_2: 1.343,
                Tier.Tier_3: 1.368,
                Tier.Tier_4: 1.391,
            }
        ),
        6: MultTier(
            levl=6,
            data={
                Tier.Tier_1: 1.395,
                Tier.Tier_2: 1.429,
                Tier.Tier_3: 1.461,
                Tier.Tier_4: 1.49,
            }
        ),
        7: MultTier(
            levl=7,
            data={
                Tier.Tier_1: 1.474,
                Tier.Tier_2: 1.516,
                Tier.Tier_3: 1.554,
                Tier.Tier_4: 1.59,
            }
        ),
        8: MultTier(
            levl=8,
            data={
                Tier.Tier_1: 1.552,
                Tier.Tier_2: 1.602,
                Tier.Tier_3: 1.648,
                Tier.Tier_4: 1.692,
            }
        ),
        9: MultTier(
            levl=9,
            data={
                Tier.Tier_1: 1.631,
                Tier.Tier_2: 1.689,
                Tier.Tier_3: 1.743,
                Tier.Tier_4: 1.792,
            }
        ),
        10: MultTier(
            levl=10,
            data={
                Tier.Tier_1: 1.709,
                Tier.Tier_2: 1.775,
                Tier.Tier_3: 1.837,
                Tier.Tier_4: 1.895,
            }
        ),
        11: MultTier(
            levl=11,
            data={
                Tier.Tier_1: 1.787,
                Tier.Tier_2: 1.862,
                Tier.Tier_3: 1.933,
                Tier.Tier_4: 1.998,
            }
        ),
        12: MultTier(
            levl=12,
            data={
                Tier.Tier_1: 1.865,
                Tier.Tier_2: 1.949,
                Tier.Tier_3: 2.028,
                Tier.Tier_4: 2.102,
            }
        ),
        13: MultTier(
            levl=13,
            data={
                Tier.Tier_1: 1.942,
                Tier.Tier_2: 2.036,
                Tier.Tier_3: 2.124,
                Tier.Tier_4: 2.206,
            }
        ),
        14: MultTier(
            levl=14,
            data={
                Tier.Tier_1: 2.02,
                Tier.Tier_2: 2.124,
                Tier.Tier_3: 2.22,
                Tier.Tier_4: 2.31,
            }
        ),
        15: MultTier(
            levl=15,
            data={
                Tier.Tier_1: 2.098,
                Tier.Tier_2: 2.211,
                Tier.Tier_3: 2.317,
                Tier.Tier_4: 2.415,
            }
        ),
        16: MultTier(
            levl=16,
            data={
                Tier.Tier_1: 2.175,
                Tier.Tier_2: 2.299,
                Tier.Tier_3: 2.414,
                Tier.Tier_4: 2.521,
            }
        ),
        17: MultTier(
            levl=17,
            data={
                Tier.Tier_1: 2.253,
                Tier.Tier_2: 2.386,
                Tier.Tier_3: 2.511,
                Tier.Tier_4: 2.627,
            }
        ),
        18: MultTier(
            levl=18,
            data={
                Tier.Tier_1: 2.33,
                Tier.Tier_2: 2.474,
                Tier.Tier_3: 2.608,
                Tier.Tier_4: 2.733,
            }
        ),
        19: MultTier(
            levl=19,
            data={
                Tier.Tier_1: 2.408,
                Tier.Tier_2: 2.562,
                Tier.Tier_3: 2.706,
                Tier.Tier_4: 2.841,
            }
        ),
        20: MultTier(
            levl=20,
            data={
                Tier.Tier_1: 2.485,
                Tier.Tier_2: 2.65,
                Tier.Tier_3: 2.804,
                Tier.Tier_4: 2.949,
            }
        ),
        21: MultTier(
            levl=21,
            data={
                Tier.Tier_1: 2.562,
                Tier.Tier_2: 2.738,
                Tier.Tier_3: 2.903,
                Tier.Tier_4: 3.057,
            }
        ),
        22: MultTier(
            levl=22,
            data={
                Tier.Tier_1: 2.639,
                Tier.Tier_2: 2.827,
                Tier.Tier_3: 3.002,
                Tier.Tier_4: 3.165,
            }
        ),
        23: MultTier(
            levl=23,
            data={
                Tier.Tier_1: 2.717,
                Tier.Tier_2: 2.915,
                Tier.Tier_3: 3.101,
                Tier.Tier_4: 3.274,
            }
        ),
        24: MultTier(
            levl=24,
            data={
                Tier.Tier_1: 2.794,
                Tier.Tier_2: 3.004,
                Tier.Tier_3: 3.2,
                Tier.Tier_4: 3.384,
            }
        ),
        25: MultTier(
            levl=25,
            data={
                Tier.Tier_1: 2.871,
                Tier.Tier_2: 3.093,
                Tier.Tier_3: 3.3,
                Tier.Tier_4: 3.493,
            }
        ),
        26: MultTier(
            levl=26,
            data={
                Tier.Tier_1: 2.948,
                Tier.Tier_2: 3.182,
                Tier.Tier_3: 3.4,
                Tier.Tier_4: 3.604,
            }
        ),
        27: MultTier(
            levl=27,
            data={
                Tier.Tier_1: 3.026,
                Tier.Tier_2: 3.271,
                Tier.Tier_3: 3.5,
                Tier.Tier_4: 3.714,
            }
        ),
        28: MultTier(
            levl=28,
            data={
                Tier.Tier_1: 3.103,
                Tier.Tier_2: 3.36,
                Tier.Tier_3: 3.601,
                Tier.Tier_4: 3.825,
            }
        ),
        29: MultTier(
            levl=29,
            data={
                Tier.Tier_1: 3.18,
                Tier.Tier_2: 3.45,
                Tier.Tier_3: 3.701,
                Tier.Tier_4: 3.937,
            }
        ),
        30: MultTier(
            levl=30,
            data={
                Tier.Tier_1: 3.257,
                Tier.Tier_2: 3.539,
                Tier.Tier_3: 3.803,
                Tier.Tier_4: 4.049,
            }
        ),
        31: MultTier(
            levl=31,
            data={
                Tier.Tier_1: 3.334,
                Tier.Tier_2: 3.629,
                Tier.Tier_3: 3.904,
                Tier.Tier_4: 4.161,
            }
        ),
        32: MultTier(
            levl=32,
            data={
                Tier.Tier_1: 3.412,
                Tier.Tier_2: 3.719,
                Tier.Tier_3: 4.005,
                Tier.Tier_4: 4.273,
            }
        ),
        33: MultTier(
            levl=33,
            data={
                Tier.Tier_1: 3.489,
                Tier.Tier_2: 3.809,
                Tier.Tier_3: 4.107,
                Tier.Tier_4: 4.386,
            }
        ),
        34: MultTier(
            levl=34,
            data={
                Tier.Tier_1: 3.566,
                Tier.Tier_2: 3.899,
                Tier.Tier_3: 4.209,
                Tier.Tier_4: 4.5,
            }
        ),
        35: MultTier(
            levl=35,
            data={
                Tier.Tier_1: 3.644,
                Tier.Tier_2: 3.989,
                Tier.Tier_3: 4.312,
                Tier.Tier_4: 4.613,
            }
        ),
        36: MultTier(
            levl=36,
            data={
                Tier.Tier_1: 3.721,
                Tier.Tier_2: 4.08,
                Tier.Tier_3: 4.414,
                Tier.Tier_4: 4.727,
            }
        ),
        37: MultTier(
            levl=37,
            data={
                Tier.Tier_1: 3.798,
                Tier.Tier_2: 4.17,
                Tier.Tier_3: 4.517,
                Tier.Tier_4: 4.841,
            }
        ),
        38: MultTier(
            levl=38,
            data={
                Tier.Tier_1: 3.876,
                Tier.Tier_2: 4.261,
                Tier.Tier_3: 4.62,
                Tier.Tier_4: 4.956,
            }
        ),
        39: MultTier(
            levl=39,
            data={
                Tier.Tier_1: 3.953,
                Tier.Tier_2: 4.352,
                Tier.Tier_3: 4.723,
                Tier.Tier_4: 5.071,
            }
        ),
        40: MultTier(
            levl=40,
            data={
                Tier.Tier_1: 4.031,
                Tier.Tier_2: 4.443,
                Tier.Tier_3: 4.827,
                Tier.Tier_4: 5.186,
            }
        ),
        41: MultTier(
            levl=41,
            data={
                Tier.Tier_1: 4.109,
                Tier.Tier_2: 4.534,
                Tier.Tier_3: 4.931,
                Tier.Tier_4: 5.301,
            }
        ),
        42: MultTier(
            levl=42,
            data={
                Tier.Tier_1: 4.186,
                Tier.Tier_2: 4.625,
                Tier.Tier_3: 5.035,
                Tier.Tier_4: 5.417,
            }
        ),
        43: MultTier(
            levl=43,
            data={
                Tier.Tier_1: 4.264,
                Tier.Tier_2: 4.717,
                Tier.Tier_3: 5.139,
                Tier.Tier_4: 5.533,
            }
        ),
        44: MultTier(
            levl=44,
            data={
                Tier.Tier_1: 4.342,
                Tier.Tier_2: 4.808,
                Tier.Tier_3: 5.243,
                Tier.Tier_4: 5.65,
            }
        ),
        45: MultTier(
            levl=45,
            data={
                Tier.Tier_1: 4.419,
                Tier.Tier_2: 4.9,
                Tier.Tier_3: 5.348,
                Tier.Tier_4: 5.767,
            }
        ),
        46: MultTier(
            levl=46,
            data={
                Tier.Tier_1: 4.497,
                Tier.Tier_2: 4.992,
                Tier.Tier_3: 5.453,
                Tier.Tier_4: 5.884,
            }
        ),
        47: MultTier(
            levl=47,
            data={
                Tier.Tier_1: 4.575,
                Tier.Tier_2: 5.084,
                Tier.Tier_3: 5.558,
                Tier.Tier_4: 6,
            }
        ),
        48: MultTier(
            levl=48,
            data={
                Tier.Tier_1: 4.653,
                Tier.Tier_2: 5.176,
                Tier.Tier_3: 5.663,
                Tier.Tier_4: 6.118,
            }
        ),
        49: MultTier(
            levl=49,
            data={
                Tier.Tier_1: 4.731,
                Tier.Tier_2: 5.268,
                Tier.Tier_3: 5.768,
                Tier.Tier_4: 6.236,
            }
        ),
        50: MultTier(
            levl=50,
            data={
                Tier.Tier_1: 4.81,
                Tier.Tier_2: 5.36,
                Tier.Tier_3: 5.874,
                Tier.Tier_4: 6.354,
            }
        ),
        51: MultTier(
            levl=51,
            data={
                Tier.Tier_1: 4.888,
                Tier.Tier_2: 5.453,
                Tier.Tier_3: 5.98,
                Tier.Tier_4: 6.473,
            }
        ),
        52: MultTier(
            levl=52,
            data={
                Tier.Tier_1: 4.966,
                Tier.Tier_2: 5.546,
                Tier.Tier_3: 6.086,
                Tier.Tier_4: 6.592,
            }
        ),
        53: MultTier(
            levl=53,
            data={
                Tier.Tier_1: 5.044,
                Tier.Tier_2: 5.638,
                Tier.Tier_3: 6.192,
                Tier.Tier_4: 6.71,
            }
        ),
        54: MultTier(
            levl=54,
            data={
                Tier.Tier_1: 5.123,
                Tier.Tier_2: 5.731,
                Tier.Tier_3: 6.299,
                Tier.Tier_4: 6.83,
            }
        ),
        55: MultTier(
            levl=55,
            data={
                Tier.Tier_1: 5.201,
                Tier.Tier_2: 5.825,
                Tier.Tier_3: 6.406,
                Tier.Tier_4: 6.949,
            }
        ),
        56: MultTier(
            levl=56,
            data={
                Tier.Tier_1: 5.28,
                Tier.Tier_2: 5.918,
                Tier.Tier_3: 6.513,
                Tier.Tier_4: 7.069,
            }
        ),
        57: MultTier(
            levl=57,
            data={
                Tier.Tier_1: 5.359,
                Tier.Tier_2: 6.011,
                Tier.Tier_3: 6.62,
                Tier.Tier_4: 7.19,
            }
        ),
        58: MultTier(
            levl=58,
            data={
                Tier.Tier_1: 5.437,
                Tier.Tier_2: 6.105,
                Tier.Tier_3: 6.727,
                Tier.Tier_4: 7.309,
            }
        ),
        59: MultTier(
            levl=59,
            data={
                Tier.Tier_1: 5.516,
                Tier.Tier_2: 6.198,
                Tier.Tier_3: 6.835,
                Tier.Tier_4: 7.43,
            }
        ),
        60: MultTier(
            levl=60,
            data={
                Tier.Tier_1: 5.595,
                Tier.Tier_2: 6.292,
                Tier.Tier_3: 6.942,
                Tier.Tier_4: 7.55,
            }
        ),
        61: MultTier(
            levl=61,
            data={
                Tier.Tier_1: 5.674,
                Tier.Tier_2: 6.386,
                Tier.Tier_3: 7.05,
                Tier.Tier_4: 7.671,
            }
        ),
        62: MultTier(
            levl=62,
            data={
                Tier.Tier_1: 5.753,
                Tier.Tier_2: 6.48,
                Tier.Tier_3: 7.158,
                Tier.Tier_4: 7.792,
            }
        ),
        63: MultTier(
            levl=63,
            data={
                Tier.Tier_1: 5.833,
                Tier.Tier_2: 6.575,
                Tier.Tier_3: 7.267,
                Tier.Tier_4: 7.913,
            }
        ),
        64: MultTier(
            levl=64,
            data={
                Tier.Tier_1: 5.912,
                Tier.Tier_2: 6.669,
                Tier.Tier_3: 7.375,
                Tier.Tier_4: 8.035,
            }
        ),
        65: MultTier(
            levl=65,
            data={
                Tier.Tier_1: 5.991,
                Tier.Tier_2: 6.763,
                Tier.Tier_3: 7.484,
                Tier.Tier_4: 8.157,
            }
        ),
        66: MultTier(
            levl=66,
            data={
                Tier.Tier_1: 6.071,
                Tier.Tier_2: 6.858,
                Tier.Tier_3: 7.592,
                Tier.Tier_4: 8.279,
            }
        ),
        67: MultTier(
            levl=67,
            data={
                Tier.Tier_1: 6.15,
                Tier.Tier_2: 6.953,
                Tier.Tier_3: 7.701,
                Tier.Tier_4: 8.401,
            }
        ),
        68: MultTier(
            levl=68,
            data={
                Tier.Tier_1: 6.23,
                Tier.Tier_2: 7.048,
                Tier.Tier_3: 7.811,
                Tier.Tier_4: 8.524,
            }
        ),
        69: MultTier(
            levl=69,
            data={
                Tier.Tier_1: 6.31,
                Tier.Tier_2: 7.143,
                Tier.Tier_3: 7.92,
                Tier.Tier_4: 8.646,
            }
        ),
        70: MultTier(
            levl=70,
            data={
                Tier.Tier_1: 6.39,
                Tier.Tier_2: 7.238,
                Tier.Tier_3: 8.03,
                Tier.Tier_4: 8.77,
            }
        ),
        71: MultTier(
            levl=71,
            data={
                Tier.Tier_1: 6.47,
                Tier.Tier_2: 7.334,
                Tier.Tier_3: 8.139,
                Tier.Tier_4: 8.893,
            }
        ),
        72: MultTier(
            levl=72,
            data={
                Tier.Tier_1: 6.55,
                Tier.Tier_2: 7.429,
                Tier.Tier_3: 8.249,
                Tier.Tier_4: 9.016,
            }
        ),
        73: MultTier(
            levl=73,
            data={
                Tier.Tier_1: 6.63,
                Tier.Tier_2: 7.525,
                Tier.Tier_3: 8.359,
                Tier.Tier_4: 9.14,
            }
        ),
        74: MultTier(
            levl=74,
            data={
                Tier.Tier_1: 6.71,
                Tier.Tier_2: 7.621,
                Tier.Tier_3: 8.47,
                Tier.Tier_4: 9.263,
            }
        ),
        75: MultTier(
            levl=75,
            data={
                Tier.Tier_1: 6.791,
                Tier.Tier_2: 7.717,
                Tier.Tier_3: 8.58,
                Tier.Tier_4: 9.387,
            }
        ),
        76: MultTier(
            levl=76,
            data={
                Tier.Tier_1: 6.871,
                Tier.Tier_2: 7.813,
                Tier.Tier_3: 8.691,
                Tier.Tier_4: 9.512,
            }
        ),
        77: MultTier(
            levl=77,
            data={
                Tier.Tier_1: 6.952,
                Tier.Tier_2: 7.909,
                Tier.Tier_3: 8.802,
                Tier.Tier_4: 9.636,
            }
        ),
        78: MultTier(
            levl=78,
            data={
                Tier.Tier_1: 7.033,
                Tier.Tier_2: 8.005,
                Tier.Tier_3: 8.913,
                Tier.Tier_4: 9.761,
            }
        ),
        79: MultTier(
            levl=79,
            data={
                Tier.Tier_1: 7.113,
                Tier.Tier_2: 8.102,
                Tier.Tier_3: 9.024,
                Tier.Tier_4: 9.886,
            }
        ),
        80: MultTier(
            levl=80,
            data={
                Tier.Tier_1: 7.194,
                Tier.Tier_2: 8.199,
                Tier.Tier_3: 9.135,
                Tier.Tier_4: 10.011,
            }
        ),
        81: MultTier(
            levl=81,
            data={
                Tier.Tier_1: 7.275,
                Tier.Tier_2: 8.295,
                Tier.Tier_3: 9.247,
                Tier.Tier_4: 10.136,
            }
        ),
        82: MultTier(
            levl=82,
            data={
                Tier.Tier_1: 7.357,
                Tier.Tier_2: 8.392,
                Tier.Tier_3: 9.358,
                Tier.Tier_4: 10.261,
            }
        ),
        83: MultTier(
            levl=83,
            data={
                Tier.Tier_1: 7.438,
                Tier.Tier_2: 8.489,
                Tier.Tier_3: 9.47,
                Tier.Tier_4: 10.387,
            }
        ),
        84: MultTier(
            levl=84,
            data={
                Tier.Tier_1: 7.519,
                Tier.Tier_2: 8.587,
                Tier.Tier_3: 9.582,
                Tier.Tier_4: 10.513,
            }
        ),
        85: MultTier(
            levl=85,
            data={
                Tier.Tier_1: 7.601,
                Tier.Tier_2: 8.684,
                Tier.Tier_3: 9.694,
                Tier.Tier_4: 10.639,
            }
        ),
        86: MultTier(
            levl=86,
            data={
                Tier.Tier_1: 7.682,
                Tier.Tier_2: 8.782,
                Tier.Tier_3: 9.807,
                Tier.Tier_4: 10.765,
            }
        ),
        87: MultTier(
            levl=87,
            data={
                Tier.Tier_1: 7.764,
                Tier.Tier_2: 8.879,
                Tier.Tier_3: 9.919,
                Tier.Tier_4: 10.892,
            }
        ),
        88: MultTier(
            levl=88,
            data={
                Tier.Tier_1: 7.846,
                Tier.Tier_2: 8.977,
                Tier.Tier_3: 10.032,
                Tier.Tier_4: 11.018,
            }
        ),
        89: MultTier(
            levl=89,
            data={
                Tier.Tier_1: 7.928,
                Tier.Tier_2: 9.075,
                Tier.Tier_3: 10.145,
                Tier.Tier_4: 11.145,
            }
        ),
        90: MultTier(
            levl=90,
            data={
                Tier.Tier_1: 8.01,
                Tier.Tier_2: 9.173,
                Tier.Tier_3: 10.258,
                Tier.Tier_4: 11.272,
            }
        ),
    }
}
