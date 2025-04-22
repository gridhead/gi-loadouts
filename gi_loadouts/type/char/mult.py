from ..rank import Rank
from ..rare import Rare

Secs = {
    Rank.Rank_0: 0,
    Rank.Rank_1: 38/182,
    Rank.Rank_2: 65/182,
    Rank.Rank_3: 101/182,
    Rank.Rank_4: 128/182,
    Rank.Rank_5: 155/182,
    Rank.Rank_6: 1,
}


Mult = {
    1: {
        Rare.Star_4: 1.000,
        Rare.Star_5: 1.000,
    },
    2: {
        Rare.Star_4: 1.083,
        Rare.Star_5: 1.083,
    },
    3: {
        Rare.Star_4: 1.165,
        Rare.Star_5: 1.166,
    },
    4: {
        Rare.Star_4: 1.248,
        Rare.Star_5: 1.250,
    },
    5: {
        Rare.Star_4: 1.330,
        Rare.Star_5: 1.333,
    },
    6: {
        Rare.Star_4: 1.413,
        Rare.Star_5: 1.417,
    },
    7: {
        Rare.Star_4: 1.495,
        Rare.Star_5: 1.500,
    },
    8: {
        Rare.Star_4: 1.578,
        Rare.Star_5: 1.584,
    },
    9: {
        Rare.Star_4: 1.661,
        Rare.Star_5: 1.668,
    },
    10: {
        Rare.Star_4: 1.743,
        Rare.Star_5: 1.751,
    },
    11: {
        Rare.Star_4: 1.826,
        Rare.Star_5: 1.835,
    },
    12: {
        Rare.Star_4: 1.908,
        Rare.Star_5: 1.919,
    },
    13: {
        Rare.Star_4: 1.991,
        Rare.Star_5: 2.003,
    },
    14: {
        Rare.Star_4: 2.073,
        Rare.Star_5: 2.088,
    },
    15: {
        Rare.Star_4: 2.156,
        Rare.Star_5: 2.172,
    },
    16: {
        Rare.Star_4: 2.239,
        Rare.Star_5: 2.256,
    },
    17: {
        Rare.Star_4: 2.321,
        Rare.Star_5: 2.341,
    },
    18: {
        Rare.Star_4: 2.404,
        Rare.Star_5: 2.425,
    },
    19: {
        Rare.Star_4: 2.486,
        Rare.Star_5: 2.510,
    },
    20: {
        Rare.Star_4: 2.569,
        Rare.Star_5: 2.594,
    },
    21: {
        Rare.Star_4: 2.651,
        Rare.Star_5: 2.679,
    },
    22: {
        Rare.Star_4: 2.734,
        Rare.Star_5: 2.764,
    },
    23: {
        Rare.Star_4: 2.817,
        Rare.Star_5: 2.849,
    },
    24: {
        Rare.Star_4: 2.899,
        Rare.Star_5: 2.934,
    },
    25: {
        Rare.Star_4: 2.982,
        Rare.Star_5: 3.019,
    },
    26: {
        Rare.Star_4: 3.064,
        Rare.Star_5: 3.105,
    },
    27: {
        Rare.Star_4: 3.147,
        Rare.Star_5: 3.190,
    },
    28: {
        Rare.Star_4: 3.229,
        Rare.Star_5: 3.275,
    },
    29: {
        Rare.Star_4: 3.312,
        Rare.Star_5: 3.361,
    },
    30: {
        Rare.Star_4: 3.394,
        Rare.Star_5: 3.446,
    },
    31: {
        Rare.Star_4: 3.477,
        Rare.Star_5: 3.532,
    },
    32: {
        Rare.Star_4: 3.560,
        Rare.Star_5: 3.618,
    },
    33: {
        Rare.Star_4: 3.642,
        Rare.Star_5: 3.704,
    },
    34: {
        Rare.Star_4: 3.725,
        Rare.Star_5: 3.789,
    },
    35: {
        Rare.Star_4: 3.807,
        Rare.Star_5: 3.875,
    },
    36: {
        Rare.Star_4: 3.890,
        Rare.Star_5: 3.962,
    },
    37: {
        Rare.Star_4: 3.972,
        Rare.Star_5: 4.048,
    },
    38: {
        Rare.Star_4: 4.055,
        Rare.Star_5: 4.134,
    },
    39: {
        Rare.Star_4: 4.138,
        Rare.Star_5: 4.220,
    },
    40: {
        Rare.Star_4: 4.220,
        Rare.Star_5: 4.307,
    },
    41: {
        Rare.Star_4: 4.303,
        Rare.Star_5: 4.393,
    },
    42: {
        Rare.Star_4: 4.385,
        Rare.Star_5: 4.480,
    },
    43: {
        Rare.Star_4: 4.468,
        Rare.Star_5: 4.567,
    },
    44: {
        Rare.Star_4: 4.550,
        Rare.Star_5: 4.653,
    },
    45: {
        Rare.Star_4: 4.633,
        Rare.Star_5: 4.740,
    },
    46: {
        Rare.Star_4: 4.716,
        Rare.Star_5: 4.827,
    },
    47: {
        Rare.Star_4: 4.798,
        Rare.Star_5: 4.914,
    },
    48: {
        Rare.Star_4: 4.881,
        Rare.Star_5: 5.001,
    },
    49: {
        Rare.Star_4: 4.963,
        Rare.Star_5: 5.089,
    },
    50: {
        Rare.Star_4: 5.046,
        Rare.Star_5: 5.176,
    },
    51: {
        Rare.Star_4: 5.128,
        Rare.Star_5: 5.263,
    },
    52: {
        Rare.Star_4: 5.211,
        Rare.Star_5: 5.351,
    },
    53: {
        Rare.Star_4: 5.294,
        Rare.Star_5: 5.438,
    },
    54: {
        Rare.Star_4: 5.376,
        Rare.Star_5: 5.526,
    },
    55: {
        Rare.Star_4: 5.459,
        Rare.Star_5: 5.614,
    },
    56: {
        Rare.Star_4: 5.541,
        Rare.Star_5: 5.702,
    },
    57: {
        Rare.Star_4: 5.624,
        Rare.Star_5: 5.790,
    },
    58: {
        Rare.Star_4: 5.706,
        Rare.Star_5: 5.878,
    },
    59: {
        Rare.Star_4: 5.789,
        Rare.Star_5: 5.966,
    },
    60: {
        Rare.Star_4: 5.872,
        Rare.Star_5: 6.054,
    },
    61: {
        Rare.Star_4: 5.954,
        Rare.Star_5: 6.142,
    },
    62: {
        Rare.Star_4: 6.037,
        Rare.Star_5: 6.230,
    },
    63: {
        Rare.Star_4: 6.119,
        Rare.Star_5: 6.319,
    },
    64: {
        Rare.Star_4: 6.202,
        Rare.Star_5: 6.407,
    },
    65: {
        Rare.Star_4: 6.284,
        Rare.Star_5: 6.496,
    },
    66: {
        Rare.Star_4: 6.367,
        Rare.Star_5: 6.585,
    },
    67: {
        Rare.Star_4: 6.450,
        Rare.Star_5: 6.673,
    },
    68: {
        Rare.Star_4: 6.532,
        Rare.Star_5: 6.762,
    },
    69: {
        Rare.Star_4: 6.615,
        Rare.Star_5: 6.851,
    },
    70: {
        Rare.Star_4: 6.697,
        Rare.Star_5: 6.940,
    },
    71: {
        Rare.Star_4: 6.780,
        Rare.Star_5: 7.029,
    },
    72: {
        Rare.Star_4: 6.862,
        Rare.Star_5: 7.119,
    },
    73: {
        Rare.Star_4: 6.945,
        Rare.Star_5: 7.208,
    },
    74: {
        Rare.Star_4: 7.028,
        Rare.Star_5: 7.297,
    },
    75: {
        Rare.Star_4: 7.110,
        Rare.Star_5: 7.387,
    },
    76: {
        Rare.Star_4: 7.193,
        Rare.Star_5: 7.476,
    },
    77: {
        Rare.Star_4: 7.275,
        Rare.Star_5: 7.566,
    },
    78: {
        Rare.Star_4: 7.358,
        Rare.Star_5: 7.656,
    },
    79: {
        Rare.Star_4: 7.440,
        Rare.Star_5: 7.746,
    },
    80: {
        Rare.Star_4: 7.523,
        Rare.Star_5: 7.836,
    },
    81: {
        Rare.Star_4: 7.606,
        Rare.Star_5: 7.926,
    },
    82: {
        Rare.Star_4: 7.688,
        Rare.Star_5: 8.016,
    },
    83: {
        Rare.Star_4: 7.771,
        Rare.Star_5: 8.106,
    },
    84: {
        Rare.Star_4: 7.853,
        Rare.Star_5: 8.196,
    },
    85: {
        Rare.Star_4: 7.936,
        Rare.Star_5: 8.286,
    },
    86: {
        Rare.Star_4: 8.018,
        Rare.Star_5: 8.377,
    },
    87: {
        Rare.Star_4: 8.101,
        Rare.Star_5: 8.467,
    },
    88: {
        Rare.Star_4: 8.183,
        Rare.Star_5: 8.558,
    },
    89: {
        Rare.Star_4: 8.266,
        Rare.Star_5: 8.649,
    },
    90: {
        Rare.Star_4: 8.349,
        Rare.Star_5: 8.739,
    },
}
