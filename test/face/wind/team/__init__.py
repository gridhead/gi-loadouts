from test.face.wind.arti import actual_ccol, actual_fwol, actual_gboe, actual_pmod, actual_sdoe

yaml_sample = """
ccol:
  area: CCOL
  levl: Level 20
  name: Royal Masque
  rare: 5
  stat:
    a:
      data: 12.0
      name: ATK
    b:
      data: 34.0
      name: ATK %
    c:
      data: 56.0
      name: Crit Rate
    d:
      data: 78.0
      name: Crit DMG
    main:
      data: 35.9
      name: Healing Bonus
  type: Noblesse Oblige
fwol:
  area: FWOL
  levl: Level 20
  name: Magnificent Tsuba
  rare: 5
  stat:
    a:
      data: 12.0
      name: Crit Rate
    b:
      data: 34.0
      name: Crit DMG
    c:
      data: 56.0
      name: Elemental Mastery
    d:
      data: 78.0
      name: Energy Recharge
    main:
      data: 4780.0
      name: HP
  type: Emblem of Severed Fate
gboe:
  area: GBOE
  levl: Level 20
  name: Hopeful Heart
  rare: 5
  stat:
    a:
      data: 12.0
      name: Elemental Mastery
    b:
      data: 34.0
      name: Energy Recharge
    c:
      data: 56.0
      name: HP %
    d:
      data: 78.0
      name: HP
    main:
      data: 58.3
      name: Physical DMG Bonus
  type: Shimenawa's Reminiscence
pmod:
  area: PMOD
  levl: Level 20
  name: Sundered Feather
  rare: 5
  stat:
    a:
      data: 12.0
      name: DEF
    b:
      data: 34.0
      name: DEF %
    c:
      data: 56.0
      name: HP
    d:
      data: 78.0
      name: HP %
    main:
      data: 311.0
      name: ATK
  type: Emblem of Severed Fate
sdoe:
  area: SDOE
  levl: Level 20
  name: Morning Dew's Moment
  rare: 5
  stat:
    a:
      data: 12.0
      name: ATK
    b:
      data: 34.0
      name: ATK %
    c:
      data: 56.0
      name: Crit Rate
    d:
      data: 78.0
      name: Crit DMG
    main:
      data: 186.5
      name: Elemental Mastery
  type: Shimenawa's Reminiscence
"""

json_sample = """
{
  "flower": {
    "id": "9AA6DAE4",
    "location": "",
    "lock": false,
    "setKey": "EmblemOfSeveredFate",
    "rarity": 5,
    "level": 20,
    "slotKey": "flower",
    "mainStatKey": "hp",
    "substats": [
      {
        "key": "critRate_",
        "value": 12.0
      },
      {
        "key": "critDMG_",
        "value": 34.0
      },
      {
        "key": "eleMas",
        "value": 56.0
      },
      {
        "key": "enerRech_",
        "value": 78.0
      }
    ]
  },
  "plume": {
    "id": "2FDCFA98",
    "location": "",
    "lock": false,
    "setKey": "EmblemOfSeveredFate",
    "rarity": 5,
    "level": 20,
    "slotKey": "plume",
    "mainStatKey": "atk",
    "substats": [
      {
        "key": "def",
        "value": 12.0
      },
      {
        "key": "def_",
        "value": 34.0
      },
      {
        "key": "hp",
        "value": 56.0
      },
      {
        "key": "hp_",
        "value": 78.0
      }
    ]
  },
  "sands": {
    "id": "9D28FAFF",
    "location": "",
    "lock": false,
    "setKey": "ShimenawasReminiscence",
    "rarity": 5,
    "level": 20,
    "slotKey": "sands",
    "mainStatKey": "eleMas",
    "substats": [
      {
        "key": "atk",
        "value": 12.0
      },
      {
        "key": "atk_",
        "value": 34.0
      },
      {
        "key": "critRate_",
        "value": 56.0
      },
      {
        "key": "critDMG_",
        "value": 78.0
      }
    ]
  },
  "goblet": {
    "id": "74541CF4",
    "location": "",
    "lock": false,
    "setKey": "ShimenawasReminiscence",
    "rarity": 5,
    "level": 20,
    "slotKey": "goblet",
    "mainStatKey": "physical_dmg_",
    "substats": [
      {
        "key": "eleMas",
        "value": 12.0
      },
      {
        "key": "enerRech_",
        "value": 34.0
      },
      {
        "key": "hp_",
        "value": 56.0
      },
      {
        "key": "hp",
        "value": 78.0
      }
    ]
  },
  "circlet": {
    "id": "B0D283FC",
    "location": "",
    "lock": false,
    "setKey": "NoblesseOblige",
    "rarity": 5,
    "level": 20,
    "slotKey": "circlet",
    "mainStatKey": "heal_",
    "substats": [
      {
        "key": "atk",
        "value": 12.0
      },
      {
        "key": "atk_",
        "value": 34.0
      },
      {
        "key": "critRate_",
        "value": 56.0
      },
      {
        "key": "critDMG_",
        "value": 78.0
      }
    ]
  }
}
"""

actual = {
    "fwol": actual_fwol,
    "pmod": actual_pmod,
    "sdoe": actual_sdoe,
    "gboe": actual_gboe,
    "ccol": actual_ccol,
}
