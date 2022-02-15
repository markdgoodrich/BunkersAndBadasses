import random
from LevelTier import level_tier


#Enemy drop drop
#numbe ro floot piles is related to the badass rank
# gold, potions, gernades, relic, shield, gun

#input badass rank







#Chest loot



#Gun randomizer
#2d8 - Item type & Guild
#       assign guild bonus
#       If favored gun - tailor to players
#1d4 + 1d6 for rarity and elemental
#       if elemental, roll % on elemental table
#Add prefix
#Fill in gun stats based on Player level
#

gun_type = {
1: 'Pistol',
2: 'Submachine Gun',
3: 'Shotgun',
4: 'Combat Rifle',
5: 'Sniper Rifle',
6: 'Rocket Launcher',
    }

guilds = {
1: 'Alas',
2: 'Dahlia',
3: 'Hyperius',
4: 'Malefactor',
5: 'Feriore',
6: 'Stoker',
7: 'Torgue',
8: 'Blackpowder',
9: 'Skuldugger'
    }


def guild_stat():
    guild = guilds[(random.randint(1,9))]
    return guild

#roll a d4 then d6. combine string values
#11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26
#if elemental, need to roll elemental table too. based on rarity...
#       percentile
#if rarity ends in 'E', roll on elemntal table
#if rarity_table[] == 'E'
rarity_table = {
11: 'Common',
12: 'CommonE',
13: 'CommonE',
14: 'Uncommon',
15: 'UncommonE',
16: 'Rare',
21: 'Common',
22: 'CommonE',
23: 'Uncommon',
24: 'UncommonE',
25: 'RareE',
26: 'Epic',
31: 'UncommonE',
32: 'Rare',
33: 'RareE',
34: 'Epic',
35: 'EpicE',
36: 'LegendaryE',
41: 'RareE',
42: 'RareE',
43: 'EpicE',
44: 'EpicE',
45: 'LegendaryE',
46: 'LegendaryE'
    }




def gun_generator(n):
    tier= level_tier(n)
    gun = gun_type[random.randint(1,6)]
    guild = guilds[(random.randint(1,8))]
    rare = rarity_table[int(str(random.randint(1,4))+str(random.randint(1,6)))]
    #print(guild, gun ,rare)
    if guild == 'Alas' or guild == 'Blackpowder':
        if rare[-1] == 'E':
            rare = rare[:-1]
        return  guild + ' ' + gun + '(' + rare + ')', bonuses(guild, rare)# + stat_gen(tier, gun)
    elif rare[-1] == 'E':
        if rare[-1] == 'E':
            rare = rare[:-1]
        #else:
        #   pass
        return element_picker(gun, guild, rare), bonuses(guild, rare)#+ stat_gen(tier, gun)
    else:
        return  guild + ' ' + gun + '(' + rare + ')', bonuses(guild,rare)#+ stat_gen(tier, gun)
        
