from ..rank import Rank
from ..rare import Rare
from ..stat import STAT

Secs = {
    Rank.Rank_0: 0,
    Rank.Rank_1: 38 / 182,
    Rank.Rank_2: 65 / 182,
    Rank.Rank_3: 101 / 182,
    Rank.Rank_4: 128 / 182,
    Rank.Rank_5: 155 / 182,
    Rank.Rank_6: 1,
}

Mult = {
    1: {
        Rare.Star_4: {STAT.defense: 1.000, STAT.health_points: 1.000, STAT.attack: 1.000},
        Rare.Star_5: {STAT.defense: 1.000, STAT.health_points: 1.000, STAT.attack: 1.000},
    },
    2: {
        Rare.Star_4: {STAT.defense: 1.083, STAT.health_points: 1.083, STAT.attack: 1.083},
        Rare.Star_5: {STAT.defense: 1.083, STAT.health_points: 1.083, STAT.attack: 1.083},
    },
    3: {
        Rare.Star_4: {STAT.defense: 1.165, STAT.health_points: 1.165, STAT.attack: 1.165},
        Rare.Star_5: {STAT.defense: 1.166, STAT.health_points: 1.166, STAT.attack: 1.166},
    },
    4: {
        Rare.Star_4: {STAT.defense: 1.248, STAT.health_points: 1.248, STAT.attack: 1.248},
        Rare.Star_5: {STAT.defense: 1.250, STAT.health_points: 1.250, STAT.attack: 1.250},
    },
    5: {
        Rare.Star_4: {STAT.defense: 1.330, STAT.health_points: 1.330, STAT.attack: 1.330},
        Rare.Star_5: {STAT.defense: 1.333, STAT.health_points: 1.333, STAT.attack: 1.333},
    },
    6: {
        Rare.Star_4: {STAT.defense: 1.413, STAT.health_points: 1.413, STAT.attack: 1.413},
        Rare.Star_5: {STAT.defense: 1.417, STAT.health_points: 1.417, STAT.attack: 1.417},
    },
    7: {
        Rare.Star_4: {STAT.defense: 1.495, STAT.health_points: 1.495, STAT.attack: 1.495},
        Rare.Star_5: {STAT.defense: 1.500, STAT.health_points: 1.500, STAT.attack: 1.500},
    },
    8: {
        Rare.Star_4: {STAT.defense: 1.578, STAT.health_points: 1.578, STAT.attack: 1.578},
        Rare.Star_5: {STAT.defense: 1.584, STAT.health_points: 1.584, STAT.attack: 1.584},
    },
    9: {
        Rare.Star_4: {STAT.defense: 1.661, STAT.health_points: 1.661, STAT.attack: 1.661},
        Rare.Star_5: {STAT.defense: 1.668, STAT.health_points: 1.668, STAT.attack: 1.668},
    },
    10: {
        Rare.Star_4: {STAT.defense: 1.743, STAT.health_points: 1.743, STAT.attack: 1.743},
        Rare.Star_5: {STAT.defense: 1.751, STAT.health_points: 1.751, STAT.attack: 1.751},
    },
    11: {
        Rare.Star_4: {STAT.defense: 1.826, STAT.health_points: 1.826, STAT.attack: 1.826},
        Rare.Star_5: {STAT.defense: 1.835, STAT.health_points: 1.835, STAT.attack: 1.835},
    },
    12: {
        Rare.Star_4: {STAT.defense: 1.908, STAT.health_points: 1.908, STAT.attack: 1.908},
        Rare.Star_5: {STAT.defense: 1.919, STAT.health_points: 1.919, STAT.attack: 1.919},
    },
    13: {
        Rare.Star_4: {STAT.defense: 1.991, STAT.health_points: 1.991, STAT.attack: 1.991},
        Rare.Star_5: {STAT.defense: 2.003, STAT.health_points: 2.003, STAT.attack: 2.003},
    },
    14: {
        Rare.Star_4: {STAT.defense: 2.073, STAT.health_points: 2.073, STAT.attack: 2.073},
        Rare.Star_5: {STAT.defense: 2.088, STAT.health_points: 2.088, STAT.attack: 2.088},
    },
    15: {
        Rare.Star_4: {STAT.defense: 2.156, STAT.health_points: 2.156, STAT.attack: 2.156},
        Rare.Star_5: {STAT.defense: 2.172, STAT.health_points: 2.172, STAT.attack: 2.172},
    },
    16: {
        Rare.Star_4: {STAT.defense: 2.239, STAT.health_points: 2.239, STAT.attack: 2.239},
        Rare.Star_5: {STAT.defense: 2.256, STAT.health_points: 2.256, STAT.attack: 2.256},
    },
    17: {
        Rare.Star_4: {STAT.defense: 2.321, STAT.health_points: 2.321, STAT.attack: 2.321},
        Rare.Star_5: {STAT.defense: 2.341, STAT.health_points: 2.341, STAT.attack: 2.341},
    },
    18: {
        Rare.Star_4: {STAT.defense: 2.404, STAT.health_points: 2.404, STAT.attack: 2.404},
        Rare.Star_5: {STAT.defense: 2.425, STAT.health_points: 2.425, STAT.attack: 2.425},
    },
    19: {
        Rare.Star_4: {STAT.defense: 2.486, STAT.health_points: 2.486, STAT.attack: 2.486},
        Rare.Star_5: {STAT.defense: 2.510, STAT.health_points: 2.510, STAT.attack: 2.510},
    },
    20: {
        Rare.Star_4: {STAT.defense: 2.569, STAT.health_points: 2.569, STAT.attack: 2.569},
        Rare.Star_5: {STAT.defense: 2.594, STAT.health_points: 2.594, STAT.attack: 2.594},
    },
    21: {
        Rare.Star_4: {STAT.defense: 2.651, STAT.health_points: 2.651, STAT.attack: 2.651},
        Rare.Star_5: {STAT.defense: 2.679, STAT.health_points: 2.679, STAT.attack: 2.679},
    },
    22: {
        Rare.Star_4: {STAT.defense: 2.734, STAT.health_points: 2.734, STAT.attack: 2.734},
        Rare.Star_5: {STAT.defense: 2.764, STAT.health_points: 2.764, STAT.attack: 2.764},
    },
    23: {
        Rare.Star_4: {STAT.defense: 2.817, STAT.health_points: 2.817, STAT.attack: 2.817},
        Rare.Star_5: {STAT.defense: 2.849, STAT.health_points: 2.849, STAT.attack: 2.849},
    },
    24: {
        Rare.Star_4: {STAT.defense: 2.899, STAT.health_points: 2.899, STAT.attack: 2.899},
        Rare.Star_5: {STAT.defense: 2.934, STAT.health_points: 2.934, STAT.attack: 2.934},
    },
    25: {
        Rare.Star_4: {STAT.defense: 2.982, STAT.health_points: 2.982, STAT.attack: 2.982},
        Rare.Star_5: {STAT.defense: 3.019, STAT.health_points: 3.019, STAT.attack: 3.019},
    },
    26: {
        Rare.Star_4: {STAT.defense: 3.064, STAT.health_points: 3.064, STAT.attack: 3.064},
        Rare.Star_5: {STAT.defense: 3.105, STAT.health_points: 3.105, STAT.attack: 3.105},
    },
    27: {
        Rare.Star_4: {STAT.defense: 3.147, STAT.health_points: 3.147, STAT.attack: 3.147},
        Rare.Star_5: {STAT.defense: 3.190, STAT.health_points: 3.190, STAT.attack: 3.190},
    },
    28: {
        Rare.Star_4: {STAT.defense: 3.229, STAT.health_points: 3.229, STAT.attack: 3.229},
        Rare.Star_5: {STAT.defense: 3.275, STAT.health_points: 3.275, STAT.attack: 3.275},
    },
    29: {
        Rare.Star_4: {STAT.defense: 3.312, STAT.health_points: 3.312, STAT.attack: 3.312},
        Rare.Star_5: {STAT.defense: 3.361, STAT.health_points: 3.361, STAT.attack: 3.361},
    },
    30: {
        Rare.Star_4: {STAT.defense: 3.394, STAT.health_points: 3.394, STAT.attack: 3.394},
        Rare.Star_5: {STAT.defense: 3.446, STAT.health_points: 3.446, STAT.attack: 3.446},
    },
    31: {
        Rare.Star_4: {STAT.defense: 3.477, STAT.health_points: 3.477, STAT.attack: 3.477},
        Rare.Star_5: {STAT.defense: 3.532, STAT.health_points: 3.532, STAT.attack: 3.532},
    },
    32: {
        Rare.Star_4: {STAT.defense: 3.560, STAT.health_points: 3.560, STAT.attack: 3.560},
        Rare.Star_5: {STAT.defense: 3.618, STAT.health_points: 3.618, STAT.attack: 3.618},
    },
    33: {
        Rare.Star_4: {STAT.defense: 3.642, STAT.health_points: 3.642, STAT.attack: 3.642},
        Rare.Star_5: {STAT.defense: 3.704, STAT.health_points: 3.704, STAT.attack: 3.704},
    },
    34: {
        Rare.Star_4: {STAT.defense: 3.725, STAT.health_points: 3.725, STAT.attack: 3.725},
        Rare.Star_5: {STAT.defense: 3.789, STAT.health_points: 3.789, STAT.attack: 3.789},
    },
    35: {
        Rare.Star_4: {STAT.defense: 3.807, STAT.health_points: 3.807, STAT.attack: 3.807},
        Rare.Star_5: {STAT.defense: 3.875, STAT.health_points: 3.875, STAT.attack: 3.875},
    },
    36: {
        Rare.Star_4: {STAT.defense: 3.890, STAT.health_points: 3.890, STAT.attack: 3.890},
        Rare.Star_5: {STAT.defense: 3.962, STAT.health_points: 3.962, STAT.attack: 3.962},
    },
    37: {
        Rare.Star_4: {STAT.defense: 3.972, STAT.health_points: 3.972, STAT.attack: 3.972},
        Rare.Star_5: {STAT.defense: 4.048, STAT.health_points: 4.048, STAT.attack: 4.048},
    },
    38: {
        Rare.Star_4: {STAT.defense: 4.055, STAT.health_points: 4.055, STAT.attack: 4.055},
        Rare.Star_5: {STAT.defense: 4.134, STAT.health_points: 4.134, STAT.attack: 4.134},
    },
    39: {
        Rare.Star_4: {STAT.defense: 4.138, STAT.health_points: 4.138, STAT.attack: 4.138},
        Rare.Star_5: {STAT.defense: 4.220, STAT.health_points: 4.220, STAT.attack: 4.220},
    },
    40: {
        Rare.Star_4: {STAT.defense: 4.220, STAT.health_points: 4.220, STAT.attack: 4.220},
        Rare.Star_5: {STAT.defense: 4.307, STAT.health_points: 4.307, STAT.attack: 4.307},
    },
    41: {
        Rare.Star_4: {STAT.defense: 4.303, STAT.health_points: 4.303, STAT.attack: 4.303},
        Rare.Star_5: {STAT.defense: 4.393, STAT.health_points: 4.393, STAT.attack: 4.393},
    },
    42: {
        Rare.Star_4: {STAT.defense: 4.385, STAT.health_points: 4.385, STAT.attack: 4.385},
        Rare.Star_5: {STAT.defense: 4.480, STAT.health_points: 4.480, STAT.attack: 4.480},
    },
    43: {
        Rare.Star_4: {STAT.defense: 4.468, STAT.health_points: 4.468, STAT.attack: 4.468},
        Rare.Star_5: {STAT.defense: 4.567, STAT.health_points: 4.567, STAT.attack: 4.567},
    },
    44: {
        Rare.Star_4: {STAT.defense: 4.550, STAT.health_points: 4.550, STAT.attack: 4.550},
        Rare.Star_5: {STAT.defense: 4.653, STAT.health_points: 4.653, STAT.attack: 4.653},
    },
    45: {
        Rare.Star_4: {STAT.defense: 4.633, STAT.health_points: 4.633, STAT.attack: 4.633},
        Rare.Star_5: {STAT.defense: 4.740, STAT.health_points: 4.740, STAT.attack: 4.740},
    },
    46: {
        Rare.Star_4: {STAT.defense: 4.716, STAT.health_points: 4.716, STAT.attack: 4.716},
        Rare.Star_5: {STAT.defense: 4.827, STAT.health_points: 4.827, STAT.attack: 4.827},
    },
    47: {
        Rare.Star_4: {STAT.defense: 4.798, STAT.health_points: 4.798, STAT.attack: 4.798},
        Rare.Star_5: {STAT.defense: 4.914, STAT.health_points: 4.914, STAT.attack: 4.914},
    },
    48: {
        Rare.Star_4: {STAT.defense: 4.881, STAT.health_points: 4.881, STAT.attack: 4.881},
        Rare.Star_5: {STAT.defense: 5.001, STAT.health_points: 5.001, STAT.attack: 5.001},
    },
    49: {
        Rare.Star_4: {STAT.defense: 4.963, STAT.health_points: 4.963, STAT.attack: 4.963},
        Rare.Star_5: {STAT.defense: 5.089, STAT.health_points: 5.089, STAT.attack: 5.089},
    },
    50: {
        Rare.Star_4: {STAT.defense: 5.046, STAT.health_points: 5.046, STAT.attack: 5.046},
        Rare.Star_5: {STAT.defense: 5.176, STAT.health_points: 5.176, STAT.attack: 5.176},
    },
    51: {
        Rare.Star_4: {STAT.defense: 5.128, STAT.health_points: 5.128, STAT.attack: 5.128},
        Rare.Star_5: {STAT.defense: 5.263, STAT.health_points: 5.263, STAT.attack: 5.263},
    },
    52: {
        Rare.Star_4: {STAT.defense: 5.211, STAT.health_points: 5.211, STAT.attack: 5.211},
        Rare.Star_5: {STAT.defense: 5.351, STAT.health_points: 5.351, STAT.attack: 5.351},
    },
    53: {
        Rare.Star_4: {STAT.defense: 5.294, STAT.health_points: 5.294, STAT.attack: 5.294},
        Rare.Star_5: {STAT.defense: 5.438, STAT.health_points: 5.438, STAT.attack: 5.438},
    },
    54: {
        Rare.Star_4: {STAT.defense: 5.376, STAT.health_points: 5.376, STAT.attack: 5.376},
        Rare.Star_5: {STAT.defense: 5.526, STAT.health_points: 5.526, STAT.attack: 5.526},
    },
    55: {
        Rare.Star_4: {STAT.defense: 5.459, STAT.health_points: 5.459, STAT.attack: 5.459},
        Rare.Star_5: {STAT.defense: 5.614, STAT.health_points: 5.614, STAT.attack: 5.614},
    },
    56: {
        Rare.Star_4: {STAT.defense: 5.541, STAT.health_points: 5.541, STAT.attack: 5.541},
        Rare.Star_5: {STAT.defense: 5.702, STAT.health_points: 5.702, STAT.attack: 5.702},
    },
    57: {
        Rare.Star_4: {STAT.defense: 5.624, STAT.health_points: 5.624, STAT.attack: 5.624},
        Rare.Star_5: {STAT.defense: 5.790, STAT.health_points: 5.790, STAT.attack: 5.790},
    },
    58: {
        Rare.Star_4: {STAT.defense: 5.706, STAT.health_points: 5.706, STAT.attack: 5.706},
        Rare.Star_5: {STAT.defense: 5.878, STAT.health_points: 5.878, STAT.attack: 5.878},
    },
    59: {
        Rare.Star_4: {STAT.defense: 5.789, STAT.health_points: 5.789, STAT.attack: 5.789},
        Rare.Star_5: {STAT.defense: 5.966, STAT.health_points: 5.966, STAT.attack: 5.966},
    },
    60: {
        Rare.Star_4: {STAT.defense: 5.872, STAT.health_points: 5.872, STAT.attack: 5.872},
        Rare.Star_5: {STAT.defense: 6.054, STAT.health_points: 6.054, STAT.attack: 6.054},
    },
    61: {
        Rare.Star_4: {STAT.defense: 5.954, STAT.health_points: 5.954, STAT.attack: 5.954},
        Rare.Star_5: {STAT.defense: 6.142, STAT.health_points: 6.142, STAT.attack: 6.142},
    },
    62: {
        Rare.Star_4: {STAT.defense: 6.037, STAT.health_points: 6.037, STAT.attack: 6.037},
        Rare.Star_5: {STAT.defense: 6.230, STAT.health_points: 6.230, STAT.attack: 6.230},
    },
    63: {
        Rare.Star_4: {STAT.defense: 6.119, STAT.health_points: 6.119, STAT.attack: 6.119},
        Rare.Star_5: {STAT.defense: 6.319, STAT.health_points: 6.319, STAT.attack: 6.319},
    },
    64: {
        Rare.Star_4: {STAT.defense: 6.202, STAT.health_points: 6.202, STAT.attack: 6.202},
        Rare.Star_5: {STAT.defense: 6.407, STAT.health_points: 6.407, STAT.attack: 6.407},
    },
    65: {
        Rare.Star_4: {STAT.defense: 6.284, STAT.health_points: 6.284, STAT.attack: 6.284},
        Rare.Star_5: {STAT.defense: 6.496, STAT.health_points: 6.496, STAT.attack: 6.496},
    },
    66: {
        Rare.Star_4: {STAT.defense: 6.367, STAT.health_points: 6.367, STAT.attack: 6.367},
        Rare.Star_5: {STAT.defense: 6.585, STAT.health_points: 6.585, STAT.attack: 6.585},
    },
    67: {
        Rare.Star_4: {STAT.defense: 6.450, STAT.health_points: 6.450, STAT.attack: 6.450},
        Rare.Star_5: {STAT.defense: 6.673, STAT.health_points: 6.673, STAT.attack: 6.673},
    },
    68: {
        Rare.Star_4: {STAT.defense: 6.532, STAT.health_points: 6.532, STAT.attack: 6.532},
        Rare.Star_5: {STAT.defense: 6.762, STAT.health_points: 6.762, STAT.attack: 6.762},
    },
    69: {
        Rare.Star_4: {STAT.defense: 6.615, STAT.health_points: 6.615, STAT.attack: 6.615},
        Rare.Star_5: {STAT.defense: 6.851, STAT.health_points: 6.851, STAT.attack: 6.851},
    },
    70: {
        Rare.Star_4: {STAT.defense: 6.697, STAT.health_points: 6.697, STAT.attack: 6.697},
        Rare.Star_5: {STAT.defense: 6.940, STAT.health_points: 6.940, STAT.attack: 6.940},
    },
    71: {
        Rare.Star_4: {STAT.defense: 6.780, STAT.health_points: 6.780, STAT.attack: 6.780},
        Rare.Star_5: {STAT.defense: 7.029, STAT.health_points: 7.029, STAT.attack: 7.029},
    },
    72: {
        Rare.Star_4: {STAT.defense: 6.862, STAT.health_points: 6.862, STAT.attack: 6.862},
        Rare.Star_5: {STAT.defense: 7.119, STAT.health_points: 7.119, STAT.attack: 7.119},
    },
    73: {
        Rare.Star_4: {STAT.defense: 6.945, STAT.health_points: 6.945, STAT.attack: 6.945},
        Rare.Star_5: {STAT.defense: 7.208, STAT.health_points: 7.208, STAT.attack: 7.208},
    },
    74: {
        Rare.Star_4: {STAT.defense: 7.028, STAT.health_points: 7.028, STAT.attack: 7.028},
        Rare.Star_5: {STAT.defense: 7.297, STAT.health_points: 7.297, STAT.attack: 7.297},
    },
    75: {
        Rare.Star_4: {STAT.defense: 7.110, STAT.health_points: 7.110, STAT.attack: 7.110},
        Rare.Star_5: {STAT.defense: 7.387, STAT.health_points: 7.387, STAT.attack: 7.387},
    },
    76: {
        Rare.Star_4: {STAT.defense: 7.193, STAT.health_points: 7.193, STAT.attack: 7.193},
        Rare.Star_5: {STAT.defense: 7.476, STAT.health_points: 7.476, STAT.attack: 7.476},
    },
    77: {
        Rare.Star_4: {STAT.defense: 7.275, STAT.health_points: 7.275, STAT.attack: 7.275},
        Rare.Star_5: {STAT.defense: 7.566, STAT.health_points: 7.566, STAT.attack: 7.566},
    },
    78: {
        Rare.Star_4: {STAT.defense: 7.358, STAT.health_points: 7.358, STAT.attack: 7.358},
        Rare.Star_5: {STAT.defense: 7.656, STAT.health_points: 7.656, STAT.attack: 7.656},
    },
    79: {
        Rare.Star_4: {STAT.defense: 7.440, STAT.health_points: 7.440, STAT.attack: 7.440},
        Rare.Star_5: {STAT.defense: 7.746, STAT.health_points: 7.746, STAT.attack: 7.746},
    },
    80: {
        Rare.Star_4: {STAT.defense: 7.523, STAT.health_points: 7.523, STAT.attack: 7.523},
        Rare.Star_5: {STAT.defense: 7.836, STAT.health_points: 7.836, STAT.attack: 7.836},
    },
    81: {
        Rare.Star_4: {STAT.defense: 7.606, STAT.health_points: 7.606, STAT.attack: 7.606},
        Rare.Star_5: {STAT.defense: 7.926, STAT.health_points: 7.926, STAT.attack: 7.926},
    },
    82: {
        Rare.Star_4: {STAT.defense: 7.688, STAT.health_points: 7.688, STAT.attack: 7.688},
        Rare.Star_5: {STAT.defense: 8.016, STAT.health_points: 8.016, STAT.attack: 8.016},
    },
    83: {
        Rare.Star_4: {STAT.defense: 7.771, STAT.health_points: 7.771, STAT.attack: 7.771},
        Rare.Star_5: {STAT.defense: 8.106, STAT.health_points: 8.106, STAT.attack: 8.106},
    },
    84: {
        Rare.Star_4: {STAT.defense: 7.853, STAT.health_points: 7.853, STAT.attack: 7.853},
        Rare.Star_5: {STAT.defense: 8.196, STAT.health_points: 8.196, STAT.attack: 8.196},
    },
    85: {
        Rare.Star_4: {STAT.defense: 7.936, STAT.health_points: 7.936, STAT.attack: 7.936},
        Rare.Star_5: {STAT.defense: 8.286, STAT.health_points: 8.286, STAT.attack: 8.286},
    },
    86: {
        Rare.Star_4: {STAT.defense: 8.018, STAT.health_points: 8.018, STAT.attack: 8.018},
        Rare.Star_5: {STAT.defense: 8.377, STAT.health_points: 8.377, STAT.attack: 8.377},
    },
    87: {
        Rare.Star_4: {STAT.defense: 8.101, STAT.health_points: 8.101, STAT.attack: 8.101},
        Rare.Star_5: {STAT.defense: 8.467, STAT.health_points: 8.467, STAT.attack: 8.467},
    },
    88: {
        Rare.Star_4: {STAT.defense: 8.183, STAT.health_points: 8.183, STAT.attack: 8.183},
        Rare.Star_5: {STAT.defense: 8.558, STAT.health_points: 8.558, STAT.attack: 8.558},
    },
    89: {
        Rare.Star_4: {STAT.defense: 8.266, STAT.health_points: 8.266, STAT.attack: 8.266},
        Rare.Star_5: {STAT.defense: 8.649, STAT.health_points: 8.649, STAT.attack: 8.649},
    },
    90: {
        Rare.Star_4: {STAT.defense: 8.349, STAT.health_points: 8.349, STAT.attack: 8.349},
        Rare.Star_5: {STAT.defense: 8.739, STAT.health_points: 8.739, STAT.attack: 8.739},
    },
    95: {
        Rare.Star_4: {STAT.defense: 8.761, STAT.health_points: 8.761, STAT.attack: 9.87},
        Rare.Star_5: {STAT.defense: 9.195, STAT.health_points: 9.195, STAT.attack: 10.184},
    },
    100: {
        Rare.Star_4: {STAT.defense: 9.174, STAT.health_points: 9.174, STAT.attack: 11.392},
        Rare.Star_5: {STAT.defense: 9.652, STAT.health_points: 9.652, STAT.attack: 11.629},
    },
}
