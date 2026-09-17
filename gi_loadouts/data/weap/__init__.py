from ..weap import bows, catalysts, claymores, polearms, swords
from .bows.hymn_of_the_maelstrom import HymnOfTheMaelstrom


__bowsdict__ = {
    **bows.BowsDict,
    "Hymn of the Maelstrom": HymnOfTheMaelstrom,
}

Family = {
    "Bow": __bowsdict__,
    "Catalyst": catalysts.CatalystsDict,
    "Claymore": claymores.ClaymoresDict,
    "Polearm": polearms.PolearmsDict,
    "Sword": swords.SwordsDict,
}
