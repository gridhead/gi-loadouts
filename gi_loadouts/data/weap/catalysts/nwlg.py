from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class NightweaversLookingGlass(Catalyst):
    name: str = "Nightweaver's Looking Glass"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.elemental_mastery, stat_data=57.6)
    tier: Tier = Tier.Tier_1
    rare: Rare = Rare.Star_5
    refi_name: str = "Millennial Hymn"
    refi_list: list[str] = [
        "When the character uses Hydro/Dendro Elemental Skill, they gain 'Prayer of the Far North' (+60 EM for 4.5s). When party members trigger Lunar-Bloom reactions, they gain 'New Moon Verse' (+60 EM for 10s). When both effects are active, party members receive: Bloom DMG +120%, Hyperbloom/Burgeon DMG +80%, Lunar-Bloom DMG +40%.",
        "When the character uses Hydro/Dendro Elemental Skill, they gain 'Prayer of the Far North' (+75 EM for 4.5s). When party members trigger Lunar-Bloom reactions, they gain 'New Moon Verse' (+75 EM for 10s). When both effects are active, party members receive: Bloom DMG +150%, Hyperbloom/Burgeon DMG +100%, Lunar-Bloom DMG +50%.",
        "When the character uses Hydro/Dendro Elemental Skill, they gain 'Prayer of the Far North' (+90 EM for 4.5s). When party members trigger Lunar-Bloom reactions, they gain 'New Moon Verse' (+90 EM for 10s). When both effects are active, party members receive: Bloom DMG +180%, Hyperbloom/Burgeon DMG +120%, Lunar-Bloom DMG +60%.",
        "When the character uses Hydro/Dendro Elemental Skill, they gain 'Prayer of the Far North' (+105 EM for 4.5s). When party members trigger Lunar-Bloom reactions, they gain 'New Moon Verse' (+105 EM for 10s). When both effects are active, party members receive: Bloom DMG +210%, Hyperbloom/Burgeon DMG +140%, Lunar-Bloom DMG +70%.",
        "When the character uses Hydro/Dendro Elemental Skill, they gain 'Prayer of the Far North' (+120 EM for 4.5s). When party members trigger Lunar-Bloom reactions, they gain 'New Moon Verse' (+120 EM for 10s). When both effects are active, party members receive: Bloom DMG +240%, Hyperbloom/Burgeon DMG +160%, Lunar-Bloom DMG +80%.",
    ]
    file: str = "nwlg"
