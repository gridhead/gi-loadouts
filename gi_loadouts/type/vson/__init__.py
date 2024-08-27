from enum import Enum

from pydantic import BaseModel


class VisionType(BaseModel):
    name: str = ""
    colour: str = ""


class Vision(Enum):
    anemo = VisionType(name="Anemo", colour="rgba(126, 212, 184, 128)")
    cryo = VisionType(name="Cryo", colour="rgba(164, 226, 240, 128)")
    dendro = VisionType(name="Dendro", colour="rgba(166, 202, 56, 128)")
    electro = VisionType(name="Electro", colour="rgba(180, 139, 202, 128)")
    geo = VisionType(name="Geo", colour="rgba(222, 188, 108, 128)")
    hydro = VisionType(name="Hydro", colour="rgba(0, 190, 254, 128)")
    pyro = VisionType(name="Pyro", colour="rgba(240, 122, 52, 128)")
    none = VisionType(name="None", colour="rgba(128, 128, 128, 128)")
