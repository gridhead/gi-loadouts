from pydantic import BaseModel

from gi_loadouts.type.stat import ATTR, STAT


class FWOL(BaseModel):
    fwol_main: ATTR = ATTR(stat_name=STAT.health_points, stat_data=0.0)
    fwol_seco_a: ATTR = ATTR()
    fwol_seco_b: ATTR = ATTR()
    fwol_seco_c: ATTR = ATTR()
    fwol_seco_d: ATTR = ATTR()


class PMOD(BaseModel):
    pmod_main: ATTR = ATTR(stat_name=STAT.attack, stat_data=0.0)
    pmod_seco_a: ATTR = ATTR()
    pmod_seco_b: ATTR = ATTR()
    pmod_seco_c: ATTR = ATTR()
    pmod_seco_d: ATTR = ATTR()


class SDOE(BaseModel):
    sdoe_main: ATTR = ATTR()
    sdoe_seco_a: ATTR = ATTR()
    sdoe_seco_b: ATTR = ATTR()
    sdoe_seco_c: ATTR = ATTR()
    sdoe_seco_d: ATTR = ATTR()


class GBOE(BaseModel):
    gboe_main: ATTR = ATTR()
    gboe_seco_a: ATTR = ATTR()
    gboe_seco_b: ATTR = ATTR()
    gboe_seco_c: ATTR = ATTR()
    gboe_seco_d: ATTR = ATTR()


class CCOL(BaseModel):
    ccol_main: ATTR = ATTR()
    ccol_seco_a: ATTR = ATTR()
    ccol_seco_b: ATTR = ATTR()
    ccol_seco_c: ATTR = ATTR()
    ccol_seco_d: ATTR = ATTR()


class TEAM(FWOL, PMOD, SDOE, GBOE, CCOL):
    pairdata_a: list = []
    pairdata_b: list = []
    quaddata: list = []
