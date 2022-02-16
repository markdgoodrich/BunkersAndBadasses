import random

potions = {
1: 'Tina Potion Common',
2: 'Common Health Potion: Regains 1d8 Health',
3: 'Common Shield Potion: Recharges 1d8 Shield',
4: 'Check Potion: +5 to x Check for 1 hour',
5: 'Element Potion: Protection from x Element for 2 turns',
6: 'Tina Potion Rare',
7: 'Rare Health Potion: Regens 2d8 + 5 Health',
8: 'Rare Shield Potion: Recharges 2d8 + 5 Shield',
9: 'Stat Potion: 3 to x Stat Mod for 1 hour',
10: 'Twofer Potion: Gain 1d8 +3 Health and Shields',
11: 'Tina Potion Epic',
12: 'Epic Health Potion: Regen 3d8 + 10 Health',
13: 'Epic Shield Potion: Recharges 3d8 + 10 Shield',
14: 'Lucky Potion: Reroll 1 die per Attack for 2 turns',
15: 'Invisibility Potion: Become Cloaked for 3 turns',
16: 'Tina Potion Legendary',
17: 'Legendary Health Potion: Regens 4d8 + 20 Health',
18: 'Legendary Shield Potion: Recharges 4d8 + 20 Shields',
19: "Fumble Potion: All 1's become 20's for 2 hours",
20: 'Gold Farmer Potion: +2d6 is all Cache Rolls for 2 hours'
    }

tina_potions = {
1: "Golden Gulp: Shhh it's just pee, don't tell anyone.",
2: "Deadly Horrible Potion of Death: Kills you dead in exactly 1 hour.  Can only be cured bu doing a hundo pushups",
3: "One Liner Juice: After drinking this, everything you do for the next hour has to be followed with a cool punny one liner, or else you spasm, taking 5 damage",
4: "Best Drink Ever: The single best thing you have or ever will taste.  Even if you get another one of these potions it'll never taste as good as the first, so you're sorta bummed forever that nothing tastes as good.",
5: "What if We Were Girlfriends: The next two people to drink this juice see what their life would be like if they moved their beds together",
6: "Gotta Sing: You have to sing everything you say for the next hour or until the BM gets bored",
7: "Friday Freak: The next two people to drink this swap bodies for the rest of the session",
8: "Love Potion Number 69 (nice): When you drink this potion, the next person you smooch will love for you exactly sixty-nine real seconds. Once the 69 seconds are up, they'll hate you with the exact same perocity with which they just loved you.",
9: "Truth Serum: You can only rell the truth for the rest of the session.",
10: "No Curses Plz: If the drinker curses anytime for the rest of the session, they take 5 Damage",
11: "Gotta Dance: You can't stop dancing for 10 minutes. When taking movement actions, specifically describe what sick steps you put down.",
12: "Big Booty Potion: Makes the booty grow 300%. Too Juicy. I die.",
13: "Vommodrink: Makes you vomit real bad for 30 seconds [Create a Corrosive puddle in all adjacent squares every turn for however long the BM hates you]",
14: "Stank Drank: Anyone who drinks this smells so bad that people gotta get as far away from them as possible for a half hour.  Allies cannot move through squares within a Range of 2 around you.]",
15: "Do U Feel Lucky: Has a fifty-fifty change to give the drinker 20 HP or deal 20 Health Damage.",
16: "Bullet Burp: For twenty minutes, you burn uncontrollably, causing bullets to come out and do 1d4 damage each to anyone adjacent. DO NOT KISS ANYONE AFTER DRINKING THIS",
17: "Baddie Juice: You immediately take the form of the one person you hate the most. Wears off after an hour.",
18: "Do You Like Me Y/N: Anyone drinking this has to tell their true feelings about the BM.",
19: "Roshambo: Exactly once, instead of doing a proper combat against an Enemy, you can play rock-paper-scissors with the BM. If you lose, your character is DEAD FOREVER or at least gets like 3 trauma",
20: "Punch Drunk: You have to Melee Attack someone every hour or your heart stops, but your Melee Attacks deal a bonus 1d12 Damage.",
21: "Butt Farts: Once, during the remainer of the session, you have the ability to do a fart so big it deals 2d8 Damage to everyone in 2 squares Range",
22: "Haterate: Anyone who drinks this makes everyone around em so mad that they gotta beat the puss out of them for at least a half hour. [All enemies make their next Attack against you, probably]",
23: "Fancy Feats: Gives you a fancy voice for an hour [+10 to Impersonation check]",
24: "2 Sexy: Makes you reeeeeeally alluring to one type of creature of the BM's choice [Gain +5 Talk and Interact checks for that enemy type]",
25: "Parent Trap: Whoever drinks this will insatntly create a baby with the next person they smooch. They baby will just pop into existence outta thin air",
26: "Scrappy: Drinkin this give you a little sidekick who looks like a smaller version of you. They're really irritating but they give you an extra Action every turn and they love you, but they have 1 HP.  You or the BM control them, and do their voice, whoever wants it first.",
27: "Not Today: The next time you would die... you don't.  Ignore the would-kill-you damage and get your life together",
28: "Liquid Confidence: Adjacent allies gain +2 to all checks",
29: "Good Touch: You Melee Attacks heal targets.",
30: "Tina Tincture: Makes you sound like Tiny Tina, your main main [Control one non-boss Enemey during the next encounter]"
    }

checks = {
1: "Interact",
2: "Talk",
3: "Insight",
4: "Sneak",
5: "Search",
6: "Traverse"
    }

elements = {
1: 'Radiation',
2: 'Corrosive',
3: 'Shock',
4: 'Explosive',
5: 'Incendiary',
6: 'Cyro'
    }

stats = {
1: 'ACC',
2: 'DMG',
3: 'SPD',
4: 'MST'
    }


def potion_gen():
    potion_pick = potions[random.randint(1,20)]
    if potion_pick[:11] == 'Tina Potion':
        potion = tina_potions[random.randint(1,30)]
    elif potion_pick[:5] == 'Check':
        potion = potion_pick.replace('x', checks[random.randint(1,6)])
    elif potion_pick[:7] == 'Element':
        potion = potion_pick.replace('x', elements[random.randint(1,6)])
    elif potion_pick[:4] == 'Stat':
        potion = potion_pick.replace('x', stats[random.randint(1,4)])
    else:
        potion = potion_pick
    return potion
