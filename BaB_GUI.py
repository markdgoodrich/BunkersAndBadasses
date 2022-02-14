import os
from tkinter import *
from LevelTier import level_tier
from BunkersBadassesLoot import gun_generator
from Grenades import grenade_gen
from Shields import shield_gen

def display_guns(n):
    gun_info.delete(1.0, 'end') #Clears old entry
    for i in range (1, int(n) +1):
        #gun_str = str(gun_generator())
        gun_str = str(gun_generator())[2:-2].replace("'", '')     #removes unnecessary characters
        gun_info.insert(1.0, str(gun_str)+ '\n')

def display_grenades():
    gre_info.delete(1.0, 'end')
    gre_info.insert(1.0, str(grenade_gen(int(lvl.get()))))

def display_shield():
    shield_info.delete(1.0, 'end')
    shield_info.insert(1.0, str(shield_gen(int(lvl.get()))))


root = Tk()
root.title('Bunkers and Badasses Loot, suckas!')
root.geometry("800x800")

#----   Tier/Levels    ----#
levels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
lvl = StringVar(root)
lvl.set(levels[0]) #Start at lvl1
level_choice = OptionMenu(root, lvl, *levels, command=level_tier)
level_label = Label(root, text="Player level")


#----   Guns   ----#

gun_num_label = Label(root, text="Number o' Guns", fg='white')
gun_num = Entry(root, width=3)
gun_num.insert(0, 1)

gun_info = Text(root, height=10, width=60, wrap=WORD, font=('Helvetica 13')) #Displays gun info generated from the Button

gun_btn = Button(root, text='Gimmie Guns, Baby!', command=lambda: display_guns(gun_num.get()) )   #need lambda so it doesn't run immediately



#----   Grenade    ----#
gre_btn = Button(root, text='Press for Grenades', command=lambda: display_grenades())
gre_info = Text(root, height=2, width=40)

#---- Shields    ----#
shield_btn = Button(root, text='Shields Here', command=lambda: display_shield())
shield_info = Text(root, height=2, width=50)


#----- Placements -----#

level_label.pack()
level_choice.pack()

gre_btn.pack()
gre_info.pack()

shield_btn.pack()
shield_info.pack()

gun_num_label.pack()
gun_num.pack()
gun_btn.pack()
gun_info.pack()

root.mainloop()

