import pytest

from gi_loadouts.data.char import __charmaps__
from gi_loadouts.type.levl import Level
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType
from test import verify_accuracy


@pytest.mark.parametrize(
    "name, weap, rare, vson, seco, data",
    [
        pytest.param(
            "Aether", "sword", 5, "none", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (5012.89, 97.91, 314.61, 6.0),
                "Level 80/90 (Rank 6)": (10121.78, 197.69, 635.25, 24.0),
            }, id="data.char: Aether",
        ),
        pytest.param(
            "Albedo", "sword", 5, "geo", STAT.damage_bonus_geo_perc,
            {
                "Level 40/50 (Rank 2)": (5944.44, 112.88, 393.80, 7.2),
                "Level 80/90 (Rank 6)": (12295.87, 233.48, 814.56, 28.8),
            }, id="data.char: Albedo",
        ),
        pytest.param(
            "Alhaitham", "sword", 5, "dendro", STAT.damage_bonus_dendro_perc,
            {
                "Level 40/50 (Rank 2)": (5999.48, 140.83, 351.31, 7.2),
                "Level 80/90 (Rank 6)": (12409.72, 291.30, 726.67, 28.8),
            }, id="data.char: Alhaitham",
        ),
        pytest.param(
            "Aloy", "bow", 5, "cryo", STAT.damage_bonus_cryo_perc,
            {
                "Level 40/50 (Rank 2)": (4898.66, 105.14, 303.99, 7.2),
                "Level 80/90 (Rank 6)": (10132.71, 217.47, 628.78, 28.8),
            }, id="data.char: Aloy",
        ),
        pytest.param(
            "Amber", "bow", 4, "pyro", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (4361.22, 102.80, 276.86, 6.0),
                "Level 80/90 (Rank 6)": (8805.94, 207.57, 559.02, 24.0),
            }, id="data.char: Amber",
        ),
        pytest.param(
            "Arataki Itto", "claymore", 5, "geo", STAT.critical_rate_perc,
            {
                "Level 40/50 (Rank 2)": (5779.31, 102.13, 431.11, 4.8),
                "Level 80/90 (Rank 6)": (11954.32, 211.25, 891.73, 19.2),
            }, id="data.char: Arataki Itto",
        ),
        pytest.param(
            "Arlecchino", "polearm", 5, "pyro", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (5889.40, 153.73, 343.71, 9.6),
                "Level 80/90 (Rank 6)": (12182.02, 317.98, 710.96, 38.4),
            }, id="data.char: Arlecchino",
        ),
        pytest.param(
            "Baizhu", "catalyst", 5, "dendro", STAT.health_points_perc,
            {
                "Level 40/50 (Rank 2)": (5999.48, 86.54, 224.53, 7.2),
                "Level 80/90 (Rank 6)": (12409.72, 179.00, 464.44, 28.8),
            }, id="data.char: Baizhu",
        ),
        pytest.param(
            "Barbara", "catalyst", 4, "hydro", STAT.health_points_perc,
            {
                "Level 40/50 (Rank 2)": (4511.60, 73.43, 308.32, 6.0),
                "Level 80/90 (Rank 6)": (9109.60, 148.27, 622.55, 24.0),
            }, id="data.char: Barbara",
        ),
        pytest.param(
            "Beidou", "claymore", 4, "electro", STAT.damage_bonus_electro_perc,
            {
                "Level 40/50 (Rank 2)": (6015.47, 103.78, 298.88, 6.0),
                "Level 80/90 (Rank 6)": (12146.13, 209.55, 603.49, 24.0),
            }, id="data.char: Beidou",
        ),
        pytest.param(
            "Bennett", "sword", 4, "pyro", STAT.energy_recharge_perc,
            {
                "Level 40/50 (Rank 2)": (5714.70, 88.12, 355.51, 6.7),
                "Level 80/90 (Rank 6)": (11538.82, 177.92, 717.84, 26.8),
            }, id="data.char: Bennett",
        ),
        pytest.param(
            "Candace", "polearm", 4, "hydro", STAT.health_points_perc,
            {
                "Level 40/50 (Rank 2)": (5012.89, 97.91, 314.61, 6.0),
                "Level 80/90 (Rank 6)": (10121.78, 197.69, 635.25, 24.0),
            }, id="data.char: Candace",
        ),
        pytest.param(
            "Charlotte", "catalyst", 4, "cryo", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (4962.76, 79.79, 251.69, 6.0),
                "Level 80/90 (Rank 6)": (10020.56, 161.12, 508.20, 24.0),
            }, id="data.char: Charlotte",
        ),
        pytest.param(
            "Chasca", "bow", 5, "anemo", STAT.critical_rate_perc,
            {
                "Level 40/50 (Rank 2)": (4403.29, 155.88, 276.35, 4.8),
                "Level 80/90 (Rank 6)": (9108.05, 322.43, 571.62, 19.2),
            }, id="data.char: Chasca",
        ),
        pytest.param(
            "Chevreuse", "polearm", 4, "pyro", STAT.health_points_perc,
            {
                "Level 40/50 (Rank 2)": (5514.18, 89.09, 278.75, 6.0),
                "Level 80/90 (Rank 6)": (11133.95, 179.90, 562.83, 24.0),
            }, id="data.char: Chevreuse",
        ),
        pytest.param(
            "Chiori", "sword", 5, "geo", STAT.critical_rate_perc,
            {
                "Level 40/50 (Rank 2)": (5140.83, 145.13, 428.35, 4.8),
                "Level 80/90 (Rank 6)": (10633.64, 300.19, 886.02, 19.2),
            }, id="data.char: Chiori",
        ),
        pytest.param(
            "Chongyun", "claymore", 4, "cryo", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (5063.02, 102.80, 298.88, 6.0),
                "Level 80/90 (Rank 6)": (10222.99, 207.57, 603.49, 24.0),
            }, id="data.char: Chongyun",
        ),
        pytest.param(
            "Citlali", "catalyst", 5, "cryo", STAT.elemental_mastery,
            {
                "Level 40/50 (Rank 2)": (5229.451285714286, 56.97654357142857, 343.0167307142857, 28.8),
                "Level 80/90 (Rank 6)": (10815.882, 117.84738999999999, 709.52277, 115.2),
            }, id="data.char: Citlali",
        ),
        pytest.param(
            "Clorinde", "sword", 5, "electro", STAT.critical_rate_perc,
            {
                "Level 40/50 (Rank 2)": (5823.35, 151.58, 352.35, 4.8),
                "Level 80/90 (Rank 6)": (12045.40, 313.53, 728.82, 19.2),
            }, id="data.char: Clorinde",
        ),
        pytest.param(
            "Collei", "bow", 4, "dendro", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (4511.60, 92.03, 276.86, 6.0),
                "Level 80/90 (Rank 6)": (9109.60, 185.83, 559.02, 24.0),
            }, id="data.char: Collei",
        ),
        pytest.param(
            "Cyno", "polearm", 5, "electro", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (5614.19, 142.98, 386.20, 9.6),
                "Level 80/90 (Rank 6)": (11612.76, 295.74, 798.84, 38.4),
            }, id="data.char: Cyno",
        ),
        pytest.param(
            "Dehya", "claymore", 5, "pyro", STAT.health_points_perc,
            {
                "Level 40/50 (Rank 2)": (7045.26, 119.33, 282.22, 7.2),
                "Level 80/90 (Rank 6)": (14572.88, 246.82, 583.77, 28.8),
            }, id="data.char: Dehya",
        ),
        pytest.param(
            "Diluc", "claymore", 5, "pyro", STAT.critical_rate_perc,
            {
                "Level 40/50 (Rank 2)": (5834.36, 150.50, 352.35, 4.8),
                "Level 80/90 (Rank 6)": (12068.17, 311.31, 728.82, 19.2),
            }, id="data.char: Diluc",
        ),
        pytest.param(
            "Diona", "bow", 4, "cryo", STAT.damage_bonus_cryo_perc,
            {
                "Level 40/50 (Rank 2)": (4411.34, 97.91, 276.86, 6.0),
                "Level 80/90 (Rank 6)": (8907.16, 197.69, 559.02, 24.0),
            }, id="data.char: Diona",
        ),
        pytest.param(
            "Dori", "claymore", 4, "electro", STAT.health_points_perc,
            {
                "Level 40/50 (Rank 2)": (5714.70, 102.80, 333.49, 6.0),
                "Level 80/90 (Rank 6)": (11538.82, 207.57, 673.37, 24.0),
            }, id="data.char: Dori",
        ),
        pytest.param(
            "Emilie", "polearm", 5, "dendro", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (6098.55, 150.50, 328.17, 9.6),
                "Level 80/90 (Rank 6)": (12614.65, 311.31, 678.80, 38.4),
            }, id="data.char: Emilie",
        ),
        pytest.param(
            "Eula", "claymore", 5, "cryo", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (5944.44, 153.73, 337.49, 9.6),
                "Level 80/90 (Rank 6)": (12295.87, 317.98, 698.09, 38.4),
            }, id="data.char: Eula",
        ),
        pytest.param(
            "Faruzan", "bow", 4, "anemo", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (4411.34, 90.56, 289.45, 6.0),
                "Level 80/90 (Rank 6)": (8907.16, 182.86, 584.43, 24.0),
            }, id="data.char: Faruzan",
        ),
        pytest.param(
            "Fischl", "bow", 4, "electro", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (4235.89, 112.59, 273.71, 6.0),
                "Level 80/90 (Rank 6)": (8552.90, 227.34, 552.67, 24.0),
            }, id="data.char: Faruzan",
        ),
        pytest.param(
            "Freminet", "claymore", 4, "cryo", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (5564.31, 117.49, 326.57, 6.0),
                "Level 80/90 (Rank 6)": (11235.17, 237.23, 659.39, 24.0),
            }, id="data.char: Freminet",
        ),
        pytest.param(
            "Furina", "sword", 5, "hydro", STAT.critical_rate_perc,
            {
                "Level 40/50 (Rank 2)": (6880.14, 109.65, 312.62, 4.8),
                "Level 80/90 (Rank 6)": (14231.33, 226.81, 646.65, 19.2),
            }, id="data.char: Furina",
        ),
        pytest.param(
            "Gaming", "claymore", 4, "pyro", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (5263.54, 139.03, 324.05, 6.0),
                "Level 80/90 (Rank 6)": (10627.86, 280.72, 654.31, 24.0),
            }, id="data.char: Gaming",
        ),
        pytest.param(
            "Ganyu", "bow", 5, "cryo", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (4403.29, 150.50, 283.26, 9.6),
                "Level 80/90 (Rank 6)": (9108.05, 311.31, 585.91, 38.4),
            }, id="data.char: Ganyu",
        ),
        pytest.param(
            "Gorou", "bow", 4, "geo", STAT.damage_bonus_geo_perc,
            {
                "Level 40/50 (Rank 2)": (4411.34, 84.20, 298.88, 6.0),
                "Level 80/90 (Rank 6)": (8907.16, 170.01, 603.49, 24.0),
            }, id="data.char: Gorou",
        ),
        pytest.param(
            "Hu Tao", "polearm", 5, "pyro", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (6990.22, 47.84, 393.80, 9.6),
                "Level 80/90 (Rank 6)": (14459.03, 98.95, 814.56, 38.4),
            }, id="data.char: Hu Tao",
        ),
        pytest.param(
            "Jean", "sword", 5, "anemo", STAT.healing_bonus_perc,
            {
                "Level 40/50 (Rank 2)": (6604.93, 107.50, 345.44, 5.5),
                "Level 80/90 (Rank 6)": (13662.08, 222.36, 714.53, 22.0),
            }, id="data.char: Jean",
        ),
        pytest.param(
            "Kachina", "polearm", 4, "geo", STAT.damage_bonus_geo_perc,
            {
                "Level 40/50 (Rank 2)": (5438.99, 99.86, 365.27, 6.0),
                "Level 80/90 (Rank 6)": (10982.13, 201.64, 737.53, 24.0),
            }, id="data.char: Kachina",
        ),
        pytest.param(
            "Kaedehara Kazuha", "sword", 5, "anemo", STAT.elemental_mastery,
            {
                "Level 40/50 (Rank 2)": (5999.48, 133.30, 362.71, 28.8),
                "Level 80/90 (Rank 6)": (12409.72, 275.73, 750.25, 115.2),
            }, id="data.char: Kaedehara Kazuha",
        ),
        pytest.param(
            "Kaeya", "sword", 4, "cryo", STAT.energy_recharge_perc,
            {
                "Level 40/50 (Rank 2)": (5363.79, 102.80, 364.95, 6.7),
                "Level 80/90 (Rank 6)": (10830.30, 207.57, 736.89, 26.8),
            }, id="data.char: Kaeya",
        ),
        pytest.param(
            "Kamisato Ayaka", "sword", 5, "cryo", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (5779.31, 153.73, 352.35, 9.6),
                "Level 80/90 (Rank 6)": (11954.32, 317.98, 728.82, 38.4),
            }, id="data.char: Kamisato Ayaka",
        ),
        pytest.param(
            "Kamisato Ayato", "sword", 5, "hydro", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (6164.60, 134.38, 345.44, 9.6),
                "Level 80/90 (Rank 6)": (12751.27, 277.96, 714.53, 38.4),
            }, id="data.char: Kamisato Ayato",
        ),
        pytest.param(
            "Kaveh", "claymore", 4, "dendro", STAT.elemental_mastery,
            {
                "Level 40/50 (Rank 2)": (5514.18, 107.70, 346.08, 24.0),
                "Level 80/90 (Rank 6)": (11133.95, 217.46, 698.78, 96.0),
            }, id="data.char: Kaveh",
        ),
        pytest.param(
            "Keqing", "sword", 5, "electro", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (5889.40, 145.13, 359.26, 9.6),
                "Level 80/90 (Rank 6)": (12182.02, 300.19, 743.11, 38.4),
            }, id="data.char: Keqing",
        ),
        pytest.param(
            "Kinich", "claymore", 5, "dendro", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (5779.31, 149.43, 360.29, 9.6),
                "Level 80/90 (Rank 6)": (11954.32, 309.09, 745.25, 38.4),
            }, id="data.char: Kinich",
        ),
        pytest.param(
            "Kirara", "sword", 4, "dendro", STAT.health_points_perc,
            {
                "Level 40/50 (Rank 2)": (5614.44, 102.80, 251.69, 6.0),
                "Level 80/90 (Rank 6)": (11336.39, 207.57, 508.20, 24.0),
            }, id="data.char: Kirara",
        ),
        pytest.param(
            "Klee", "catalyst", 5, "pyro", STAT.damage_bonus_pyro_perc,
            {
                "Level 40/50 (Rank 2)": (4623.45, 139.75, 276.35, 7.2),
                "Level 80/90 (Rank 6)": (9563.45, 289.07, 571.62, 28.8),
            }, id="data.char: Klee",
        ),
        pytest.param(
            "Kujou Sara", "bow", 4, "electro", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (4411.34, 90.07, 289.45, 6.0),
                "Level 80/90 (Rank 6)": (8907.16, 181.87, 584.43, 24.0),
            }, id="data.char: Kujou Sara",
        ),
        pytest.param(
            "Kuki Shinobu", "sword", 4, "electro", STAT.health_points_perc,
            {
                "Level 40/50 (Rank 2)": (5664.57, 97.91, 346.08, 6.0),
                "Level 80/90 (Rank 6)": (11437.61, 197.69, 698.78, 24.0),
            }, id="data.char: Kuki Shinobu",
        ),
        pytest.param(
            "Layla", "sword", 4, "cryo", STAT.health_points_perc,
            {
                "Level 40/50 (Rank 2)": (5113.15, 99.86, 302.03, 6.0),
                "Level 80/90 (Rank 6)": (10324.21, 201.64, 609.84, 24.0),
            }, id="data.char: Layla",
        ),
        pytest.param(
            "Lisa", "catalyst", 4, "electro", STAT.elemental_mastery,
            {
                "Level 40/50 (Rank 2)": (4411.34, 106.72, 264.28, 24.0),
                "Level 80/90 (Rank 6)": (8907.16, 215.48, 533.61, 96.0),
            }, id="data.char: Lisa",
        ),
        pytest.param(
            "Lumine", "sword", 5, "none", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (5012.89, 97.91, 314.61, 6.0),
                "Level 80/90 (Rank 6)": (10121.78, 197.69, 635.25, 24.0),
            }, id="data.char: Lumine",
        ),
        pytest.param(
            "Lynette", "sword", 4, "anemo", STAT.damage_bonus_anemo_perc,
            {
                "Level 40/50 (Rank 2)": (5714.70, 106.72, 328.14, 6.0),
                "Level 80/90 (Rank 6)": (11538.82, 215.48, 662.57, 24.0),
            }, id="data.char: Lynette",
        ),
        pytest.param(
            "Lyney", "bow", 5, "pyro", STAT.critical_rate_perc,
            {
                "Level 40/50 (Rank 2)": (4953.70, 142.98, 241.81, 4.8),
                "Level 80/90 (Rank 6)": (10246.56, 295.74, 500.17, 19.2),
            }, id="data.char: Lyney",
        ),
        pytest.param(
            "Mavuika", "claymore", 5, "pyro", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (5641.509357142857, 161.25512785714287, 355.7947757142857, 9.6),
                "Level 80/90 (Rank 6)": (11669.769, 333.54921, 735.96714, 38.4),
            }, id="data.char: Mavuika",
        ),
        pytest.param(
            "Mika", "polearm", 4, "cryo", STAT.health_points_perc,
            {
                "Level 40/50 (Rank 2)": (5764.82, 102.80, 328.77, 6.0),
                "Level 80/90 (Rank 6)": (11640.04, 207.57, 663.84, 24.0),
            }, id="data.char: Mika",
        ),
        pytest.param(
            "Mona", "catalyst", 5, "hydro", STAT.energy_recharge_perc,
            {
                "Level 40/50 (Rank 2)": (4678.49, 129.00, 293.62, 8.0),
                "Level 80/90 (Rank 6)": (9677.30, 266.84, 607.35, 32.0),
            }, id="data.char: Mona",
        ),
        pytest.param(
            "Mualani", "catalyst", 5, "hydro", STAT.critical_rate_perc,
            {
                "Level 40/50 (Rank 2)": (6825.10, 81.70, 256.31, 4.8),
                "Level 80/90 (Rank 6)": (14117.48, 169.00, 530.18, 19.2),
            }, id="data.char: Mualani",
        ),
        pytest.param(
            "Navia", "claymore", 5, "geo", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (5685.75, 158.03, 356.49, 9.6),
                "Level 80/90 (Rank 6)": (11760.77, 326.88, 737.39, 38.4),
            }, id="data.char: Navia",
        ),
        pytest.param(
            "Neuvillette", "catalyst", 5, "hydro", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (6604.93, 93.63, 259.08, 9.6),
                "Level 80/90 (Rank 6)": (13662.08, 193.68, 535.90, 38.4),
            }, id="data.char: Neuvillette",
        ),
        pytest.param(
            "Nilou", "sword", 5, "hydro", STAT.health_points_perc,
            {
                "Level 40/50 (Rank 2)": (6825.10, 103.20, 327.48, 7.2),
                "Level 80/90 (Rank 6)": (14117.48, 213.47, 677.37, 28.8),
            }, id="data.char: Nilou",
        ),
        pytest.param(
            "Ningguang", "catalyst", 4, "geo", STAT.damage_bonus_geo_perc,
            {
                "Level 40/50 (Rank 2)": (4511.60, 97.91, 264.28, 6.0),
                "Level 80/90 (Rank 6)": (9109.60, 197.69, 533.61, 24.0),
            }, id="data.char: Ningguang",
        ),
        pytest.param(
            "Noelle", "claymore", 4, "geo", STAT.defense_perc,
            {
                "Level 40/50 (Rank 2)": (5564.31, 88.12, 368.10, 7.5),
                "Level 80/90 (Rank 6)": (11235.17, 177.92, 743.25, 30.0),
            }, id="data.char: Noelle",
        ),
        pytest.param(
            "Ororon", "bow", 4, "electro", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (4260.96, 112.59, 270.57, 6.0),
                "Level 80/90 (Rank 6)": (8603.51, 227.34, 546.32, 24.0),
            }, id="data.char: Ororon",
        ),
        pytest.param(
            "Qiqi", "sword", 5, "cryo", STAT.healing_bonus_perc,
            {
                "Level 40/50 (Rank 2)": (5559.15, 129.00, 414.53, 5.5),
                "Level 80/90 (Rank 6)": (11498.91, 266.84, 857.43, 22.0),
            }, id="data.char: Qiqi",
        ),
        pytest.param(
            "Raiden Shogun", "polearm", 5, "electro", STAT.energy_recharge_perc,
            {
                "Level 40/50 (Rank 2)": (5801.33, 151.58, 354.76, 8.0),
                "Level 80/90 (Rank 6)": (11999.86, 313.53, 733.82, 32.0),
            }, id="data.char: Raiden Shogun",
        ),
        pytest.param(
            "Razor", "claymore", 4, "electro", STAT.damage_bonus_physical_perc,
            {
                "Level 40/50 (Rank 2)": (5514.18, 107.70, 346.08, 7.5),
                "Level 80/90 (Rank 6)": (11133.95, 217.46, 698.78, 30.0),
            }, id="data.char: Razor",
        ),
        pytest.param(
            "Rosaria", "polearm", 4, "cryo", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (5664.57, 110.63, 327.20, 6.0),
                "Level 80/90 (Rank 6)": (11437.61, 223.39, 660.66, 24.0),
            }, id="data.char: Rosaria",
        ),
        pytest.param(
            "Sangonomiya Kokomi", "catalyst", 5, "hydro", STAT.damage_bonus_hydro_perc,
            {
                "Level 40/50 (Rank 2)": (6054.52, 105.35, 295.35, 7.2),
                "Level 80/90 (Rank 6)": (12523.57, 217.92, 610.92, 28.8),
            }, id="data.char: Sangonomiya Kokomi",
        ),
        pytest.param(
            "Sayu", "claymore", 4, "anemo", STAT.elemental_mastery,
            {
                "Level 40/50 (Rank 2)": (5464.05, 112.59, 343.24, 24.0),
                "Level 80/90 (Rank 6)": (11032.74, 227.34, 693.06, 96.0),
            }, id="data.char: Sayu",
        ),
        pytest.param(
            "Sethos", "bow", 4, "electro", STAT.elemental_mastery,
            {
                "Level 40/50 (Rank 2)": (4511.60, 104.76, 257.98, 24.0),
                "Level 80/90 (Rank 6)": (9109.60, 211.53, 520.91, 96.0),
            }, id="data.char: Sethos",
        ),
        pytest.param(
            "Shenhe", "polearm", 5, "cryo", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (5839.86, 136.53, 373.07, 7.2),
                "Level 80/90 (Rank 6)": (12079.55, 282.40, 771.69, 28.8),
            }, id="data.char: Shenhe",
        ),
        pytest.param(
            "Shikanoin Heizou", "catalyst", 4, "anemo", STAT.damage_bonus_anemo_perc,
            {
                "Level 40/50 (Rank 2)": (4912.63, 103.78, 315.24, 6.0),
                "Level 80/90 (Rank 6)": (9919.34, 209.55, 636.52, 24.0),
            }, id="data.char: Shikanoin Heizou",
        ),
        pytest.param(
            "Sigewinne", "bow", 5, "hydro", STAT.health_points_perc,
            {
                "Level 40/50 (Rank 2)": (5999.48, 86.54, 224.53, 7.2),
                "Level 80/90 (Rank 6)": (12409.72, 179.00, 464.44, 28.8),
            }, id="data.char: Sigewinne",
        ),
        pytest.param(
            "Sucrose", "catalyst", 4, "anemo", STAT.damage_bonus_anemo_perc,
            {
                "Level 40/50 (Rank 2)": (4260.96, 78.33, 324.05, 6.0),
                "Level 80/90 (Rank 6)": (8603.51, 158.15, 654.31, 24.0),
            }, id="data.char: Sucrose",
        ),
        pytest.param(
            "Tartaglia", "bow", 5, "hydro", STAT.damage_bonus_hydro_perc,
            {
                "Level 40/50 (Rank 2)": (5889.40, 135.45, 366.16, 7.2),
                "Level 80/90 (Rank 6)": (12182.02, 280.18, 757.40, 28.8),
            }, id="data.char: Tartaglia",
        ),
        pytest.param(
            "Thoma", "polearm", 4, "pyro", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (4762.25, 93.01, 346.08, 6.0),
                "Level 80/90 (Rank 6)": (9615.69, 187.80, 698.78, 24.0),
            }, id="data.char: Thoma",
        ),
        pytest.param(
            "Tighnari", "bow", 5, "dendro", STAT.damage_bonus_dendro_perc,
            {
                "Level 40/50 (Rank 2)": (4876.64, 120.40, 283.26, 7.2),
                "Level 80/90 (Rank 6)": (10087.17, 249.05, 585.91, 28.8),
            }, id="data.char: Tighnari",
        ),
        pytest.param(
            "Venti", "bow", 5, "anemo", STAT.energy_recharge_perc,
            {
                "Level 40/50 (Rank 2)": (4733.53, 118.25, 300.53, 8.0),
                "Level 80/90 (Rank 6)": (9791.15, 244.60, 621.64, 32.0),
            }, id="data.char: Venti",
        ),
        pytest.param(
            "Wanderer", "catalyst", 5, "anemo", STAT.critical_rate_perc,
            {
                "Level 40/50 (Rank 2)": (4568.41, 147.28, 272.90, 4.8),
                "Level 80/90 (Rank 6)": (9449.60, 304.64, 564.48, 19.2),
            }, id="data.char: Wanderer",
        ),
        pytest.param(
            "Wriothesley", "catalyst", 5, "cryo", STAT.critical_damage_perc,
            {
                "Level 40/50 (Rank 2)": (6109.56, 139.75, 343.02, 9.6),
                "Level 80/90 (Rank 6)": (12637.42, 289.07, 709.53, 38.4),
            }, id="data.char: Wriothesley",
        ),
        pytest.param(
            "Xiangling", "polearm", 4, "pyro", STAT.elemental_mastery,
            {
                "Level 40/50 (Rank 2)": (5012.89, 103.78, 308.32, 24.0),
                "Level 80/90 (Rank 6)": (10121.78, 209.55, 622.55, 96.0),
            }, id="data.char: Xiangling",
        ),
        pytest.param(
            "Xianyun", "catalyst", 5, "anemo", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (4678.49, 150.50, 257.35, 7.2),
                "Level 80/90 (Rank 6)": (9677.30, 311.31, 532.32, 28.8),
            }, id="data.char: Xianyun",
        ),
        pytest.param(
            "Xiao", "polearm", 5, "anemo", STAT.critical_rate_perc,
            {
                "Level 40/50 (Rank 2)": (5724.27, 156.95, 359.26, 4.8),
                "Level 80/90 (Rank 6)": (11840.47, 324.65, 743.11, 19.2),
            }, id="data.char: Xiao",
        ),
        pytest.param(
            "Xilonen", "sword", 5, "geo", STAT.defense_perc,
            {
                "Level 40/50 (Rank 2)": (5575.66, 123.63, 417.98, 9.0),
                "Level 80/90 (Rank 6)": (11533.07, 255.72, 864.58, 36.0),
            }, id="data.char: Xilonen",
        ),
        pytest.param(
            "Xingqiu", "sword", 4, "hydro", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (4712.12, 93.01, 349.22, 6.0),
                "Level 80/90 (Rank 6)": (9514.47, 187.80, 705.13, 24.0),
            }, id="data.char: Xingqiu",
        ),
        pytest.param(
            "Xinyan", "claymore", 4, "pyro", STAT.attack_perc,
            {
                "Level 40/50 (Rank 2)": (5163.28, 114.55, 368.10, 6.0),
                "Level 80/90 (Rank 6)": (10425.43, 231.29, 743.25, 24.0),
            }, id="data.char: Xinyan",
        ),
        pytest.param(
            "Yae Miko", "catalyst", 5, "electro", STAT.critical_rate_perc,
            {
                "Level 40/50 (Rank 2)": (4661.98, 152.65, 255.62, 4.8),
                "Level 80/90 (Rank 6)": (9643.15, 315.76, 528.75, 19.2),
            }, id="data.char: Yae Miko",
        ),
        pytest.param(
            "Yanfei", "catalyst", 4, "pyro", STAT.damage_bonus_pyro_perc,
            {
                "Level 40/50 (Rank 2)": (4311.09, 110.63, 270.57, 6.0),
                "Level 80/90 (Rank 6)": (8704.73, 223.39, 546.32, 24.0),
            }, id="data.char: Yanfei",
        ),
        pytest.param(
            "Yaoyao", "polearm", 4, "dendro", STAT.health_points_perc,
            {
                "Level 40/50 (Rank 2)": (5664.57, 97.91, 346.08, 6.0),
                "Level 80/90 (Rank 6)": (11437.61, 197.69, 698.78, 24.0),
            }, id="data.char: Yaoyao",
        ),
        pytest.param(
            "Yelan", "bow", 5, "hydro", STAT.critical_rate_perc,
            {
                "Level 40/50 (Rank 2)": (6494.85, 109.65, 246.30, 4.8),
                "Level 80/90 (Rank 6)": (13434.37, 226.81, 509.46, 19.2),
            }, id="data.char: Yelan",
        ),
        pytest.param(
            "Yoimiya", "bow", 5, "pyro", STAT.critical_rate_perc,
            {
                "Level 40/50 (Rank 2)": (4568.41, 145.13, 276.35, 4.8),
                "Level 80/90 (Rank 6)": (9449.60, 300.19, 571.62, 19.2),
            }, id="data.char: Yoimiya",
        ),
        pytest.param(
            "Yun Jin", "polearm", 4, "geo", STAT.energy_recharge_perc,
            {
                "Level 40/50 (Rank 2)": (4912.63, 88.12, 338.53, 6.7),
                "Level 80/90 (Rank 6)": (9919.34, 177.92, 683.53, 26.8),
            }, id="data.char: Yun Jin",
        ),
        pytest.param(
            "Zhongli", "polearm", 5, "geo", STAT.damage_bonus_geo_perc,
            {
                "Level 40/50 (Rank 2)": (6604.93, 112.88, 331.62, 7.2),
                "Level 80/90 (Rank 6)": (13662.08, 233.48, 685.95, 28.8),
            }, id="data.char: Zhongli",
        ),
    ]
)
def test_char(name: str, weap: str, rare: int, vson: int, seco: STAT, data: dict) -> None:
    """
    Test all characters for correctness

    :return:
    """
    unit = __charmaps__[name]()
    assert name == unit.name
    assert getattr(WeaponType, weap) == unit.weapon
    assert getattr(Rare, f"Star_{rare}") == unit.rare
    assert getattr(Vision, vson) == unit.vision
    assert seco == unit.__statname__
    for lvtx, qant in data.items():
        lvut = getattr(Level, lvtx.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_"))
        unit.levl = lvut
        assert verify_accuracy(qant[0], unit.health_points.stat_data)
        assert verify_accuracy(qant[1], unit.attack.stat_data)
        assert verify_accuracy(qant[2], unit.defense.stat_data)
        assert qant[3] == unit.seco.stat_data
