from enum import Enum


class Vision(str, Enum):
    anemo = "Anemo"
    cryo = "Cryo"
    dendro = "Dendro"
    electro = "Electro"
    geo = "Geo"
    hydro = "Hydro"
    pyro = "Pyro"
    none = "None"


__visioncolour__ = {
    Vision.anemo: "rgba(126, 212, 184, 128)",
    Vision.cryo: "rgba(164, 226, 240, 128)",
    Vision.dendro: "rgba(166, 202, 56, 128)",
    Vision.electro: "rgba(180, 139, 202, 128)",
    Vision.geo: "rgba(222, 188, 108, 128)",
    Vision.hydro: "rgba(0, 190, 255, 128)",
    Vision.pyro: "rgba(240, 122, 52, 128)",
    Vision.none: "rgba(128, 128, 128, 128)",
}
