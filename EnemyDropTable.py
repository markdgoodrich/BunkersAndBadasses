import random


loot_1 = {
1: "10g",
2: "Health Potion (1d8)",
3: "Shield Potion (1d8)",
4: "Grenade (1)"
    }

loot_2 = {
1: "30g",
2: "Health Potion (2d8+5)",
3: "Shield Potion (1d8)",
4: "Grenades (2)"
    }

loot_3 = {
1: "Health Potion (3d8 + 5)",
2: "Shield Potion (2d8+5)",
3: "Random Potion (1)",
4: "Grenades (3)"
    }

loot_4 = {
1: "Random Potions(2)",
2: "Grenade Mod",
3: "Shield Mod",
4: "Random Gun"
    }

loot_5 = {
1: "Grenade Mod",
2: "Shield Mod",
3: "Common Relic",
4: "Random Gun"
    }

loot_6 = {
1: "Grenade Mod",
2: "Uncommon Relic",
3: "Random Gun",
4: "Random Gun"
    }


def rank_piles(n):
    #n is badass rank
    if n <= 3:
        return 1
    elif n >3 and n <=6:
        return 2
    elif n >6 and n<=12:
        return 3
    elif n >12 and n <= 18:
        return 4
    elif n > 18 and n <= 24:
        return 5
    else:
        return 6
    
def enemy_drop_table(counter):
    #ncounter is rank_piles return
    loot_array = []
    while counter > 0:
        if counter == 6:
            loot_array.append(loot_6[random.randint(1,4)])
            counter -= 1
        elif counter == 5:
            loot_array.append(loot_6[random.randint(1,4)])
            counter -= 1
        elif counter == 4:
            loot_array.append(loot_4[random.randint(1,4)])
            counter -= 1
        elif counter == 3:
            loot_array.append(loot_3[random.randint(1,4)])
            counter -= 1
        elif counter == 2:
            loot_array.append(loot_2[random.randint(1,4)])
            counter -= 1
        elif counter == 1:
            loot_array.append(loot_1[random.randint(1,4)])
            counter -= 1
    return loot_array

#print(rank_piles(28))
#print(enemy_drop_table(rank_piles(15)))
