from ....type.rare import Rare
from ....type.weap import Sword, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class MoonweaversDawn(Sword):
    name: str = "Moonweaver's Dawn"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_3
    rare: Rare = Rare.Star_4
    refi_name: str = "Secret Silver's Testament"
    refi_list: list[str] = [
        "Increases Elemental Burst DMG by 20%. When the character's Energy Capacity does not exceed 60, Elemental Burst DMG increases by an additional 16%. When the character's Energy Capacity does not exceed 40, Elemental Burst DMG increases by an additional 28%.",
        "Increases Elemental Burst DMG by 25%. When the character's Energy Capacity does not exceed 60, Elemental Burst DMG increases by an additional 20%. When the character's Energy Capacity does not exceed 40, Elemental Burst DMG increases by an additional 35%.",
        "Increases Elemental Burst DMG by 30%. When the character's Energy Capacity does not exceed 60, Elemental Burst DMG increases by an additional 24%. When the character's Energy Capacity does not exceed 40, Elemental Burst DMG increases by an additional 42%.",
        "Increases Elemental Burst DMG by 35%. When the character's Energy Capacity does not exceed 60, Elemental Burst DMG increases by an additional 28%. When the character's Energy Capacity does not exceed 40, Elemental Burst DMG increases by an additional 49%.",
        "Increases Elemental Burst DMG by 40%. When the character's Energy Capacity does not exceed 60, Elemental Burst DMG increases by an additional 32%. When the character's Energy Capacity does not exceed 40, Elemental Burst DMG increases by an additional 56%.",
    ]
    file: str = "mwdn"
