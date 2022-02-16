import random

prefix_list = {
1: "One:Can only be fired once per day. Deals 10x Damage",
2: "Normal:Appearance of a Common Gun",
3: "Adorable:25% to distract Enemies with baby hallucinations",
4: "Gaudy:Highly refletice, which can be used to temporarily blind Enemies, giving them -3 of Attack Rolls",
5: "Cheerful:Grants +1 to all Talk Checks while equipped",
6: "Jumbled:Has the Accuracy and Damage, but the Range and bonuses of another",
7: "Classy:Gun will only fire if the wielder has the pinky of their shooting hand out",
8: "Economic:Enemies drop 2 gold per Hit and 5 gold per Crit",
9: "Certain:Grants a +2 bonus during Badass attempts",
10: "Humdrum:Enemies Hit experience ennui.",
11: "Lively:This gun has an AI that thinks it's alive.It can only any door once per day",
12: "Sleepy:Enemies Hit and Slowed,
13: "Deafening:Screams when fired, dealing 1 Damage to all adjacent targets",
14: "Selfish:Deals 1d6 Damage to wielder when changing to another equipped gun",
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




def prefix_gen():
    prefix_choice = prefix_list[(random.randint(1,100))]
    #split it into prefix & effect
    prefix, prefix_effect = prefix_choice.split(":")
    return prefix