def element_picker(gun, guild, rare):        
    ele_roll = random.randint(1,100) 
    if rare == 'Common':
        if ele_roll == 99 or ele_roll == 100:
            return 'Cyro' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 97 or ele_roll == 98:
            return 'Incendiary' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 95 or ele_roll == 96:
            return 'Explosive' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 93 or ele_roll == 94:
            return 'Shock' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 91 or ele_roll == 92:
            return 'Corrosive' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 90 and ele_roll >= 86:
            return 'Radiation'  + guild + ' ' + gun + '(' + rare + ')'
        else:
            return guild + ' ' + gun + '(' + rare + ')'
    elif rare == 'Uncommon':
        if ele_roll == 99 or ele_roll == 100:
            return 'Cyro (+1d6)'  + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 97 or ele_roll == 98:
            return 'Incendiary (+1d6)'  + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 95 or ele_roll == 96:
            return 'Explosive (+1d6)' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 93 or ele_roll == 94:
            return 'Shock (+1d6)' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 91 or ele_roll == 92:
            return 'Corrosive (+1d6)' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 90 and ele_roll >= 86:
            return 'Radiation (+1d6)' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 85 and ele_roll >= 81:
            return 'Cyro' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 80 and ele_roll >= 76:
            return 'Incendiary'  + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 75 and ele_roll >= 71:
            return 'Explosive' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 70 and ele_roll >= 66:
            return 'Shock' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 65 and ele_roll >= 61:
            return 'Corrosive' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 60 and ele_roll >= 56:
            return 'Radiation' + guild + ' ' + gun + '(' + rare + ')'
        else:
            return guild + ' ' + gun + '(' + rare + ')'
    elif rare == 'Rare':
        if ele_roll == 99 or ele_roll == 100:
            return 'Cyro (+2d6)' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 97 or ele_roll == 98:
            return 'Incendiary (+2d6)' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 95 or ele_roll == 96:
            return 'Explosive (+2d6)' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 93 or ele_roll == 94:
            return 'Shock (+2d6)' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 91 or ele_roll == 92:
            return 'Corrosive (+2d6)' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 90 and ele_roll >= 86:
            return 'Radiation (+2d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 85 and ele_roll >= 81:
            return 'Cyro (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 80 and ele_roll >= 76:
            return 'Incendiary (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 75 and ele_roll >= 71:
            return 'Explosive (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 70 and ele_roll >= 66:
            return 'Shock (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 65 and ele_roll >= 61:
            return 'Corrosive (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 60 and ele_roll >= 56:
            return 'Radiation (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 55 and ele_roll >= 51:
            return 'Cyro' + ' ' +  guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 50 and ele_roll >= 46:
            return 'Incendiary' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 45 and ele_roll >= 41:
            return 'Explosive' +  ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 40 and ele_roll >= 36:
            return 'Shock' +  ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 35 and ele_roll >= 31:
            return 'Corrosive' +  ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 30 and ele_roll >= 26:
            return 'Radiation' +  ' ' + guild + ' ' + gun + '(' + rare + ')'
        else:
            return guild + ' ' + gun + '(' + rare + ')'
    elif rare == 'Epic':
        if ele_roll == 99 or ele_roll == 100:
            return 'Cyro & Explosive'  + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 97 or ele_roll == 98:
            return 'Shock & Corrosive' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 95 or ele_roll == 96:
            return 'Radiation & Incendiary' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 93 or ele_roll == 94:
            return 'Cyro (+2d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 91 or ele_roll == 92:
            return 'Incendiary (+2d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 90 and ele_roll >= 86:
            return 'Explosive (+2d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 85 and ele_roll >= 81:
            return 'Shock (+2d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 80 and ele_roll >= 76:
            return 'Corrosive (+2d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 75 and ele_roll >= 71:
            return 'Radiation (+2d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 70 and ele_roll >= 66:
            return 'Cryo (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 65 and ele_roll >= 61:
            return 'Incendiary (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 60 and ele_roll >= 56:
            return 'Explosive (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 55 and ele_roll >= 51:
            return 'Shock (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 50 and ele_roll >= 46:
            return 'Corrosive (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 45 and ele_roll >= 41:
            return 'Radiation (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 40 and ele_roll >= 36:
            return 'Cyro' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 35 and ele_roll >= 31:
            return 'Incendiary' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 30 and ele_roll >= 26:
            return 'Explosive' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 25 and ele_roll >= 21:
            return 'Shock' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 20 and ele_roll >= 16:
            return 'Corrosive' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 15 and ele_roll >= 11:
            return 'Radiation' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        else:
            return guild + ' ' + gun + '(' + rare + ')'
    elif rare == 'Legendary':
        if ele_roll == 99 or ele_roll == 100:
            return 'Cyro & Explosive' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 97 or ele_roll == 98:
            return 'Shock & Corrosive' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 95 or ele_roll == 96:
            return 'Radiation & Incendiary' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 93 or ele_roll == 94:
            return 'Cyro (+2d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll == 91 or ele_roll == 92:
            return 'Incendiary (+2d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 90 and ele_roll >= 86:
            return 'Explosive (+2d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 85 and ele_roll >= 81:
            return 'Shock (+2d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 80 and ele_roll >= 76:
            return 'Corrosive (+2d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 75 and ele_roll >= 71:
            return 'Radiation (+2d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 70 and ele_roll >= 66:
            return 'Cryo (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 65 and ele_roll >= 61:
            return 'Incendiary (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 60 and ele_roll >= 56:
            return 'Explosive (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 55 and ele_roll >= 51:
            return 'Shock (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 50 and ele_roll >= 46:
            return 'Corrosive (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 45 and ele_roll >= 41:
            return 'Radiation (+1d6)' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 40 and ele_roll >= 36:
            return 'Cyro' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 35 and ele_roll >= 31:
            return 'Incendiary' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 30 and ele_roll >= 26:
            return 'Explosive' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 25 and ele_roll >= 21:
            return 'Shock' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 20 and ele_roll >= 16:
            return 'Corrosive' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        elif ele_roll <= 15 and ele_roll >= 11:
            return 'Radiation' + ' ' + guild + ' ' + gun + '(' + rare + ')'
        else:
            return guild + ' ' + gun + '(' + rare + ')'
    else: 
        return guild + ' ' + gun + '(' + rare + ')'


