import pytest

from gi_loadouts.type.arti import CCOL, FWOL, GBOE, PMOD, SDOE
from gi_loadouts.type.arti.base import (
    MainStatType_CCOL,
    MainStatType_FWOL,
    MainStatType_GBOE,
    MainStatType_PMOD,
    MainStatType_SDOE,
)
from gi_loadouts.type.arti.ccol import __revmap__ as __ccolpage__
from gi_loadouts.type.arti.fwol import __revmap__ as __fwolpage__
from gi_loadouts.type.arti.gboe import __revmap__ as __gboepage__
from gi_loadouts.type.arti.pmod import __revmap__ as __pmodpage__
from gi_loadouts.type.arti.sdoe import __revmap__ as __sdoepage__


@pytest.mark.parametrize(
    "item, stat",
    [
        pytest.param(
            FWOL(),
            stat,
            id=f"type.arti.fwol: Flower of Life with {stat.value.value}",
        )
        for stat in __fwolpage__.values()
    ],
)
def test_fwol(item, stat):
    zerodata = {
        MainStatType_FWOL.health_points: 129,
    }
    item.stat_name = stat
    assert item.stat_data == zerodata[stat]


@pytest.mark.parametrize(
    "item, stat",
    [
        pytest.param(
            PMOD(),
            stat,
            id=f"type.arti.pmod: Plume of Death with {stat.value.value}",
        )
        for stat in __pmodpage__.values()
    ],
)
def test_pmod(item, stat):
    zerodata = {
        MainStatType_PMOD.attack: 8.0,
    }
    item.stat_name = stat
    assert item.stat_data == zerodata[stat]


@pytest.mark.parametrize(
    "item, stat",
    [
        pytest.param(
            SDOE(),
            stat,
            id=f"type.arti.sdoe: Sands of Eon with {stat.value.value}",
        )
        for stat in __sdoepage__.values()
    ],
)
def test_sdoe(item, stat):
    zerodata = {
        MainStatType_SDOE.attack_perc: 3.1,
        MainStatType_SDOE.defense_perc: 3.9,
        MainStatType_SDOE.health_points_perc: 3.1,
        MainStatType_SDOE.elemental_mastery: 12.6,
        MainStatType_SDOE.energy_recharge_perc: 3.5,
    }
    item.stat_name = stat
    assert item.stat_data == zerodata[stat]


@pytest.mark.parametrize(
    "item, stat",
    [
        pytest.param(
            GBOE(),
            stat,
            id=f"type.arti.gboe: Goblet of Eonothem with {stat.value.value}",
        )
        for stat in __gboepage__.values()
    ],
)
def test_gboe(item, stat):
    zerodata = {
        MainStatType_GBOE.attack_perc: 3.1,
        MainStatType_GBOE.defense_perc: 3.9,
        MainStatType_GBOE.health_points_perc: 3.1,
        MainStatType_GBOE.elemental_mastery: 12.6,
        MainStatType_GBOE.damage_bonus_anemo_perc: 3.1,
        MainStatType_GBOE.damage_bonus_cryo_perc: 3.1,
        MainStatType_GBOE.damage_bonus_dendro_perc: 3.1,
        MainStatType_GBOE.damage_bonus_electro_perc: 3.1,
        MainStatType_GBOE.damage_bonus_geo_perc: 3.1,
        MainStatType_GBOE.damage_bonus_hydro_perc: 3.1,
        MainStatType_GBOE.damage_bonus_pyro_perc: 3.1,
        MainStatType_GBOE.damage_bonus_physical_perc: 3.9,
    }
    item.stat_name = stat
    assert item.stat_data == zerodata[stat]


@pytest.mark.parametrize(
    "item, stat",
    [
        pytest.param(
            CCOL(),
            stat,
            id=f"type.arti.ccol: Circlet of Logos with {stat.value.value}",
        )
        for stat in __ccolpage__.values()
    ],
)
def test_ccol(item, stat):
    zerodata = {
        MainStatType_CCOL.attack_perc: 3.1,
        MainStatType_CCOL.defense_perc: 3.9,
        MainStatType_CCOL.health_points_perc: 3.1,
        MainStatType_CCOL.elemental_mastery: 12.6,
        MainStatType_CCOL.healing_bonus_perc: 2.4,
        MainStatType_CCOL.critical_rate_perc: 2.1,
        MainStatType_CCOL.critical_damage_perc: 4.2,
    }
    item.stat_name = stat
    assert item.stat_data == zerodata[stat]
