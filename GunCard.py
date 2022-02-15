from LevelTier import level_tier
#-------Gun Card Here-----------
gun_type = {
1: 'Pistol',
2: 'Submachine Gun',
3: 'Shotgun',
4: 'Combat Rifle',
5: 'Sniper Rifle',
6: 'Rocket Launcher',
    }

tier1_gun = {
'Pistol' : '102030:2d4:5',
'Submachine Gun' : '203050:d4:5',
'Shotgun' : '102011:1d8:4',
'Combat Rifle' : '1103021:1d6:6',
'Sniper Rifle' : '001011:1d10:8',
'Rocket Launcher' : '101011:1d12:4'
    }

tier2_gun = {
'Pistol' : '101131:1d6:5',
'Submachine Gun' : '204051:2d4:5',
'Shotgun' : '102021:2d8:4',
'Combat Rifle' : '203021:1d8:6',
'Sniper Rifle' : '001011:1d12:8',
'Rocket Launcher' : '101011:2d10:4'
    }

tier3_gun = {
'Pistol' : '102021:2d6:5',
'Submachine Gun' : '203151:1d6:5',
'Shotgun' : '112122:1d8:4',
'Combat Rifle' : '112122:1d8:6',
'Sniper Rifle' : '101112:1d10:8',
'Rocket Launcher' : '101012:1d12:4'
    }

tier4_gun = {
'Pistol' : '101112:2d8:5',
'Submachine Gun' : '202141:2d6:5',
'Shotgun' : '101121:2d10:4',
'Combat Rifle' : '102131:2d6:6',
'Sniper Rifle' : '101112:2d10:8',
'Rocket Launcher' : '101122:1d12:4'
    }

tier5_gun = {
'Pistol' : '202122:2d8:5',
'Submachine Gun' : '223252:1d10:5',
'Shotgun' : '112122:1d12:4',
'Combat Rifle' : '112123:1d10:6',
'Sniper Rifle' : '101122:1d12:8',
'Rocket Launcher' : '111121:1d20:4'
    }

def stat_gen(n, gun):
    tier = level_tier(n)
    #gun = gun_type[random.randint(1,6)]
    if tier == 1:
        gun_card = tier1_gun[gun]
    elif tier == 2:
        gun_card = tier2_gun[gun]
    elif tier == 3:
        gun_card = tier3_gun[gun]
    elif tier == 4:
        gun_card = tier4_gun[gun]
    elif tier == 5:
        gun_card = tier5_gun[gun]

    dmg, die, dist = gun_card.split(':')
    '''
    print("\nAcc |  2  -  7  |  8 - 15   |   16+     | DMG | Range")
    print("-----------------------------------------------------")
    print("    | Hit  Crit | Hit  Crit | Hit  Crit |     |      ")
    print("    |  " + dmg[0] + "     " + dmg[1] + "  |  " + dmg[2] + "     " + dmg[3] + "  |  " + dmg[4] + "     " + dmg[5] + "  | " + die  + " |  " + dist)
    bad_variable = "\nAcc |  2  -  7  |  8 - 15   |   16+     | DMG | Range\n-----------------------------------------------------\n    | Hit  Crit | Hit  Crit | Hit  Crit |     |      \n    |  " + dmg[0] + "     " + dmg[1] + "  |  " + dmg[2] + "     " + dmg[3] + "  |  " + dmg[4] + "     " + dmg[5] + "  | " + die  + " |  " + dist
    '''
    return dmg, die, dist
