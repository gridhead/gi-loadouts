from ....type.rare import Rare
from ....type.weap import Claymore, WeaponStat, WeaponStatType
from ....type.weap.tier import Tier


class ForgedByTheGoldenMelody(Claymore):
    name: str = "Forged by the Golden Melody"
    seco_stat: WeaponStat = WeaponStat(stat_name=WeaponStatType.critical_rate_perc, stat_data=6.0)
    tier: Tier = Tier.Tier_2
    rare: Rare = Rare.Star_4
    refi_name: str = "Day and Night in Counterpoint"
    refi_list: list[str] = [
        "Every 10s, the equipping character plays a \"Harmonic Movement\" of the corresponding type for a boost in the following order: +18% ATK > +120 Elemental Mastery > +28% Stellar Glimmer reaction DMG. Each instance of Harmonic Movement lasts 10s. This effect can trigger even when the equipping character is not on the field. \nTriggering a Stellar Glimmer reaction will also grant an additional 12-second instance of \"Harmonic Movement: Contrapuntal\" with the same effects as the Harmonic Movement active when Stellar Glimmer is triggered. This effect stacks with the original Harmonic Movement effect, and can trigger once every 12s.",
        "Every 10s, the equipping character plays a \"Harmonic Movement\" of the corresponding type for a boost in the following order: +22.5% ATK > +150 Elemental Mastery > +35% Stellar Glimmer reaction DMG. Each instance of Harmonic Movement lasts 10s. This effect can trigger even when the equipping character is not on the field. \nTriggering a Stellar Glimmer reaction will also grant an additional 12-second instance of \"Harmonic Movement: Contrapuntal\" with the same effects as the Harmonic Movement active when Stellar Glimmer is triggered. This effect stacks with the original Harmonic Movement effect, and can trigger once every 12s.",
        "Every 10s, the equipping character plays a \"Harmonic Movement\" of the corresponding type for a boost in the following order: +27% ATK > +180 Elemental Mastery > +42% Stellar Glimmer reaction DMG. Each instance of Harmonic Movement lasts 10s. This effect can trigger even when the equipping character is not on the field. \nTriggering a Stellar Glimmer reaction will also grant an additional 12-second instance of \"Harmonic Movement: Contrapuntal\" with the same effects as the Harmonic Movement active when Stellar Glimmer is triggered. This effect stacks with the original Harmonic Movement effect, and can trigger once every 12s.",
        "Every 10s, the equipping character plays a \"Harmonic Movement\" of the corresponding type for a boost in the following order: +31.5% ATK > +210 Elemental Mastery > +49% Stellar Glimmer reaction DMG. Each instance of Harmonic Movement lasts 10s. This effect can trigger even when the equipping character is not on the field. \nTriggering a Stellar Glimmer reaction will also grant an additional 12-second instance of \"Harmonic Movement: Contrapuntal\" with the same effects as the Harmonic Movement active when Stellar Glimmer is triggered. This effect stacks with the original Harmonic Movement effect, and can trigger once every 12s.",
        "Every 10s, the equipping character plays a \"Harmonic Movement\" of the corresponding type for a boost in the following order: +36% ATK > +240 Elemental Mastery > +56% Stellar Glimmer reaction DMG. Each instance of Harmonic Movement lasts 10s. This effect can trigger even when the equipping character is not on the field. \nTriggering a Stellar Glimmer reaction will also grant an additional 12-second instance of \"Harmonic Movement: Contrapuntal\" with the same effects as the Harmonic Movement active when Stellar Glimmer is triggered. This effect stacks with the original Harmonic Movement effect, and can trigger once every 12s.",
    ]
    file: str = "fbgm"
