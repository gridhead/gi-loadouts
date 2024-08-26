from enum import Enum

from pydantic import BaseModel


class ConsType(BaseModel):
    name: str = "Constellation 0"
    data: int = 0


__cons__ = {
    "Constellation 0": ConsType(name="Constellation 0", data=0),
    "Constellation 1": ConsType(name="Constellation 1", data=1),
    "Constellation 2": ConsType(name="Constellation 2", data=2),
    "Constellation 3": ConsType(name="Constellation 3", data=3),
    "Constellation 4": ConsType(name="Constellation 4", data=4),
    "Constellation 5": ConsType(name="Constellation 5", data=5),
    "Constellation 6": ConsType(name="Constellation 6", data=6),
}


Cons = Enum(
    "Cons",
    {
        item.replace(" ", "_"): data for item, data in __cons__.items()
    }
)
