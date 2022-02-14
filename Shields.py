import random
from LevelTier import level_tier

guilds_shield = {
1: 'Ashen',
2: 'Alas',
3: 'Dahlia',
4: 'Feriore',
5: 'Malefactor',
6: 'Pangoblin',
7: 'Stoker',
8: 'Torgue'
    }

tier1_shield = {
'Ashen' : 'Capacity: 30    Recharge: 15    Fast Recharge Rate',
'Alas' : 'Capacity: 30    Recharge: 10    1d4 Shock Resistance',
'Dahlia' : 'Capacity: 30    Recharge: 10    1d4 Corrosive Resistance',
'Feriore' : 'Capacity: 30    Recharge: 10    1d4 Health Regen per Recharge',
'Malefactor' : 'Capacity: 30    Recharge: 10    When depleted, 1d6 Shock damage to adjacent targets',
'Pangoblin' : 'Capacity: 40    Recharge: 5    High Capacity',
'Stoker' : 'Capacity: 30    Recharge: 10    When depleted, 1d6 Incendiary damage to adjacent targets',
'Torgue' : 'Capacity 30    Recharge: 10    Gain 10 Max Health',
    }

tier2_shield = {
'Ashen' : 'Capacity: 55    Recharge: 20    Fast Recharge Rate',
'Alas' : 'Capacity: 55    Recharge: 20    1d6 Shock Resistance',
'Dahlia' : 'Capacity: 55    Recharge: 15    1d6 Corrosive Resistance',
'Feriore' : 'Capacity: 50    Recharge: 15    1d6 Health Regen per Recharge',
'Malefactor' : 'Capacity: 50    Recharge: 15    When depleted, 2d6 Shock damage to adjacent targets',
'Pangoblin' : 'Capacity: 60    Recharge: 10    High Capacity',
'Stoker' : 'Capacity: 50    Recharge: 15    When depleted, 2d6 Incendiary damage to adjacent targets',
'Torgue' : 'Capacity 50    Recharge: 15    Gain 20 Max Health',
    }

tier3_shield = {
'Ashen' : 'Capacity: 70    Recharge: 25    Fast Recharge Rate',
'Alas' : 'Capacity: 70    Recharge: 20    1d10 Shock Resistance',
'Dahlia' : 'Capacity: 75    Recharge: 20    1d10 Corrosive Resistance',
'Feriore' : 'Capacity: 70    Recharge: 20    1d8 Health Regen per Recharge',
'Malefactor' : 'Capacity: 70    Recharge: 20    When depleted, 3d6 Shock damage to adjacent targets',
'Pangoblin' : 'Capacity: 80    Recharge: 20    High Capacity',
'Stoker' : 'Capacity: 70    Recharge: 20    When depleted, 3d6 Incendiary damage to adjacent targets',
'Torgue' : 'Capacity 70    Recharge: 20    Gain 30 Max Health',
    }

tier4_shield = {
'Ashen' : 'Capacity: 70    Recharge: 15    Gain +30 Max Health and +3 Melee Damage while equipped.',
'Alas' : 'Capacity: 60    Recharge: 10    Roll d100 for each incoming Attack. On a 60+, take Half Damage.',
'Dahlia' : 'Capacity: 80    Recharge: 10    When depleted during an encounter, drops 20 gold.',
'Feriore' : 'Capacity: 70    Recharge: 20    Recharge 5 Shield at the start of each turn.',
'Malefactor' : 'Capacity: 70    Recharge: 15    When depleted, pulls targets up to 3 squares away into an adjacent square then deals 4d6 damage to adjacent targets.',
'Pangoblin' : 'Capacity: 100    Recharge: 20    Reduces Movement to 2 squares unless depleted.',
'Stoker' : 'Capacity: 70    Recharge: 15    Shock Damage Recharges the Shield instead of Damaging it.',
'Torgue' : 'Capacity 75    Recharge: 15    Insults an Enemy as Mr. torgue each turn, dealing 1d4 damage and Taunting the Enemy.',
    }

tier5_shield = {
'Ashen' : 'Capacity: 60    Recharge: 10    Gain +30 Max Health and +10 Health Regen while equipped.',
'Alas' : 'Capacity: 0    Recharge: 0    Roll d100 for each incoming Attack. On a 70+, take No Damage.',
'Dahlia' : 'Capacity: 80    Recharge: 15    When depleted, spawns 3 grenades into adjacent squares that each deal 3d6 Shock Damage.',
'Feriore' : 'Capacity: 60    Recharge: 20    When depleted, toss like a grenade, dealing 3d8 damage then returning.',
'Malefactor' : 'Capacity: 80    Recharge: 15    Deals 2d6 Incendiary Damage to adjacent squares each turn while depleted.',
'Pangoblin' : 'Capacity: 60    Recharge: 10    Gain +4 DMG Mod to Ranged Attacks while not depleted.',
'Stoker' : 'Capacity: 80    Recharge: 15    Launches 3 Corrosive spikes at the target if you take 10 or more damage from an Attack.  Each spike deals 1d6 Corrosive damage.',
'Torgue' : 'Capacity 80    Recharge: 15    When depleted, creates a 3x3 square area blast dealing 3d6 Explosive damage and causing Knockback.',
    }


def shield_gen(n):
    tier = level_tier(n)
    guild = guilds_shield[(random.randint(1,8))]
    if tier == 1:
        shield = tier1_shield[guild]
    elif tier == 2:
        shield = tier2_shield[guild]
    elif tier == 3:
        shield = tier3_shield[guild]
    elif tier == 4:
        shield = tier4_shield[guild]
    elif tier == 5:
        shield = tier5_shield[guild]
    return shield
