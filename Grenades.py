import random
from LevelTier import level_tier


guilds_grenade = {
1: 'Ashen',
2: 'Dahlia',
3: 'Feriore',
4: 'Hyperius',
5: 'Malefactor',
6: 'Pangoblin',
7: 'Stoker',
8: 'Torgue'
    }

tier1_grenade = {
'Ashen' : 'Transfusion - Gain Health equal to Damage dealt. 1d8',
'Dahlia' : 'Generator - Recharges Shields equal to Damage dealt. 1d8',
'Feriore' : 'Jumping - Detonates, then jumps 2 squares and detonates again. 1d8',
'Hyperius' : 'Longbow - Teleports to Target. Ignores Cover. 1d8',
'Malefactor' : 'Elemental - Gains Elemental Type. 1d8',
'Pangoblin' : 'Rubberized - Bounce of surfaces. Detonates onn contact with any Target. 1d8',
'Stoker' : 'Proximity Mine - Wont detonate until target is adjacent. 1d8',
'Torgue' : 'Splash - Deals full Splash Damage. 1d8',
    }

tier2_grenade = {
'Ashen' : 'Homing - Automatically hits closest tartget. 2d8',
'Dahlia' : 'Bouncing Betty - Detonates in target quare for 2 turns. 2d8',
'Feriore' : 'Sticky - Sticks to surfaces. Deonates after 1 turn. 2d8',
'Hyperius' : 'Roider - Increased Damage. 2d10',
'Malefactor' : 'Contact - Detonates on contact with target. 2d8',
'Pangoblin' : 'Force - Targets Hit are Knocked Back 1 square. 2d8',
'Stoker' : 'Rain - Launches up and eals Damage downward in a 2x2 square area. 2d8',
'Torgue' : 'MIRV - Splits into 3 grenades. 2d8',
    }

tier3_grenade = {
'Ashen' : 'Transfusion - Gain Health equal to Damage dealt. 3d8',
'Dahlia' : 'Generator - Recharges Shields equal to Damage dealt. 3d8',
'Feriore' : 'Jumping - Detonates, then jumps 2 squares and detonates again. 3d8',
'Hyperius' : 'Longbow - Teleports to Target. Ignores Cover. 3d8',
'Malefactor' : 'Elemental - Gains Elemental Type. 3d8',
'Pangoblin' : 'Rubberized - Bounce of surfaces. Detonates onn contact with any Target. 3d8',
'Stoker' : 'Proximity Mine - Wont detonate until target is adjacent. 3d8',
'Torgue' : 'Splash - Deals full Splash Damage. 3d8',
    }

tier4_grenade = {
'Ashen' : 'Homing - Automatically hits closest tartget. 4d8',
'Dahlia' : 'Bouncing Betty - Detonates in target quare for 2 turns. 4d8',
'Feriore' : 'Sticky - Sticks to surfaces. Deonates after 1 turn. 4d8',
'Hyperius' : 'Roider - Increased Damage. 4d10',
'Malefactor' : 'Contact - Detonates on contact with target. 4d8',
'Pangoblin' : 'Force - Targets Hit are Knocked Back 1 square. 4d8',
'Stoker' : 'Rain - Launches up and eals Damage downward in a 2x2 square area. 4d8',
'Torgue' : 'MIRV - Splits into 3 grenades. 4d8',
    }

tier5_grenade = {
'Ashen' : 'Transfusion - Gain Health equal to Damage dealt. 5d8',
'Dahlia' : 'Generator - Recharges Shields equal to Damage dealt. 5d8',
'Feriore' : 'Jumping - Detonates, then jumps 2 squares and detonates again. 5d8',
'Hyperius' : 'Longbow - Teleports to Target. Ignores Cover. 5d8',
'Malefactor' : 'Elemental - Gains Elemental Type. 5d8',
'Pangoblin' : 'Rubberized - Bounce of surfaces. Detonates onn contact with any Target. 5d8',
'Stoker' : 'Proximity Mine - Wont detonate until target is adjacent. 5d8',
'Torgue' : 'Splash - Deals full Splash Damage. 5d8',
    }


def grenade_gen(n):
    tier = level_tier(n)
    guild = guilds_grenade[(random.randint(1,8))]
    #print(guild, level_tier(n))
    if tier == 1:
        grenade = tier1_grenade[guild]
    elif tier == 2:
        grenade = tier2_grenade[guild]
    elif tier == 3:
        grenade = tier3_grenade[guild]
    elif tier == 4:
        grenade = tier4_grenade[guild]
    elif tier == 5:
        grenade = tier5_grenade[guild]
    return grenade



