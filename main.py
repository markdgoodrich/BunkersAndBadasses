import os
from tkinter import *
from LevelTier import level_tier
from Guns import gun_generator
from Guns import rarity_table
from GunCard import stat_gen
from GunCard import gun_type
from Grenades import grenade_gen
from Shields import shield_gen
from Relics import  relic_gen
from Potions import potion_gen
from RedText import redtext_gen
from Prefixes import prefix_gen
from EnemyDropTable import rank_piles
from EnemyDropTable import enemy_drop_table


def display_guns(n):
    gun_info.delete(1.0, 'end') #Clears old entry
    prefix_info.delete(1.0, 'end')
    
    if prefix_var.get():        #Checks to see if Prefix should be generated
        display_prefix()
    #if redtext_var.get():
    #    display_redtext()
        
    for i in range (1, int(n) +1):
        gun_str = str(gun_generator(int(lvl.get())))[2:-2].replace("'", '')     #removes unnecessary characters
        #print(gun_str)
        gun_info.insert(2.0, str(gun_str)+ '\n')
        display_stats(gun_str)  #To Generate the Stats Card
        color_gun_text(gun_str)
        shotgun_sniper_bonus(gun_str)

        elemental_bonus(gun_str)
        
        display_redtext(color_gun_text(gun_str))    #To determine Red Text
        
        return gun_str

def display_grenades():
    gre_info.delete(1.0, 'end')
    gre_info.insert(1.0, str(grenade_gen(int(lvl.get()))))

def display_shield():
    shield_info.delete(1.0, 'end')
    shield_info.insert(1.0, str(shield_gen(int(lvl.get()))))

def display_relic():
    relic_info.delete(1.0, 'end')
    relic_info.insert(1.0, str(relic_gen()))

def display_potions():
    potion_info.delete(1.0, 'end')
    potion_info.insert(1.0, str(potion_gen()))

def display_redtext(n):     #inputs gun rarity
    if redtext_var.get() and n == 'Epic':
        redtext_info.delete(1.0, 'end')
        redtext_info.insert(1.0, str(redtext_gen()))
    elif redtext_var.get() and n == 'Legendary':
        redtext_info.delete(1.0, 'end')
        redtext_info.insert(1.0, str(redtext_gen()))
    else:
        redtext_info.delete(1.0, 'end')
        
def display_prefix():
    prefix = prefix_gen()   #runs prefix_gun
    gun_info.insert(1.0, prefix[0] + " ")
    prefix_info.insert(1.0, prefix[1])

def display_stats(n):
    #Clear all old fields
    dmg1_text.delete(1.0,'end')
    dmg2_text.delete(1.0,'end')
    dmg3_text.delete(1.0,'end')
    dmg_die.delete(1.0,'end')
    gun_range.delete(1.0,'end')

    for x in gun_type:  #from GunCard file
        if gun_type[x] in n:    #finds the gun type from the current gun name
            stats = stat_gen(int(lvl.get()), str(gun_type[x]))
            
    #Parses & writes gun value data out to the text fields
    stats = str(stats).replace("(",'').replace(')', '').replace("'", "")
    dmg, die, dist = stats.split(",")
    dmg1_text.insert(1.0, dmg[0] + "  " + dmg[1])
    dmg2_text.insert(1.0, dmg[2] + "  " + dmg[3])
    dmg3_text.insert(1.0, dmg[4] + "  " + dmg[5])
    dmg_die.insert(1.0, die)
    gun_range.insert(1.0, dist)


def color_gun_text(n):
    rarity = ''
    gun_info.config(bg=background_color)
    #Adds color to the gun text depending on rarity
    for x in rarity_table: #from Guns file
        if rarity_table[x] in n:    #finds rarity in the current gun name
            rarity = rarity_table[x]
            break
    if rarity == 'Common':
        gun_info.config(bg='#eeeeee')
    elif rarity == 'Uncommon':
        gun_info.config(bg='#93c47d')
    elif rarity == 'Rare':
        gun_info.config(bg='#6fa8dc')
    elif rarity == 'Epic':
        gun_info.config(bg='#d5a6bd')
    elif rarity == 'Legendary':
        gun_info.config(bg='#f6b26b')
    return rarity