def bonuses(guild, rare):
    if rare == 'Common':
        if guild == 'Alas':
            return "+1 DMG mod"
        elif guild == 'Skuldugger':
            return "+2 DMG Mod. Overheat: 1d4"
        elif guild == 'Dahlia':
            return "Burst: +1 hit"
        elif guild == 'Blackpowder':
            return "+2 ACC mod.  +2 Crit damage"
        elif guild == 'Malefactor':
            return "-2 DMG Mod"
        elif guild == 'Hyperius':
                return "+1 ACC mod. -2 DMG Mod"
        elif guild == 'Feriore':
            return "Swap/Reload: 1d4 Grenade damage. -3 ACC mod"
        elif guild == 'Torgue':
            return "Splash. -4 ACC Mod"
        elif guild == 'Stoker':
            return "Extra Attack. -3 ACC Mod"
    elif rare == 'Uncommon':
        if guild == 'Alas':
            return "+2 DMG mod"
        elif guild == 'Skuldugger':
            return "+3 DMG Mod. Overheat: 1d6"
        elif guild == 'Dahlia':
            return "Burst: +1 hit. +1 ACC Mod"
        elif guild == 'Blackpowder':
            return "+2 ACC mod.  +3 Crit damage"
        elif guild == 'Malefactor':
            return "-1 DMG Mod"
        elif guild == 'Hyperius':
            return "+2 ACC mod. -2 DMG Mod"
        elif guild == 'Feriore':
            return "Swap/Reload: 1d6 Grenade damage. -3 ACC mod"
        elif guild == 'Torgue':
            return "Splash. -3 ACC Mod"
        elif guild == 'Stoker':
            return "Extra Attack. -2 ACC Mod"
    elif rare == 'Rare':
        if guild == 'Alas':
            return "+3 DMG mod"
        elif guild == 'Skuldugger':
            return "+4 DMG Mod. Overheat: 1d8"
        elif guild == 'Dahlia':
            return "Burst: +1 hit. +2 ACC Mod"
        elif guild == 'Blackpowder':
            return "+2 ACC mod.  +4 Crit damage"
        elif guild == 'Malefactor':
            return "+10% Elemental Roll"
        elif guild == 'Hyperius':
            return "+3 ACC mod. -2 DMG Mod"
        elif guild == 'Feriore':
            return "Swap/Reload: 1d8 Grenade damage. -2 ACC mod"
        elif guild == 'Torgue':
            return "Splash. -2 ACC Mod"
        elif guild == 'Stoker':
            return "Extra Attack. -1 ACC Mod"
    elif rare == 'Epic':
        if guild == 'Alas':
            return "+3 DMG mod"
        elif guild == 'Skuldugger':
            return "+5 DMG Mod. Overheat: 1d10"
        elif guild == 'Dahlia':
            return "Burst: +1 hit. +3 ACC Mod"
        elif guild == 'Blackpowder':
            return "+2 ACC mod.  +5 Crit damage"
        elif guild == 'Malefactor':
            return "+15% Elemental Roll"
        elif guild == 'Hyperius':
            return "+4 ACC mod. -2 DMG Mod"
        elif guild == 'Feriore':
            return "Swap/Reload: 1d10 Grenade damage. -2 ACC mod"
        elif guild == 'Torgue':
            return "Splash. -1 ACC Mod"
        elif guild == 'Stoker':
            return "Extra Attack"
    elif rare == 'Legendary':
        if guild == 'Alas':
            return "+4 DMG mod"
        elif guild == 'Skuldugger':
            return "+6 DMG Mod. Overheat: 1d12"
        elif guild == 'Dahlia':
            return "Burst: +1 hit. +4 ACC Mod"
        elif guild == 'Blackpowder':
            return "+2 ACC mod.  +6 Crit damage"
        elif guild == 'Malefactor':
            return "+20% Elemental Roll"
        elif guild == 'Hyperius':
            return "+5 ACC mod. -2 DMG Mod"
        elif guild == 'Feriore':
            return "Swap/Reload: 1d10 Grenade damage. -1 ACC mod"
        elif guild == 'Torgue':
            return "Splash."
        elif guild == 'Stoker':
            return "Extra Attack. Extra Movement"

def lootsplosion(n):
    for i in range (1, int(n)+1):
        print(gun_generator())
        return gun_generator() 

def lootsplosion_array(n):
    loot = []
    if n =='':
        pass
    for i in range (1, int(n)+1):
        g = gun_generator()
        print(g)
        loot.append(g)
        #print(gun_generator())
        
    return loot 




#stat_gen(11, 'Pistol')

#while True:
#    gun_num = input('HOW MANY GUNS DO YOU WANT?!?: ')
#    lootsplosion(gun_num)

