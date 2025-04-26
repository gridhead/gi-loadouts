from enum import Enum

from ...type.arti import ArtifactTeam
from ...type.rare import Rare
from . import (
    acpt,
    advn,
    bscv,
    bskr,
    bvht,
    bzst,
    cwof,
    dfwl,
    dspc,
    dwmm,
    eoao,
    eosf,
    fodg,
    fohw,
    fopl,
    gdfl,
    gdtp,
    gldr,
    gmbr,
    hodp,
    hood,
    istr,
    lkdg,
    lnso,
    lvwk,
    mcht,
    mdbv,
    mtat,
    nlob,
    nmdr,
    none,
    nwiw,
    ochc,
    odcx,
    plfm,
    rcbl,
    rosj,
    sclr,
    shcc,
    smrm,
    sodp,
    tdfr,
    tdst,
    texl,
    totm,
    tvdt,
    tymc,
    ufrv,
    vdvn,
    vkgw,
    vmha,
    wdtp,
)

__artilist__ = {
    advn.team.__teamname__: ArtifactTeam(
        name=advn.team.__teamname__,
        fwol=advn.fwol(), pmod=advn.pmod(), sdoe=advn.sdoe(), gboe=advn.gboe(), ccol=advn.ccol(),
        pairdata=advn.team.__pairdata__, pairtext=advn.team.__pairtext__,
        quaddata=advn.team.__quaddata__, quadtext=advn.team.__quadtext__,
        rare=[Rare.Star_1, Rare.Star_2, Rare.Star_3],
        file=advn.__name__.split(".")[-1]
    ),
    acpt.team.__teamname__: ArtifactTeam(
        name=acpt.team.__teamname__,
        fwol=acpt.fwol(), pmod=acpt.pmod(), sdoe=acpt.sdoe(), gboe=acpt.gboe(), ccol=acpt.ccol(),
        pairdata=acpt.team.__pairdata__, pairtext=acpt.team.__pairtext__,
        quaddata=acpt.team.__quaddata__, quadtext=acpt.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=acpt.__name__.split(".")[-1]
    ),
    bskr.team.__teamname__: ArtifactTeam(
        name=bskr.team.__teamname__,
        fwol=bskr.fwol(), pmod=bskr.pmod(), sdoe=bskr.sdoe(), gboe=bskr.gboe(), ccol=bskr.ccol(),
        pairdata=bskr.team.__pairdata__, pairtext=bskr.team.__pairtext__,
        quaddata=bskr.team.__quaddata__, quadtext=bskr.team.__quadtext__,
        rare=[Rare.Star_3, Rare.Star_4],
        file=bskr.__name__.split(".")[-1]
    ),
    bzst.team.__teamname__: ArtifactTeam(
        name=bzst.team.__teamname__,
        fwol=bzst.fwol(), pmod=bzst.pmod(), sdoe=bzst.sdoe(), gboe=bzst.gboe(), ccol=bzst.ccol(),
        pairdata=bzst.team.__pairdata__, pairtext=bzst.team.__pairtext__,
        quaddata=bzst.team.__quaddata__, quadtext=bzst.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=bzst.__name__.split(".")[-1]
    ),
    bscv.team.__teamname__: ArtifactTeam(
        name=bscv.team.__teamname__,
        fwol=bscv.fwol(), pmod=bscv.pmod(), sdoe=bscv.sdoe(), gboe=bscv.gboe(), ccol=bscv.ccol(),
        pairdata=bscv.team.__pairdata__, pairtext=bscv.team.__pairtext__,
        quaddata=bscv.team.__quaddata__, quadtext=bscv.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=bscv.__name__.split(".")[-1]
    ),
    bvht.team.__teamname__: ArtifactTeam(
        name=bvht.team.__teamname__,
        fwol=bvht.fwol(), pmod=bvht.pmod(), sdoe=bvht.sdoe(), gboe=bvht.gboe(), ccol=bvht.ccol(),
        pairdata=bvht.team.__pairdata__, pairtext=bvht.team.__pairtext__,
        quaddata=bvht.team.__quaddata__, quadtext=bvht.team.__quadtext__,
        rare=[Rare.Star_3, Rare.Star_4],
        file=bvht.__name__.split(".")[-1]
    ),
    cwof.team.__teamname__: ArtifactTeam(
        name=cwof.team.__teamname__,
        fwol=cwof.fwol(), pmod=cwof.pmod(), sdoe=cwof.sdoe(), gboe=cwof.gboe(), ccol=cwof.ccol(),
        pairdata=cwof.team.__pairdata__, pairtext=cwof.team.__pairtext__,
        quaddata=cwof.team.__quaddata__, quadtext=cwof.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=cwof.__name__.split(".")[-1]
    ),
    dwmm.team.__teamname__: ArtifactTeam(
        name=dwmm.team.__teamname__,
        fwol=dwmm.fwol(), pmod=dwmm.pmod(), sdoe=dwmm.sdoe(), gboe=dwmm.gboe(), ccol=dwmm.ccol(),
        pairdata=dwmm.team.__pairdata__, pairtext=dwmm.team.__pairtext__,
        quaddata=dwmm.team.__quaddata__, quadtext=dwmm.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=dwmm.__name__.split(".")[-1]
    ),
    dfwl.team.__teamname__: ArtifactTeam(
        name=dfwl.team.__teamname__,
        fwol=dfwl.fwol(), pmod=dfwl.pmod(), sdoe=dfwl.sdoe(), gboe=dfwl.gboe(), ccol=dfwl.ccol(),
        pairdata=dfwl.team.__pairdata__, pairtext=dfwl.team.__pairtext__,
        quaddata=dfwl.team.__quaddata__, quadtext=dfwl.team.__quadtext__,
        rare=[Rare.Star_3, Rare.Star_4],
        file=dfwl.__name__.split(".")[-1]
    ),
    dspc.team.__teamname__: ArtifactTeam(
        name=dspc.team.__teamname__,
        fwol=dspc.fwol(), pmod=dspc.pmod(), sdoe=dspc.sdoe(), gboe=dspc.gboe(), ccol=dspc.ccol(),
        pairdata=dspc.team.__pairdata__, pairtext=dspc.team.__pairtext__,
        quaddata=dspc.team.__quaddata__, quadtext=dspc.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=dspc.__name__.split(".")[-1]
    ),
    eoao.team.__teamname__: ArtifactTeam(
        name=eoao.team.__teamname__,
        fwol=eoao.fwol(), pmod=eoao.pmod(), sdoe=eoao.sdoe(), gboe=eoao.gboe(), ccol=eoao.ccol(),
        pairdata=eoao.team.__pairdata__, pairtext=eoao.team.__pairtext__,
        quaddata=eoao.team.__quaddata__, quadtext=eoao.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=eoao.__name__.split(".")[-1]
    ),
    eosf.team.__teamname__: ArtifactTeam(
        name=eosf.team.__teamname__,
        fwol=eosf.fwol(), pmod=eosf.pmod(), sdoe=eosf.sdoe(), gboe=eosf.gboe(), ccol=eosf.ccol(),
        pairdata=eosf.team.__pairdata__, pairtext=eosf.team.__pairtext__,
        quaddata=eosf.team.__quaddata__, quadtext=eosf.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=eosf.__name__.split(".")[-1]
    ),
    fodg.team.__teamname__: ArtifactTeam(
        name=fodg.team.__teamname__,
        fwol=fodg.fwol(), pmod=fodg.pmod(), sdoe=fodg.sdoe(), gboe=fodg.gboe(), ccol=fodg.ccol(),
        pairdata=fodg.team.__pairdata__, pairtext=fodg.team.__pairtext__,
        quaddata=fodg.team.__quaddata__, quadtext=fodg.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=fodg.__name__.split(".")[-1]
    ),
    fopl.team.__teamname__: ArtifactTeam(
        name=fopl.team.__teamname__,
        fwol=fopl.fwol(), pmod=fopl.pmod(), sdoe=fopl.sdoe(), gboe=fopl.gboe(), ccol=fopl.ccol(),
        pairdata=fopl.team.__pairdata__, pairtext=fopl.team.__pairtext__,
        quaddata=fopl.team.__quaddata__, quadtext=fopl.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=fopl.__name__.split(".")[-1]
    ),
    fohw.team.__teamname__: ArtifactTeam(
        name=fohw.team.__teamname__,
        fwol=fohw.fwol(), pmod=fohw.pmod(), sdoe=fohw.sdoe(), gboe=fohw.gboe(), ccol=fohw.ccol(),
        pairdata=fohw.team.__pairdata__, pairtext=fohw.team.__pairtext__,
        quaddata=fohw.team.__quaddata__, quadtext=fohw.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=fohw.__name__.split(".")[-1]
    ),
    gmbr.team.__teamname__: ArtifactTeam(
        name=gmbr.team.__teamname__,
        fwol=gmbr.fwol(), pmod=gmbr.pmod(), sdoe=gmbr.sdoe(), gboe=gmbr.gboe(), ccol=gmbr.ccol(),
        pairdata=gmbr.team.__pairdata__, pairtext=gmbr.team.__pairtext__,
        quaddata=gmbr.team.__quaddata__, quadtext=gmbr.team.__quadtext__,
        rare=[Rare.Star_3, Rare.Star_4],
        file=gmbr.__name__.split(".")[-1]
    ),
    gldr.team.__teamname__: ArtifactTeam(
        name=gldr.team.__teamname__,
        fwol=gldr.fwol(), pmod=gldr.pmod(), sdoe=gldr.sdoe(), gboe=gldr.gboe(), ccol=gldr.ccol(),
        pairdata=gldr.team.__pairdata__, pairtext=gldr.team.__pairtext__,
        quaddata=gldr.team.__quaddata__, quadtext=gldr.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=gldr.__name__.split(".")[-1]
    ),
    gdfl.team.__teamname__: ArtifactTeam(
        name=gdfl.team.__teamname__,
        fwol=gdfl.fwol(), pmod=gdfl.pmod(), sdoe=gdfl.sdoe(), gboe=gdfl.gboe(), ccol=gdfl.ccol(),
        pairdata=gdfl.team.__pairdata__, pairtext=gdfl.team.__pairtext__,
        quaddata=gdfl.team.__quaddata__, quadtext=gdfl.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=gdfl.__name__.split(".")[-1]
    ),
    gdtp.team.__teamname__: ArtifactTeam(
        name=gdtp.team.__teamname__,
        fwol=gdtp.fwol(), pmod=gdtp.pmod(), sdoe=gdtp.sdoe(), gboe=gdtp.gboe(), ccol=gdtp.ccol(),
        pairdata=gdtp.team.__pairdata__, pairtext=gdtp.team.__pairtext__,
        quaddata=gdtp.team.__quaddata__, quadtext=gdtp.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=gdtp.__name__.split(".")[-1]
    ),
    hodp.team.__teamname__: ArtifactTeam(
        name=hodp.team.__teamname__,
        fwol=hodp.fwol(), pmod=hodp.pmod(), sdoe=hodp.sdoe(), gboe=hodp.gboe(), ccol=hodp.ccol(),
        pairdata=hodp.team.__pairdata__, pairtext=hodp.team.__pairtext__,
        quaddata=hodp.team.__quaddata__, quadtext=hodp.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=hodp.__name__.split(".")[-1]
    ),
    hood.team.__teamname__: ArtifactTeam(
        name=hood.team.__teamname__,
        fwol=hood.fwol(), pmod=hood.pmod(), sdoe=hood.sdoe(), gboe=hood.gboe(), ccol=hood.ccol(),
        pairdata=hood.team.__pairdata__, pairtext=hood.team.__pairtext__,
        quaddata=hood.team.__quaddata__, quadtext=hood.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=hood.__name__.split(".")[-1]
    ),
    istr.team.__teamname__: ArtifactTeam(
        name=istr.team.__teamname__,
        fwol=istr.fwol(), pmod=istr.pmod(), sdoe=istr.sdoe(), gboe=istr.gboe(), ccol=istr.ccol(),
        pairdata=istr.team.__pairdata__, pairtext=istr.team.__pairtext__,
        quaddata=istr.team.__quaddata__, quadtext=istr.team.__quadtext__,
        rare=[Rare.Star_3, Rare.Star_4],
        file=istr.__name__.split(".")[-1]
    ),
    lvwk.team.__teamname__: ArtifactTeam(
        name=lvwk.team.__teamname__,
        fwol=lvwk.fwol(), pmod=lvwk.pmod(), sdoe=lvwk.sdoe(), gboe=lvwk.gboe(), ccol=lvwk.ccol(),
        pairdata=lvwk.team.__pairdata__, pairtext=lvwk.team.__pairtext__,
        quaddata=lvwk.team.__quaddata__, quadtext=lvwk.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=lvwk.__name__.split(".")[-1]
    ),
    lnso.team.__teamname__: ArtifactTeam(
        name=lnso.team.__teamname__,
        fwol=lnso.fwol(), pmod=lnso.pmod(), sdoe=lnso.sdoe(), gboe=lnso.gboe(), ccol=lnso.ccol(),
        pairdata=lnso.team.__pairdata__, pairtext=lnso.team.__pairtext__,
        quaddata=lnso.team.__quaddata__, quadtext=lnso.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=lnso.__name__.split(".")[-1]
    ),
    lkdg.team.__teamname__: ArtifactTeam(
        name=lkdg.team.__teamname__,
        fwol=lkdg.fwol(), pmod=lkdg.pmod(), sdoe=lkdg.sdoe(), gboe=lkdg.gboe(), ccol=lkdg.ccol(),
        pairdata=lkdg.team.__pairdata__, pairtext=lkdg.team.__pairtext__,
        quaddata=lkdg.team.__quaddata__, quadtext=lkdg.team.__quadtext__,
        rare=[Rare.Star_1, Rare.Star_2, Rare.Star_3],
        file=lkdg.__name__.split(".")[-1]
    ),
    mdbv.team.__teamname__: ArtifactTeam(
        name=mdbv.team.__teamname__,
        fwol=mdbv.fwol(), pmod=mdbv.pmod(), sdoe=mdbv.sdoe(), gboe=mdbv.gboe(), ccol=mdbv.ccol(),
        pairdata=mdbv.team.__pairdata__, pairtext=mdbv.team.__pairtext__,
        quaddata=mdbv.team.__quaddata__, quadtext=mdbv.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=mdbv.__name__.split(".")[-1]
    ),
    mcht.team.__teamname__: ArtifactTeam(
        name=mcht.team.__teamname__,
        fwol=mcht.fwol(), pmod=mcht.pmod(), sdoe=mcht.sdoe(), gboe=mcht.gboe(), ccol=mcht.ccol(),
        pairdata=mcht.team.__pairdata__, pairtext=mcht.team.__pairtext__,
        quaddata=mcht.team.__quaddata__, quadtext=mcht.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=mcht.__name__.split(".")[-1]
    ),
    mtat.team.__teamname__: ArtifactTeam(
        name=mtat.team.__teamname__,
        fwol=mtat.fwol(), pmod=mtat.pmod(), sdoe=mtat.sdoe(), gboe=mtat.gboe(), ccol=mtat.ccol(),
        pairdata=mtat.team.__pairdata__, pairtext=mtat.team.__pairtext__,
        quaddata=mtat.team.__quaddata__, quadtext=mtat.team.__quadtext__,
        rare=[Rare.Star_3, Rare.Star_4],
        file=mtat.__name__.split(".")[-1]
    ),
    nwiw.team.__teamname__: ArtifactTeam(
        name=nwiw.team.__teamname__,
        fwol=nwiw.fwol(), pmod=nwiw.pmod(), sdoe=nwiw.sdoe(), gboe=nwiw.gboe(), ccol=nwiw.ccol(),
        pairdata=nwiw.team.__pairdata__, pairtext=nwiw.team.__pairtext__,
        quaddata=nwiw.team.__quaddata__, quadtext=nwiw.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=nwiw.__name__.split(".")[-1]
    ),
    nlob.team.__teamname__: ArtifactTeam(
        name=nlob.team.__teamname__,
        fwol=nlob.fwol(), pmod=nlob.pmod(), sdoe=nlob.sdoe(), gboe=nlob.gboe(), ccol=nlob.ccol(),
        pairdata=nlob.team.__pairdata__, pairtext=nlob.team.__pairtext__,
        quaddata=nlob.team.__quaddata__, quadtext=nlob.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=nlob.__name__.split(".")[-1]
    ),
    nmdr.team.__teamname__: ArtifactTeam(
        name=nmdr.team.__teamname__,
        fwol=nmdr.fwol(), pmod=nmdr.pmod(), sdoe=nmdr.sdoe(), gboe=nmdr.gboe(), ccol=nmdr.ccol(),
        pairdata=nmdr.team.__pairdata__, pairtext=nmdr.team.__pairtext__,
        quaddata=nmdr.team.__quaddata__, quadtext=nmdr.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=nmdr.__name__.split(".")[-1]
    ),
    odcx.team.__teamname__: ArtifactTeam(
        name=odcx.team.__teamname__,
        fwol=odcx.fwol(), pmod=odcx.pmod(), sdoe=odcx.sdoe(), gboe=odcx.gboe(), ccol=odcx.ccol(),
        pairdata=odcx.team.__pairdata__, pairtext=odcx.team.__pairtext__,
        quaddata=odcx.team.__quaddata__, quadtext=odcx.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=odcx.__name__.split(".")[-1]
    ),
    ochc.team.__teamname__: ArtifactTeam(
        name=ochc.team.__teamname__,
        fwol=ochc.fwol(), pmod=ochc.pmod(), sdoe=ochc.sdoe(), gboe=ochc.gboe(), ccol=ochc.ccol(),
        pairdata=ochc.team.__pairdata__, pairtext=ochc.team.__pairtext__,
        quaddata=ochc.team.__quaddata__, quadtext=ochc.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=ochc.__name__.split(".")[-1]
    ),
    plfm.team.__teamname__: ArtifactTeam(
        name=plfm.team.__teamname__,
        fwol=plfm.fwol(), pmod=plfm.pmod(), sdoe=plfm.sdoe(), gboe=plfm.gboe(), ccol=plfm.ccol(),
        pairdata=plfm.team.__pairdata__, pairtext=plfm.team.__pairtext__,
        quaddata=plfm.team.__quaddata__, quadtext=plfm.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=plfm.__name__.split(".")[-1]
    ),
    rosj.team.__teamname__: ArtifactTeam(
        name=rosj.team.__teamname__,
        fwol=rosj.fwol(), pmod=rosj.pmod(), sdoe=rosj.sdoe(), gboe=rosj.gboe(), ccol=rosj.ccol(),
        pairdata=rosj.team.__pairdata__, pairtext=rosj.team.__pairtext__,
        quaddata=rosj.team.__quaddata__, quadtext=rosj.team.__quadtext__,
        rare=[Rare.Star_3, Rare.Star_4],
        file=rosj.__name__.split(".")[-1]
    ),
    rcbl.team.__teamname__: ArtifactTeam(
        name=rcbl.team.__teamname__,
        fwol=rcbl.fwol(), pmod=rcbl.pmod(), sdoe=rcbl.sdoe(), gboe=rcbl.gboe(), ccol=rcbl.ccol(),
        pairdata=rcbl.team.__pairdata__, pairtext=rcbl.team.__pairtext__,
        quaddata=rcbl.team.__quaddata__, quadtext=rcbl.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=rcbl.__name__.split(".")[-1]
    ),
    sclr.team.__teamname__: ArtifactTeam(
        name=sclr.team.__teamname__,
        fwol=sclr.fwol(), pmod=sclr.pmod(), sdoe=sclr.sdoe(), gboe=sclr.gboe(), ccol=sclr.ccol(),
        pairdata=sclr.team.__pairdata__, pairtext=sclr.team.__pairtext__,
        quaddata=sclr.team.__quaddata__, quadtext=sclr.team.__quadtext__,
        rare=[Rare.Star_3, Rare.Star_4],
        file=sclr.__name__.split(".")[-1]
    ),
    shcc.team.__teamname__: ArtifactTeam(
        name=shcc.team.__teamname__,
        fwol=shcc.fwol(), pmod=shcc.pmod(), sdoe=shcc.sdoe(), gboe=shcc.gboe(), ccol=shcc.ccol(),
        pairdata=shcc.team.__pairdata__, pairtext=shcc.team.__pairtext__,
        quaddata=shcc.team.__quaddata__, quadtext=shcc.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=shcc.__name__.split(".")[-1]
    ),
    smrm.team.__teamname__: ArtifactTeam(
        name=smrm.team.__teamname__,
        fwol=smrm.fwol(), pmod=smrm.pmod(), sdoe=smrm.sdoe(), gboe=smrm.gboe(), ccol=smrm.ccol(),
        pairdata=smrm.team.__pairdata__, pairtext=smrm.team.__pairtext__,
        quaddata=smrm.team.__quaddata__, quadtext=smrm.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=smrm.__name__.split(".")[-1]
    ),
    sodp.team.__teamname__: ArtifactTeam(
        name=sodp.team.__teamname__,
        fwol=sodp.fwol(), pmod=sodp.pmod(), sdoe=sodp.sdoe(), gboe=sodp.gboe(), ccol=sodp.ccol(),
        pairdata=sodp.team.__pairdata__, pairtext=sodp.team.__pairtext__,
        quaddata=sodp.team.__quaddata__, quadtext=sodp.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=sodp.__name__.split(".")[-1]
    ),
    totm.team.__teamname__: ArtifactTeam(
        name=totm.team.__teamname__,
        fwol=totm.fwol(), pmod=totm.pmod(), sdoe=totm.sdoe(), gboe=totm.gboe(), ccol=totm.ccol(),
        pairdata=totm.team.__pairdata__, pairtext=totm.team.__pairtext__,
        quaddata=totm.team.__quaddata__, quadtext=totm.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=totm.__name__.split(".")[-1]
    ),
    texl.team.__teamname__: ArtifactTeam(
        name=texl.team.__teamname__,
        fwol=texl.fwol(), pmod=texl.pmod(), sdoe=texl.sdoe(), gboe=texl.gboe(), ccol=texl.ccol(),
        pairdata=texl.team.__pairdata__, pairtext=texl.team.__pairtext__,
        quaddata=texl.team.__quaddata__, quadtext=texl.team.__quadtext__,
        rare=[Rare.Star_3, Rare.Star_4],
        file=texl.__name__.split(".")[-1]
    ),
    tdfr.team.__teamname__: ArtifactTeam(
        name=tdfr.team.__teamname__,
        fwol=tdfr.fwol(), pmod=tdfr.pmod(), sdoe=tdfr.sdoe(), gboe=tdfr.gboe(), ccol=tdfr.ccol(),
        pairdata=tdfr.team.__pairdata__, pairtext=tdfr.team.__pairtext__,
        quaddata=tdfr.team.__quaddata__, quadtext=tdfr.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=tdfr.__name__.split(".")[-1]
    ),
    tdst.team.__teamname__: ArtifactTeam(
        name=tdst.team.__teamname__,
        fwol=tdst.fwol(), pmod=tdst.pmod(), sdoe=tdst.sdoe(), gboe=tdst.gboe(), ccol=tdst.ccol(),
        pairdata=tdst.team.__pairdata__, pairtext=tdst.team.__pairtext__,
        quaddata=tdst.team.__quaddata__, quadtext=tdst.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=tdst.__name__.split(".")[-1]
    ),
    tymc.team.__teamname__: ArtifactTeam(
        name=tymc.team.__teamname__,
        fwol=tymc.fwol(), pmod=tymc.pmod(), sdoe=tymc.sdoe(), gboe=tymc.gboe(), ccol=tymc.ccol(),
        pairdata=tymc.team.__pairdata__, pairtext=tymc.team.__pairtext__,
        quaddata=tymc.team.__quaddata__, quadtext=tymc.team.__quadtext__,
        rare=[Rare.Star_3, Rare.Star_4],
        file=tymc.__name__.split(".")[-1]
    ),
    tvdt.team.__teamname__: ArtifactTeam(
        name=tvdt.team.__teamname__,
        fwol=tvdt.fwol(), pmod=tvdt.pmod(), sdoe=tvdt.sdoe(), gboe=tvdt.gboe(), ccol=tvdt.ccol(),
        pairdata=tvdt.team.__pairdata__, pairtext=tvdt.team.__pairtext__,
        quaddata=tvdt.team.__quaddata__, quadtext=tvdt.team.__quadtext__,
        rare=[Rare.Star_1, Rare.Star_2, Rare.Star_3],
        file=tvdt.__name__.split(".")[-1]
    ),
    ufrv.team.__teamname__: ArtifactTeam(
        name=ufrv.team.__teamname__,
        fwol=ufrv.fwol(), pmod=ufrv.pmod(), sdoe=ufrv.sdoe(), gboe=ufrv.gboe(), ccol=ufrv.ccol(),
        pairdata=ufrv.team.__pairdata__, pairtext=ufrv.team.__pairtext__,
        quaddata=ufrv.team.__quaddata__, quadtext=ufrv.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=ufrv.__name__.split(".")[-1]
    ),
    vmha.team.__teamname__: ArtifactTeam(
        name=vmha.team.__teamname__,
        fwol=vmha.fwol(), pmod=vmha.pmod(), sdoe=vmha.sdoe(), gboe=vmha.gboe(), ccol=vmha.ccol(),
        pairdata=vmha.team.__pairdata__, pairtext=vmha.team.__pairtext__,
        quaddata=vmha.team.__quaddata__, quadtext=vmha.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=vmha.__name__.split(".")[-1]
    ),
    vdvn.team.__teamname__: ArtifactTeam(
        name=vdvn.team.__teamname__,
        fwol=vdvn.fwol(), pmod=vdvn.pmod(), sdoe=vdvn.sdoe(), gboe=vdvn.gboe(), ccol=vdvn.ccol(),
        pairdata=vdvn.team.__pairdata__, pairtext=vdvn.team.__pairtext__,
        quaddata=vdvn.team.__quaddata__, quadtext=vdvn.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=vdvn.__name__.split(".")[-1]
    ),
    vkgw.team.__teamname__: ArtifactTeam(
        name=vkgw.team.__teamname__,
        fwol=vkgw.fwol(), pmod=vkgw.pmod(), sdoe=vkgw.sdoe(), gboe=vkgw.gboe(), ccol=vkgw.ccol(),
        pairdata=vkgw.team.__pairdata__, pairtext=vkgw.team.__pairtext__,
        quaddata=vkgw.team.__quaddata__, quadtext=vkgw.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=vkgw.__name__.split(".")[-1]
    ),
    wdtp.team.__teamname__: ArtifactTeam(
        name=wdtp.team.__teamname__,
        fwol=wdtp.fwol(), pmod=wdtp.pmod(), sdoe=wdtp.sdoe(), gboe=wdtp.gboe(), ccol=wdtp.ccol(),
        pairdata=wdtp.team.__pairdata__, pairtext=wdtp.team.__pairtext__,
        quaddata=wdtp.team.__quaddata__, quadtext=wdtp.team.__quadtext__,
        rare=[Rare.Star_4, Rare.Star_5],
        file=wdtp.__name__.split(".")[-1]
    ),
    none.team.__teamname__: ArtifactTeam(
        name=none.team.__teamname__,
        fwol=none.fwol(), pmod=none.pmod(), sdoe=none.sdoe(), gboe=none.gboe(), ccol=none.ccol(),
        pairdata=none.team.__pairdata__, pairtext=none.team.__pairtext__,
        quaddata=none.team.__quaddata__, quadtext=none.team.__quadtext__,
        rare=[Rare.Star_0],
        file=none.__name__.split(".")[-1]
    ),
}


ArtiList = Enum(
    "ArtifactList",
    {
        item.replace(" ", "_").replace("'", "").replace("-", "_"): data for item, data in __artilist__.items()
    }
)