def shotgun_sniper_bonus(n):
    if 'Sniper' in n:
        prefix_info.insert(0.0, "If Range 3+: +3 Accuracy. ")
    elif 'Shotgun' in n:
        prefix_info.insert(0.0, "If Range 3 or less: +2 Damage. ")
            
def elemental_bonus(n):
    if 'Shock' in n:
        prefix_info.insert(2.0, " Double Damage to Shields")
    elif 'Incendiary' in n:
        prefix_info.insert(2.0, " Double Damage to Flesh")
    elif 'Corrosive' in n:
        prefix_info.insert(2.0, " Double Damage to Armor and Metal")
    elif 'Explosive' in n:
        prefix_info.insert(2.0, " Deals half Damage to all adjacent squares. 30% chance to cause Knockback")
    elif 'Radiation' in n:
        prefix_info.insert(2.0, " Penetrates Shield. If Target dies, explodes and deals 3d6 Splash Radiation Damage")
    elif 'Cryo' in n:
        prefix_info.insert(2.0, " Target can only move 1 square. if Target is hit again, they are Frozen: can either move one square or make a Melee Attack")


def display_enemy_drop(n):
    loot_enemy_info.delete(1.0, "end")
    lootpile = enemy_drop_table(rank_piles(n)) #returns array
    print(str(lootpile)[2:-2])
    loot_enemy_info.insert(1.0, str(lootpile)[2:-2])

root = Tk()
root.title('Bunkers and Badasses Loot, suckas!')
root.geometry("750x800")
background_color = '#5b5b5b'
button_color= '#c27ba0'
textbox_color = '#999999'

root['background'] = background_color

#--- Image 
vault_sym = PhotoImage(file="./assests/VaultSymbol.png")
vault_sym = vault_sym.subsample(6,6)
panel = Label(root, image = vault_sym, bg=background_color)
panel.grid(row=0, rowspan=5, column=7, sticky='e')

#----   Tier/Levels    ----#
levels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
lvl = StringVar(root)
lvl.set(levels[0]) #Start at lvl1
level_choice = OptionMenu(root, lvl, *levels, command=level_tier)
level_choice.config(bg=background_color)
level_label = Label(root, text="Player level", font='12', bg=background_color)

#----   Guns   ----#

gun_num_label = Label(root, text="Number o' Guns")
gun_num = Entry(root, width=3)
gun_num.insert(0, 1)

gun_info = Text(root, height=3, width=60, wrap=WORD, font=('Helvetica 12'), bg=textbox_color) #Displays gun info generated from the Button#
gun_btn = Button(root, text='Gimmie Guns, Baby!', command=lambda: display_guns(int(gun_num.get())) )   #need lambda so it doesn't run immediately


#---- Gun Stat Table----#

acc_label = Label(root, text="Acc", bg=background_color).grid(row=20, column=1, sticky='w')
dmg1 = Label(root, text=" 2 - 7 ", bg=background_color).grid(row=20, column=2, sticky='w')
dmg2 = Label(root, text=" 8 - 15 ", bg=background_color).grid(row=20, column=3, sticky='w')
dmg3 = Label(root, text=" 16+ ", bg=background_color).grid(row=20, column=4, sticky='w')
dmg = Label(root, text=" DMG ", bg=background_color).grid(row=20, column=5, sticky='w')
ranged = Label(root, text="Range", bg=background_color).grid(row=20, column=6, sticky='w')

hit_crit1 = Label(root, text="Hit Crit", bg=background_color).grid(row=21, column=2, sticky='w')
hit_crit2 = Label(root, text="Hit Crit", bg=background_color).grid(row=21, column=3, sticky='w')
hit_crit3 = Label(root, text="Hit Crit", bg=background_color).grid(row=21, column=4, sticky='w')


dmg1_text = Text(root, width=5, height=1)
dmg2_text = Text(root, width=5, height=1)
dmg3_text = Text(root, width=5, height=1)
dmg_die = Text(root, width=5, height=1)
gun_range = Text(root, width=5, height=1)


