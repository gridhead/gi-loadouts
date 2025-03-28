import pytest

from gi_loadouts.data.arti import __artilist__
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import ATTR, STAT


@pytest.mark.parametrize(
    "name, pair, quad, rare, team",
    [
        pytest.param(
            "Adventurer",
            [ATTR(stat_name=STAT.health_points, stat_data=1000)],
            [],
            [1, 2, 3],
            (
                "Adventurer's Flower",
                "Adventurer's Tail Feather",
                "Adventurer's Pocket Watch",
                "Adventurer's Golden Goblet",
                "Adventurer's Bandana"
            ),
            id="data.arti: Adventurer"
        ),
        pytest.param(
            "Archaic Petra",
            [ATTR(stat_name=STAT.damage_bonus_geo_perc, stat_data=15)],
            [],
            [4, 5],
            (
                "Flower of Creviced Cliff",
                "Feather of Jagged Peaks",
                "Sundial of Enduring Jade",
                "Goblet of Chiseled Crag",
                "Mask of Solitude Basalt"
            ),
            id="data.arti: Archaic Petra"
        ),
        pytest.param(
            "Berserker",
            [ATTR(stat_name=STAT.critical_rate_perc, stat_data=12)],
            [],
            [3, 4],
            (
                "Berserker's Rose",
                "Berserker's Indigo Feather",
                "Berserker's Timepiece",
                "Berserker's Bone Goblet",
                "Berserker's Battle Mask"
            ),
            id="data.arti: Berserker"
        ),
        pytest.param(
            "Blizzard Strayer",
            [ATTR(stat_name=STAT.damage_bonus_cryo_perc, stat_data=15)],
            [],
            [4, 5],
            (
                "Snowswept Memory",
                "Icebreaker's Resolve",
                "Frozen Homeland's Demise",
                "Frost-Weaved Dignity",
                "Broken Rime's Echo"
            ),
            id="data.arti: Blizzard Strayer"
        ),
        pytest.param(
            "Bloodstained Chivalry",
            [ATTR(stat_name=STAT.damage_bonus_physical_perc, stat_data=25)],
            [],
            [4, 5],
            (
                "Bloodstained Flower of Iron",
                "Bloodstained Black Plume",
                "Bloodstained Final Hour",
                "Bloodstained Chevalier's Goblet",
                "Bloodstained Iron Mask"
            ),
            id="data.arti: Bloodstained Chivalry"
        ),
        pytest.param(
            "Brave Heart",
            [ATTR(stat_name=STAT.attack_perc, stat_data=18)],
            [],
            [3, 4],
            (
                "Medal of the Brave",
                "Prospect of the Brave",
                "Fortitude of the Brave",
                "Outset of the Brave",
                "Crown of the Brave"
            ),
            id="data.arti: Brave Heart"
        ),
        pytest.param(
            "Crimson Witch of Flames",
            [ATTR(stat_name=STAT.damage_bonus_pyro_perc, stat_data=15)],
            [],
            [4, 5],
            (
                "Witch's Flower of Blaze",
                "Witch's Ever-Burning Plume",
                "Witch's End Time",
                "Witch's Heart Flames",
                "Witch's Scorching Hat"
            ),
            id="data.arti: Crimson Witch of Flames"
        ),
        pytest.param(
            "Deepwood Memories",
            [ATTR(stat_name=STAT.damage_bonus_dendro_perc, stat_data=15)],
            [],
            [4, 5],
            (
                "Labyrinth Wayfarer",
                "Scholar of Vines",
                "A Time of Insight",
                "Lamp of the Lost",
                "Laurel Coronet"
            ),
            id="data.arti: Deepwood Memories"
        ),
        pytest.param(
            "Defender's Will",
            [ATTR(stat_name=STAT.defense_perc, stat_data=30)],
            [],
            [3, 4],
            (
                "Guardian's Flower",
                "Guardian's Sigil",
                "Guardian's Clock",
                "Guardian's Vessel",
                "Guardian's Band"
            ),
            id="data.arti: Defender's Will"
        ),
        pytest.param(
            "Desert Pavilion Chronicle",
            [ATTR(stat_name=STAT.damage_bonus_anemo_perc, stat_data=15)],
            [],
            [4, 5],
            (
                "The First Days of the City of Kings",
                "End of the Golden Realm",
                "Timepiece of the Lost Path",
                "Defender of the Enchanting Dream",
                "Legacy of the Desert High-Born"
            ),
            id="data.arti: Desert Pavilion Chronicle"
        ),
        pytest.param(
            "Echoes of an Offering",
            [ATTR(stat_name=STAT.attack_perc, stat_data=18)],
            [],
            [4, 5],
            (
                "Soulscent Bloom",
                "Jade Leaf",
                "Symbol of Felicitation",
                "Chalice of the Font",
                "Flowing Rings"
            ),
            id="data.arti: Archaic Petra"
        ),
        pytest.param(
            "Emblem of Severed Fate",
            [ATTR(stat_name=STAT.energy_recharge_perc, stat_data=20)],
            [],
            [4, 5],
            (
                "Magnificent Tsuba",
                "Sundered Feather",
                "Storm Cage",
                "Scarlet Vessel",
                "Ornate Kabuto"
            ),
            id="data.arti: Emblem of Severed Fate"
        ),
        pytest.param(
            "Finale of the Deep Galleries",
            [ATTR(stat_name=STAT.damage_bonus_cryo_perc, stat_data=15)],
            [],
            [4, 5],
            (
                "Deep Gallery's Echoing Song",
                "Deep Gallery's Distant Pact",
                "Deep Gallery's Moment of Oblivion",
                "Deep Gallery's Bestowed Banquet",
                "Deep Gallery's Lost Crown"
            ),
            id="data.arti: Finale of the Deep Galleries"
        ),
        pytest.param(
            "Flower of Paradise Lost",
            [ATTR(stat_name=STAT.elemental_mastery, stat_data=80)],
            [],
            [4, 5],
            (
                "Ay-Khanoum's Myriad",
                "Wilting Feast",
                "A Moment Congealed",
                "Secret-Keeper's Magic Bottle",
                "Amethyst Crown"
            ),
            id="data.arti: Flower of Paradise Lost"
        ),
        pytest.param(
            "Fragment of Harmonic Whimsy",
            [ATTR(stat_name=STAT.attack_perc, stat_data=18)],
            [],
            [4, 5],
            (
                "Harmonious Symphony Prelude",
                "Ancient Sea's Nocturnal Musing",
                "The Grand Jape of the Turning of Fate",
                "Ichor Shower Rhapsody",
                "Whimsical Dance of the Withered"
            ),
            id="data.arti: Fragment of Harmonic Whimsy"
        ),
        pytest.param(
            "Gambler",
            [],
            [],
            [3, 4],
            (
                "Gambler's Brooch",
                "Gambler's Feather Accessory",
                "Gambler's Pocket Watch",
                "Gambler's Dice Cup",
                "Gambler's Earrings"
            ),
            id="data.arti: Gambler"
        ),
        pytest.param(
            "Gilded Dreams",
            [ATTR(stat_name=STAT.elemental_mastery, stat_data=80)],
            [],
            [4, 5],
            (
                "Dreaming Steelbloom",
                "Feather of Judgment",
                "The Sunken Years",
                "Honeyed Final Feast",
                "Shadow of the Sand King"
            ),
            id="data.arti: Gilded Dreams"
        ),
        pytest.param(
            "Gladiator's Finale",
            [ATTR(stat_name=STAT.attack_perc, stat_data=18)],
            [],
            [4, 5],
            (
                "Gladiator's Nostalgia",
                "Gladiator's Destiny",
                "Gladiator's Longing",
                "Gladiator's Intoxication",
                "Gladiator's Triumphus"
            ),
            id="data.arti: Gladiator's Finale"
        ),
        pytest.param(
            "Golden Troupe",
            [],
            [],
            [4, 5],
            (
                "Golden Song's Variation",
                "Golden Bird's Shedding",
                "Golden Era's Prelude",
                "Golden Night's Bustle",
                "Golden Troupe's Reward"
            ),
            id="data.arti: Golden Troupe"
        ),
        pytest.param(
            "Heart of Depth",
            [ATTR(stat_name=STAT.damage_bonus_hydro_perc, stat_data=15)],
            [],
            [4, 5],
            (
                "Gilded Corsage",
                "Gust of Nostalgia",
                "Copper Compass",
                "Goblet of Thundering Deep",
                "Wine-Stained Tricorne"
            ),
            id="data.arti: Heart of Depth"
        ),
        pytest.param(
            "Husk of Opulent Dreams",
            [ATTR(stat_name=STAT.defense_perc, stat_data=30)],
            [],
            [4, 5],
            (
                "Bloom Times",
                "Plume of Luxury",
                "Song of Life",
                "Calabash of Awakening",
                "Skeletal Hat"
            ),
            id="data.arti: Husk of Opulent Dreams"
        ),
        pytest.param(
            "Instructor",
            [ATTR(stat_name=STAT.elemental_mastery, stat_data=80)],
            [],
            [3, 4],
            (
                "Instructor's Brooch",
                "Instructor's Feather Accessory",
                "Instructor's Pocket Watch",
                "Instructor's Tea Cup",
                "Instructor's Cap"
            ),
            id="data.arti: Instructor"
        ),
        pytest.param(
            "Lavawalker",
            [ATTR(stat_name=STAT.resistance_pyro_perc, stat_data=40)],
            [],
            [4, 5],
            (
                "Lavawalker's Resolution",
                "Lavawalker's Salvation",
                "Lavawalker's Torment",
                "Lavawalker's Epiphany",
                "Lavawalker's Wisdom"
            ),
            id="data.arti: Lavawalker"
        ),
        pytest.param(
            "Long Night's Oath",
            [],
            [],
            [4, 5],
            (
                "Lightkeeper's Pledge",
                "Nightingale's Tail Feather",
                "Undying One's Mourning Bell",
                "A Horn Unwinded",
                "Dyed Tassel"
            ),
            id="data.arti: Long Night's Oath"
        ),
        pytest.param(
            "Lucky Dog",
            [ATTR(stat_name=STAT.defense, stat_data=100)],
            [],
            [1, 2, 3],
            (
                "Lucky Dog's Clover",
                "Lucky Dog's Eagle Feather",
                "Lucky Dog's Hourglass",
                "Lucky Dog's Goblet",
                "Lucky Dog's Silver Circlet"
            ),
            id="data.arti: Lucky Dog"
        ),
        pytest.param(
            "Maiden Beloved",
            [ATTR(stat_name=STAT.healing_bonus_perc, stat_data=15)],
            [],
            [4, 5],
            (
                "Maiden's Distant Love",
                "Maiden's Heart-Stricken Infatuation",
                "Maiden's Passing Youth",
                "Maiden's Fleeting Leisure",
                "Maiden's Fading Beauty"
            ),
            id="data.arti: Maiden Beloved"
        ),
        pytest.param(
            "Marechaussee Hunter",
            [],
            [],
            [4, 5],
            (
                "Hunter's Brooch",
                "Masterpiece's Overture",
                "Moment of Judgment",
                "Forgotten Vessel",
                "Veteran's Visage"
            ),
            id="data.arti: Marechaussee Hunter"
        ),
        pytest.param(
            "Martial Artist",
            [],
            [],
            [3, 4],
            (
                "Martial Artist's Red Flower",
                "Martial Artist's Feather Accessory",
                "Martial Artist's Water Hourglass",
                "Martial Artist's Wine Cup",
                "Martial Artist's Bandana"
            ),
            id="data.arti: Martial Artist"
        ),
        pytest.param(
            "Nighttime Whispers in the Echoing Woods",
            [ATTR(stat_name=STAT.attack_perc, stat_data=18)],
            [],
            [4, 5],
            (
                "Selfless Floral Accessory",
                "Honest Quill",
                "Faithful Hourglass",
                "Magnanimous Ink Bottle",
                "Compassionate Ladies' Hat"
            ),
            id="data.arti: Nighttime Whispers in the Echoing Woods"
        ),
        pytest.param(
            "Noblesse Oblige",
            [],
            [],
            [4, 5],
            (
                "Royal Flora",
                "Royal Plume",
                "Royal Pocket Watch",
                "Royal Silver Urn",
                "Royal Masque"
            ),
            id="data.arti: Noblesse Oblige"
        ),
        pytest.param(
            "Nymph's Dream",
            [ATTR(stat_name=STAT.damage_bonus_hydro_perc, stat_data=15)],
            [],
            [4, 5],
            (
                "Odyssean Flower",
                "Wicked Mage's Plumule",
                "Nymph's Constancy",
                "Heroes' Tea Party",
                "Fell Dragon's Monocle"
            ),
            id="data.arti: Nymph's Dream"
        ),
        pytest.param(
            "Obsidian Codex",
            [],
            [],
            [4, 5],
            (
                "Reckoning of the Xenogenic",
                "Root of the Spirit-Marrow",
                "Myths of the Night Realm",
                "Pre-Banquet of the Contenders",
                "Crown of the Saints"
            ),
            id="data.arti: Obsidian Codex"
        ),
        pytest.param(
            "Ocean-Hued Clam",
            [ATTR(stat_name=STAT.healing_bonus_perc, stat_data=15)],
            [],
            [4, 5],
            (
                "Sea-Dyed Blossom",
                "Deep Palace's Plume",
                "Cowry of Parting",
                "Pearl Cage",
                "Crown of Watatsumi"
            ),
            id="data.arti: Ocean-Hued Clam"
        ),
        pytest.param(
            "Pale Flame",
            [ATTR(stat_name=STAT.damage_bonus_physical_perc, stat_data=25)],
            [],
            [4, 5],
            (
                "Stainless Bloom",
                "Wise Doctor's Pinion",
                "Moment of Cessation",
                "Surpassing Cup",
                "Mocking Mask"
            ),
            id="data.arti: Pale Flame"
        ),
        pytest.param(
            "Resolution of Sojourner",
            [ATTR(stat_name=STAT.attack_perc, stat_data=18)],
            [],
            [3, 4],
            (
                "Heart of Comradeship",
                "Feather of Homecoming",
                "Sundial of the Sojourner",
                "Goblet of the Sojourner",
                "Crown of Parting"
            ),
            id="data.arti: Resolution of Sojourner"
        ),
        pytest.param(
            "Retracing Bolide",
            [ATTR(stat_name=STAT.shield_strength_perc, stat_data=35)],
            [],
            [4, 5],
            (
                "Summer Night's Bloom",
                "Summer Night's Finale",
                "Summer Night's Moment",
                "Summer Night's Waterballoon",
                "Summer Night's Mask"
            ),
            id="data.arti: Retracing Bolide"
        ),
        pytest.param(
            "Scholar",
            [ATTR(stat_name=STAT.energy_recharge_perc, stat_data=20)],
            [],
            [3, 4],
            (
                "Scholar's Bookmark",
                "Scholar's Quill Pen",
                "Scholar's Clock",
                "Scholar's Ink Cup",
                "Scholar's Lens"
            ),
            id="data.arti: Scholar"
        ),
        pytest.param(
            "Scroll of the Hero of Cinder City",
            [],
            [],
            [4, 5],
            (
                "Beast Tamer's Talisman",
                "Mountain Ranger's Marker",
                "Mystic's Gold Dial",
                "Wandering Scholar's Claw Cup",
                "Demon-Warrior's Feather Mask"
            ),
            id="data.arti: Scroll of the Hero of Cinder City"
        ),
        pytest.param(
            "Shimenawa's Reminiscence",
            [ATTR(stat_name=STAT.attack_perc, stat_data=18)],
            [],
            [4, 5],
            (
                "Entangling Bloom",
                "Shaft of Remembrance",
                "Morning Dew's Moment",
                "Hopeful Heart",
                "Capricious Visage"
            ),
            id="data.arti: Shimenawa's Reminiscence"
        ),
        pytest.param(
            "Song of Days Past",
            [ATTR(stat_name=STAT.healing_bonus_perc, stat_data=15)],
            [],
            [4, 5],
            (
                "Forgotten Oath of Days Past",
                "Recollection of Days Past",
                "Echoing Sound From Days Past",
                "Promised Dream of Days Past",
                "Poetry of Days Past"
            ),
            id="data.arti: Song of Days Past"
        ),
        pytest.param(
            "Tenacity of the Millelith",
            [ATTR(stat_name=STAT.health_points_perc, stat_data=20)],
            [],
            [4, 5],
            (
                "Flower of Accolades",
                "Ceremonial War-Plume",
                "Orichalceous Time-Dial",
                "Noble's Pledging Vessel",
                "General's Ancient Helm"
            ),
            id="data.arti: Tenacity of the Millelith"
        ),
        pytest.param(
            "The Exile",
            [ATTR(stat_name=STAT.energy_recharge_perc, stat_data=20)],
            [],
            [3, 4],
            (
                "Exile's Flower",
                "Exile's Feather",
                "Exile's Pocket Watch",
                "Exile's Goblet",
                "Exile's Circlet"
            ),
            id="data.arti: The Exile"
        ),
        pytest.param(
            "Thundering Fury",
            [ATTR(stat_name=STAT.damage_bonus_electro_perc, stat_data=15)],
            [],
            [4, 5],
            (
                "Thunderbird's Mercy",
                "Survivor of Catastrophe",
                "Hourglass of Thunder",
                "Omen of Thunderstorm",
                "Thunder Summoner's Crown"
            ),
            id="data.arti: Thundering Fury"
        ),
        pytest.param(
            "Thundersoother",
            [ATTR(stat_name=STAT.resistance_electro_perc, stat_data=40)],
            [],
            [4, 5],
            (
                "Thundersoother's Heart",
                "Thundersoother's Plume",
                "Hour of Soothing Thunder",
                "Thundersoother's Goblet",
                "Thundersoother's Diadem"
            ),
            id="data.arti: Thundersoother"
        ),
        pytest.param(
            "Tiny Miracle",
            [
                ATTR(stat_name=STAT.resistance_anemo_perc, stat_data=20),
                ATTR(stat_name=STAT.resistance_cryo_perc, stat_data=20),
                ATTR(stat_name=STAT.resistance_dendro_perc, stat_data=20),
                ATTR(stat_name=STAT.resistance_electro_perc, stat_data=20),
                ATTR(stat_name=STAT.resistance_geo_perc, stat_data=20),
                ATTR(stat_name=STAT.resistance_hydro_perc, stat_data=20),
                ATTR(stat_name=STAT.resistance_pyro_perc, stat_data=20)
            ],
            [],
            [3, 4],
            (
                "Tiny Miracle's Flower",
                "Tiny Miracle's Feather",
                "Tiny Miracle's Hourglass",
                "Tiny Miracle's Goblet",
                "Tiny Miracle's Earrings"
            ),
            id="data.arti: Tiny Miracle"
        ),
        pytest.param(
            "Traveling Doctor",
            [ATTR(stat_name=STAT.incoming_healing_bonus_perc, stat_data=20)],
            [],
            [1, 2, 3],
            (
                "Traveling Doctor's Silver Lotus",
                "Traveling Doctor's Owl Feather",
                "Traveling Doctor's Pocket Watch",
                "Traveling Doctor's Medicine Pot",
                "Traveling Doctor's Handkerchief"
            ),
            id="data.arti: Traveling Doctor"
        ),
        pytest.param(
            "Unfinished Reverie",
            [ATTR(stat_name=STAT.attack_perc, stat_data=18)],
            [],
            [4, 5],
            (
                "Dark Fruit of Bright Flowers",
                "Faded Emerald Tail",
                "Moment of Attainment",
                "The Wine-Flask Over Which the Plan Was Hatched",
                "Crownless Crown"
            ),
            id="data.arti: Unfinished Reverie"
        ),
        pytest.param(
            "Vermillion Hereafter",
            [ATTR(stat_name=STAT.attack_perc, stat_data=18)],
            [],
            [4, 5],
            (
                "Flowering Life",
                "Feather of Nascent Light",
                "Solar Relic",
                "Moment of the Pact",
                "Thundering Poise"
            ),
            id="data.arti: Vermillion Hereafter"
        ),
        pytest.param(
            "Viridescent Venerer",
            [ATTR(stat_name=STAT.damage_bonus_anemo_perc, stat_data=15)],
            [],
            [4, 5],
            (
                "In Remembrance of Viridescent Fields",
                "Viridescent Arrow Feather",
                "Viridescent Venerer's Determination",
                "Viridescent Venerer's Vessel",
                "Viridescent Venerer's Diadem"
            ),
            id="data.arti: Viridescent Venerer"
        ),
        pytest.param(
            "Vourukasha's Glow",
            [ATTR(stat_name=STAT.health_points_perc, stat_data=20)],
            [],
            [4, 5],
            (
                "Stamen of Khvarena's Origin",
                "Vibrant Pinion",
                "Ancient Abscission",
                "Feast of Boundless Joy",
                "Heart of Khvarena's Brilliance"
            ),
            id="data.arti: Vourukasha's Glow"
        ),
        pytest.param(
            "Wanderer's Troupe",
            [ATTR(stat_name=STAT.elemental_mastery, stat_data=80)],
            [],
            [4, 5],
            (
                "Troupe's Dawnlight",
                "Bard's Arrow Feather",
                "Concert's Final Hour",
                "Wanderer's String-Kettle",
                "Conductor's Top Hat"
            ),
            id="data.arti: Wanderer's Troupe"
        ),
    ]
)
def test_arti(name: str, pair: list, quad: list, rare: list, team: list) -> None:
    """
    Test all artifacts for correctness

    :return:
    """
    unit = __artilist__[name]
    assert name == unit.name
    assert pair == unit.pairdata
    assert quad == unit.quaddata
    assert [getattr(Rare, f"Star_{indx}") for indx in rare] == unit.rare
    for indx, item in enumerate(["fwol", "pmod", "sdoe", "gboe", "ccol"]):
        assert team[indx] == getattr(unit, item).__name__
