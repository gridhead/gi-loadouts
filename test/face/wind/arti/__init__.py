yaml_fwol_sample = """
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
"""

json_fwol_sample = """
{
  "id": "00000000",
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
}
"""

actual_fwol = {
    "area": "fwol",
    "rare": "Star 5",
    "levl": "Level 20",
    "main": "HP",
    "type": "Emblem of Severed Fate",
    "name": "Magnificent Tsuba",
    "stat": {
        "a": {
            "name": "Crit Rate",
            "data": 12.0
        },
        "b": {
            "name": "Crit DMG",
            "data": 34.0
        },
        "c": {
            "name": "Elemental Mastery",
            "data": 56.0
        },
        "d": {
            "name": "Energy Recharge",
            "data": 78.0
        },
    }
}

yaml_pmod_sample = """
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
"""

json_pmod_sample = """
{
  "id": "00000000",
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
}
"""

actual_pmod = {
    "area": "pmod",
    "rare": "Star 5",
    "levl": "Level 20",
    "main": "ATK",
    "type": "Emblem of Severed Fate",
    "name": "Sundered Feather",
    "stat": {
        "a": {
            "name": "DEF",
            "data": 12.0
        },
        "b": {
            "name": "DEF %",
            "data": 34.0
        },
        "c": {
            "name": "HP",
            "data": 56.0
        },
        "d": {
            "name": "HP %",
            "data": 78.0
        },
    }
}

yaml_sdoe_sample = """
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

json_sdoe_sample = """
{
  "id": "00000000",
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
}
"""

actual_sdoe = {
    "area": "sdoe",
    "rare": "Star 5",
    "levl": "Level 20",
    "main": "Elemental Mastery",
    "type": "Shimenawa's Reminiscence",
    "name": "Morning Dew's Moment",
    "stat": {
        "a": {
            "name": "ATK",
            "data": 12.0
        },
        "b": {
            "name": "ATK %",
            "data": 34.0
        },
        "c": {
            "name": "Crit Rate",
            "data": 56.0
        },
        "d": {
            "name": "Crit DMG",
            "data": 78.0
        },
    }
}

yaml_gboe_sample = """
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
"""

json_gboe_sample = """
{
  "id": "00000000",
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
}
"""

actual_gboe = {
    "area": "gboe",
    "rare": "Star 5",
    "levl": "Level 20",
    "main": "Physical DMG Bonus",
    "type": "Shimenawa's Reminiscence",
    "name": "Hopeful Heart",
    "stat": {
        "a": {
            "name": "Elemental Mastery",
            "data": 12.0
        },
        "b": {
            "name": "Energy Recharge",
            "data": 34.0
        },
        "c": {
            "name": "HP %",
            "data": 56.0
        },
        "d": {
            "name": "HP",
            "data": 78.0
        },
    }
}

json_gboe_sample = """
{
  "id": "00000000",
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
}
"""

yaml_ccol_sample = """
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
"""

json_ccol_sample = """
{
  "id": "00000000",
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
"""

actual_ccol = {
    "area": "ccol",
    "rare": "Star 5",
    "levl": "Level 20",
    "main": "Healing Bonus",
    "type": "Noblesse Oblige",
    "name": "Royal Masque",
    "stat": {
        "a": {
            "name": "ATK",
            "data": 12.0
        },
        "b": {
            "name": "ATK %",
            "data": 34.0
        },
        "c": {
            "name": "Crit Rate",
            "data": 56.0
        },
        "d": {
            "name": "Crit DMG",
            "data": 78.0
        },
    }
}

# YAML sample with tab characters to test tab handling fix
yaml_fwol_with_tabs_sample = """
area: FWOL
levl: Level 00
name: Adventurer's Flower
rare: 1
stat:
  a:
    data: 1.0
    name: ATK %
  b:
    data: 0.0
    name: None
  c:
    data: 0.0
    name: None	
  d:
    data: 0.0
    name: None
  main:
    data: 129.0
    name: HP
type: Adventurer
"""