dmg1_text.grid(row=22, column=2, sticky='w')
dmg2_text.grid(row=22, column=3, sticky='w')
dmg3_text.grid(row=22, column=4, sticky='w')
dmg_die.grid(row=22, column=5, sticky='w')
gun_range.grid(row=22, column=6, sticky='w')

gun_card = Label(root, text="Base Gun Stats", font='Bold 12', bg=background_color, fg='#e69138').grid(row=19, column=1, columnspan=3, sticky='w')

#----   Grenade    ----#
gre_btn = Button(root, text='Grenade Vending', bg='#fcb66f', command=lambda: display_grenades())
gre_info = Text(root, height=2, width=50, wrap=WORD, bg=textbox_color)


#---- Shields    ----#
shield_btn = Button(root, text='Shields Here', bg='#9fc5e8', command=lambda: display_shield())
shield_info = Text(root, height=3, width=50, wrap=WORD, bg=textbox_color)

#---- Relics    ----#
relic_btn = Button(root, text='Behold, Relics!', bg=button_color, command=lambda: display_relic())
relic_info = Text(root, height=2, width=50,  wrap=WORD, bg=textbox_color)


#---- Potions    ----#
potion_btn = Button(root, text='Drink Up', bg='#c1ecae', command=lambda: display_potions())
potion_info = Text(root, height=3, width=50, wrap=WORD, bg=textbox_color)


#---- Red Text  ----#
#redtext_btn = Button(root, text='Red Text', bg='#cc0000', fg='#eeeeee', command=lambda: display_redtext())
redtext_var = BooleanVar()
redtext_btn = Checkbutton(root, text='Red Text', bg='#cc0000', variable=redtext_var, onvalue = True, offvalue = False)
redtext_info = Text(root, height=3, width=50, wrap=WORD, fg='#cc0000', bg=textbox_color)


#---- Prefix  ----#
prefix_var = BooleanVar()
prefix_btn = Checkbutton(root, text='Prefix', variable=prefix_var, onvalue=True, offvalue=False)
prefix_info = Text(root, height=3, width=60, wrap=WORD, bg=textbox_color) #Displays gun info generated from the Button#


#---- Enemy Drop Table  ----#
enemy_drop_label =Label(root, text="\nEnemy Drop Loot Generation\n------------------", font='14', bg=background_color)
badass_rank_label = Label(root, text="Badass Rank", font='12', bg=background_color)
badass_rank = Text(root, height=1, width=4)
loot_enemy_btn = Button(root, text='Loot Pile', bg=background_color, command=lambda: display_enemy_drop(int(badass_rank.get("1.0", "end"))))
loot_enemy_info = Text(root, height = 8, width = 20, wrap=WORD, bg=textbox_color)

#----- Placements -----#

level_label.grid(row=1, column = 1)
level_choice.grid(row=1, column=2, sticky='w')

gre_btn.grid(row=3, column =0)
gre_info.grid(row=3, column=1, columnspan =6, sticky='w')

shield_btn.grid(row=4, column =0)
shield_info.grid(row=4, column =1, sticky='w', columnspan=6)

relic_btn.grid(row=5, column =0)
relic_info.grid(row=5, column =1, sticky='w', columnspan=6)

potion_btn.grid(row=6, column=0)
potion_info.grid(row=6, column=1, sticky='w', columnspan=6, pady=8)

prefix_btn.grid(row=9, column = 6)

gun_btn.grid(row=9, column = 1, sticky='w', columnspan=3, pady=8)
gun_info.grid(row=11, column=1, columnspan=8, sticky='w')

prefix_info.grid(row=12, column=1, sticky='w', columnspan=6, pady=4)

redtext_btn.grid(row=9, column=7)
redtext_info.grid(row=13, column=1, sticky='w', columnspan=6)

enemy_drop_label.grid(row=28, column=0, columnspan=4)
badass_rank_label.grid(row=29, column=0)
badass_rank.grid(row=29, column=1, sticky='w')
loot_enemy_btn.grid(row=29, column=2, sticky='w')
loot_enemy_info.grid(row=31, column=1, sticky='w', columnspan=6)

root.mainloop()

