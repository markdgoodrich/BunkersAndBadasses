import os
from tkinter import *
from LevelTier import level_tier
from Guns import gun_generator
from GunCard import stat_gen
from GunCard import gun_type
from Grenades import grenade_gen
from Shields import shield_gen
from Relics import  relic_gen
from PIL import ImageTk, Image

def display_guns(n):
    gun_info.delete(1.0, 'end') #Clears old entry
    for i in range (1, int(n) +1):
        gun_str = str(gun_generator(int(lvl.get())))[2:-2].replace("'", '')     #removes unnecessary characters
        #print(gun_str)
        gun_info.insert(1.0, str(gun_str)+ '\n')
        display_stats(gun_str)  #To Generate the Stats Card
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
            
    #Pareses & writes gun value data out to the text fields
    stats = str(stats).replace("(",'').replace(')', '').replace("'", "")
    dmg, die, dist = stats.split(",")
    dmg1_text.insert(1.0, dmg[0] + "  " + dmg[1])
    dmg2_text.insert(1.0, dmg[2] + "  " + dmg[3])
    dmg3_text.insert(1.0, dmg[4] + "  " + dmg[5])
    dmg_die.insert(1.0, die)
    gun_range.insert(1.0, dist)

root = Tk()
root.title('Bunkers and Badasses Loot, suckas!')
root.geometry("800x400")
#root.iconbitmap('./assests/vaultsymbol_nJt_icon.ico')

#--- Image testing
vault_sym = PhotoImage(file="./assests/VaultSymbol.png")
vault_sym = vault_sym.subsample(6,6)
panel = Label(root, image = vault_sym)
panel.grid(row=0, rowspan=5, column=8, sticky='e')

#----   Tier/Levels    ----#
levels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
lvl = StringVar(root)
lvl.set(levels[0]) #Start at lvl1
level_choice = OptionMenu(root, lvl, *levels, command=level_tier)
level_label = Label(root, text="Player level")



#----   Guns   ----#

gun_num_label = Label(root, text="Number o' Guns")
gun_num = Entry(root, width=3)
gun_num.insert(0, 1)

gun_info = Text(root, height=3, width=60, wrap=WORD, font=('Helvetica 12')) #Displays gun info generated from the Button#
gun_btn = Button(root, text='Gimmie Guns, Baby!', command=lambda: display_guns(int(gun_num.get())) )   #need lambda so it doesn't run immediately


#---- Gun Stat Table----#

acc_label = Label(root, text="Acc").grid(row=20, column=1, sticky='w')
dmg1 = Label(root, text=" 2 - 7 ").grid(row=20, column=2, sticky='w')
dmg2 = Label(root, text=" 8 - 15 ").grid(row=20, column=3, sticky='w')
dmg3 = Label(root, text=" 16+ ").grid(row=20, column=4, sticky='w')
dmg = Label(root, text=" DMG ").grid(row=20, column=5, sticky='w')
ranged = Label(root, text="Range").grid(row=20, column=6, sticky='w')

hit_crit1 = Label(root, text="Hit Crit").grid(row=21, column=2, sticky='w')
hit_crit2 = Label(root, text="Hit Crit").grid(row=21, column=3, sticky='w')
hit_crit3 = Label(root, text="Hit Crit").grid(row=21, column=4, sticky='w')


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


#----   Grenade    ----#
gre_btn = Button(root, text='Grenade Vending', command=lambda: display_grenades())
gre_info = Text(root, height=2, width=50, wrap=WORD)


#---- Shields    ----#
shield_btn = Button(root, text='Shields Here', command=lambda: display_shield())
shield_info = Text(root, height=2, width=50, wrap=WORD)

#---- Relics    ----#
relic_btn = Button(root, text='Behold, Relics!', command=lambda: display_relic())
relic_info = Text(root, height=2, width=50,  wrap=WORD)


#----- Placements -----#

level_label.grid(row=1, column = 0)
level_choice.grid(row=1, column=1, sticky='w')

#gun_num_label.grid(row=7, column=0, sticky='w')
#gun_num.grid(row = 7, column = 1, sticky='w')
gun_btn.grid(row=8, column = 1, sticky='w', columnspan=3)
gun_info.grid(row=9, column=1, columnspan=8)

gre_btn.grid(row=3, column =0, sticky='w')
gre_info.grid(row=3, column=1, columnspan =6, sticky='w')


shield_btn.grid(row=4, column =0, sticky='w')
shield_info.grid(row=4, column =1, sticky='w', columnspan=6)


relic_btn.grid(row=5, column =0, sticky='w')
relic_info.grid(row=5, column =1, sticky='w', columnspan=6)


root.mainloop()

