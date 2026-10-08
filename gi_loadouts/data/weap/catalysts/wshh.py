from ....type.rare import Rare
from ....type.weap import Catalyst, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class WintersHeavyHeart(Catalyst):
    name: str = "Winter's Heavy Heart"
    seco_stat: WeaponStat = WeaponStat(
        stat_name=WeaponStatType.critical_damage_perc, stat_data=12.0
    )
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Secrets of Frost"
    refi_list: list[str] = [
        "The equipping character gains \"Silver-Tinged Blood Pact\": The equipping character's Elemental Mastery is increased by 24 for every Cryo character present in the party. For every Electro character present in the party, the equipping character's ATK is increased by 4.8%. Up to 4 Cryo or Electro characters can provide the above buffs.\nRadiance: Stellar Glimmer: The effect of Silver-Tinged Blood Pact is changed to: For every Cryo or Electro character present in the party, the equipping character gains a 20-point Elemental Mastery boost and deals 6% increased Stellar Glimmer reaction DMG.",
        "The equipping character gains \"Silver-Tinged Blood Pact\": The equipping character's Elemental Mastery is increased by 30 for every Cryo character present in the party. For every Electro character present in the party, the equipping character's ATK is increased by 6%. Up to 4 Cryo or Electro characters can provide the above buffs.\nRadiance: Stellar Glimmer: The effect of Silver-Tinged Blood Pact is changed to: For every Cryo or Electro character present in the party, the equipping character gains a 25-point Elemental Mastery boost and deals 7.5% increased Stellar Glimmer reaction DMG.",
        "The equipping character gains \"Silver-Tinged Blood Pact\": The equipping character's Elemental Mastery is increased by 36 for every Cryo character present in the party. For every Electro character present in the party, the equipping character's ATK is increased by 7.2%. Up to 4 Cryo or Electro characters can provide the above buffs.\nRadiance: Stellar Glimmer: The effect of Silver-Tinged Blood Pact is changed to: For every Cryo or Electro character present in the party, the equipping character gains a 30-point Elemental Mastery boost and deals 9% increased Stellar Glimmer reaction DMG.",
        "The equipping character gains \"Silver-Tinged Blood Pact\": The equipping character's Elemental Mastery is increased by 42 for every Cryo character present in the party. For every Electro character present in the party, the equipping character's ATK is increased by 8.4%. Up to 4 Cryo or Electro characters can provide the above buffs.\nRadiance: Stellar Glimmer: The effect of Silver-Tinged Blood Pact is changed to: For every Cryo or Electro character present in the party, the equipping character gains a 35-point Elemental Mastery boost and deals 10.5% increased Stellar Glimmer reaction DMG.",
        "The equipping character gains \"Silver-Tinged Blood Pact\": The equipping character's Elemental Mastery is increased by 48 for every Cryo character present in the party. For every Electro character present in the party, the equipping character's ATK is increased by 9.6%. Up to 4 Cryo or Electro characters can provide the above buffs.\nRadiance: Stellar Glimmer: The effect of Silver-Tinged Blood Pact is changed to: For every Cryo or Electro character present in the party, the equipping character gains a 40-point Elemental Mastery boost and deals 12% increased Stellar Glimmer reaction DMG.",
    ]
    file: str = "wshh"
