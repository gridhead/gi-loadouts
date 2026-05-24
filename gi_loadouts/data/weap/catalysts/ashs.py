from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class AngelosHeptades(Catalyst):
    name: str = "Angelos' Heptades"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=3.6)
    tier: Tier = Tier.Tier_4
    rare: Rare = Rare.Star_5
    refi_name: str = "Crown of the Final Scion"
    refi_list: list[str] = [
        "ATK is increased by 12%. After the equipping character creates a Shield, they gain \"Pathfinder's Light\" for 20s: Increases your active party member's DMG by 10% for every 1,000 ATK the equipping character has, up to a maximum of 26%. Additionally, when the equipping character creates a Shield, they will also gain \"Guide's Contentment\": Restores 14 Elemental Energy to the equipping character. The aforementioned effect can trigger once every 14s, and can also be triggered when any type of chest is opened outside of combat. The equipping character may trigger this effect even when they are an off-field.\n\nHexerei: Secret Rite: When your own Hexerei character is off-field in the party, they will also gain 50% of the DMG increase from Pathfinder's Light.",
        "ATK is increased by 15%. After the equipping character creates a Shield, they gain \"Pathfinder's Light\" for 20s: Increases your active party member's DMG by 13% for every 1,000 ATK the equipping character has, up to a maximum of 34%. Additionally, when the equipping character creates a Shield, they will also gain \"Guide's Contentment\": Restores 15 Elemental Energy to the equipping character. The aforementioned effect can trigger once every 14s, and can also be triggered when any type of chest is opened outside of combat. The equipping character may trigger this effect even when they are an off-field.\n\nHexerei: Secret Rite: When your own Hexerei character is off-field in the party, they will also gain 50% of the DMG increase from Pathfinder's Light.",
        "ATK is increased by 18%. After the equipping character creates a Shield, they gain \"Pathfinder's Light\" for 20s: Increases your active party member's DMG by 16% for every 1,000 ATK the equipping character has, up to a maximum of 42%. Additionally, when the equipping character creates a Shield, they will also gain \"Guide's Contentment\": Restores 16 Elemental Energy to the equipping character. The aforementioned effect can trigger once every 14s, and can also be triggered when any type of chest is opened outside of combat. The equipping character may trigger this effect even when they are an off-field.\n\nHexerei: Secret Rite: When your own Hexerei character is off-field in the party, they will also gain 50% of the DMG increase from Pathfinder's Light.",
        "ATK is increased by 21%. After the equipping character creates a Shield, they gain \"Pathfinder's Light\" for 20s: Increases your active party member's DMG by 19% for every 1,000 ATK the equipping character has, up to a maximum of 50%. Additionally, when the equipping character creates a Shield, they will also gain \"Guide's Contentment\": Restores 17 Elemental Energy to the equipping character. The aforementioned effect can trigger once every 14s, and can also be triggered when any type of chest is opened outside of combat. The equipping character may trigger this effect even when they are an off-field.\n\nHexerei: Secret Rite: When your own Hexerei character is off-field in the party, they will also gain 50% of the DMG increase from Pathfinder's Light.",
        "ATK is increased by 24%. After the equipping character creates a Shield, they gain \"Pathfinder's Light\" for 20s: Increases your active party member's DMG by 22% for every 1,000 ATK the equipping character has, up to a maximum of 58%. Additionally, when the equipping character creates a Shield, they will also gain \"Guide's Contentment\": Restores 18 Elemental Energy to the equipping character. The aforementioned effect can trigger once every 14s, and can also be triggered when any type of chest is opened outside of combat. The equipping character may trigger this effect even when they are an off-field.\n\nHexerei: Secret Rite: When your own Hexerei character is off-field in the party, they will also gain 50% of the DMG increase from Pathfinder's Light.",
    ]
    refi_stat: list[list[WeaponStat]] = [
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=12.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=15.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=18.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=21.0)],
        [WeaponStat(stat_name=WeaponStatType.attack_perc, stat_data=24.0)],
    ]
    file: str = "ashs"
