import random

red_texts = {
1: "POP POP! : Deals Crit Damage twice",
2: "I never freeze : Add Cyro Element type",
3: "Toasty! : Adds Increndiary Element type",
4: "Was he slow? : Fires backwards",
5: "We Hate You, Please Die. : Taunts the farthest enemy each turn",
6: "Tell them they're next : Won't deal Damage to the final Enemy in an encounter",
7: "PAN SHOT! : always hits the closest enemy",
8: "Envision Wyverns: Adds Radiation Element type",
9: "I'm melting! : Add Corrosive Element type",
10: "The same thing that happens to everything else : Adds Shock Element type",
11: "360 quickscope : Adds a Crit to each Ranged Attack",
12: "Any Questions? : Shoots pumpkin bombs that deal an extra 3d6 Explosive Damage",
13: "Blood and Thunder : Take 1d6 Health Damage to deal +3d6 Shock Damage",
14: "SI VIS PACEM PARA BELLUM : Gain extra Attack if Acting Before Enemies",
15: "You're breathtaking! : Wielder cannot be targeted on the first turn of an encounter",
16: "Pass turn. : Wielder may throw a grenade during the End of Turn step",
17: "I am Vengeance! : Deals 2x Damage to Enemies adjacent to allies",
18: "Roll the dice : If Accuracy Roll is even, 2x Damage.  If Accuracy Roll is odd, half Damage",
19: "One among the fence : Add 21 Damage if you roll 13+ on your Accuracy Roll (1/day)",
20: "Don't be sorry. Be better. : Reroll the Badass Dice once per day",
21: "THE PICKLES! : Shoots flaming cheeseburgers that deal an extra 2d6 Incendiary Damage",
22: "Do a kickflip! : +4 on Traverse Checks while equipped.",
23: "Extinction is the Rule : Teleport to any square up to 4 away when you kill an Enemy",
24: "Never Fight a Knight with a Perm : DMG Mod +6 against non-human Enemies",
25: "Bye bye, little Butt Stallion! : Shots explode into rainbows that deal an extra 1d8 Damage",
26: "Time 2 Hack : +4 on Interact Checks and Melee Damage while equipped",
27: "HATE Magic... so much : +3 DMG Mod.  take 2d6 Vomit Damage if Reloaded",
28: "OFF WITH THEIR HEADS! : roll d100. if > 95, the Enemy's head falls off",
29: "This is my BOOMSTICK! : Deals 3x Damage to skeletons",
30: "Super easy, barely an inconvenience : Automatically pass the first Check each day",
31: "Hold onto your butts. : When fired, the wielder and targets Hit are Knocked Back 2 squares",
32: "The Wise Man's Fear : Deals 3x Damage to all Wizards",
33: "I don't want this isolate. : Won't fire unless adjacent to an ally or target",
34: "TUFF with two Fs : Prevents the first 5 Health Damage each turn",
35: "Unlikely Maths : Roll an extra die of each type rolled during an Attack and take the highest results(s)",
36: "Gravity's Rainbow : First Attack against a Badass taget always deals max Damage",
37: "Let's do this one last time... : Shoots web that reduce target's Movement to 0 for 1 turn",
38: "BIP! : Once per encounter, the wilder can run into squares with an Enemy, Knocking them Back 1 square",
39: "The Heaviest Matter of the Universe : The wielder and targets Hit cannot take Movement Actions while equipped",
40: "GREEN FLAME : Shoots burst of green flames while firing, dealing 2d6 Incendiary Damage to adjacent targets",
41: "More like Bore Ragnarok! : Gain 1 Badass Token after a successful Talk Check while equipped",
42: "That's levitation, Holmes! : Ignore difficult terrain while equipped",
43: "Let's boo-boo. : Gain extra Movement after drinking a potion while equipped.",
44: "Mmm Whatcha Say... : Gain a Ranged Attack if an Enemy is talking before an encounter",
45: "Here Comes the FunCooker : When this gun scores a Crit, the enemy suffer a miniature combustion, dealing 1d12 Explosive Damage to itself and all adjacent squares",
46: "Overwhelming strength is boring. : -6 Initiative.  The first non-Badass, non-Boss Enemy that is Melee Attacked dies instantly (1/day)",
47: "Stop talking, I will win.  It's what heroes do. : Gun fires explosives that deal +3d6 Damage to all adjacent squares",
48: "Richer and cleverer than everyone else! : Add 10 gold per Loot Pile when rolling for Enemy Drops",
49: "METAL WILL DESTROY ALL EVIL! : Allies get +2 ACC Mod each turn you perform a Melee Attack",
50: "Life is a conundrum of esoterica: Gain 2 Badass Tokens the first time you roll for a Trauma each day"
    }




def redtext_gen():
    red = red_texts[(random.randint(1,50))]
    return red
