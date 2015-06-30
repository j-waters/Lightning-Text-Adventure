from lightCore import get_save
import os.path
Name = ""
Age = 0
Health = 0
MaxHealth = 0
Helmet = None
Shirt = None
Boots = None
Leggins = None
Knowledge = []
Karma = 0
Xp = 0
Xpl = 0
Xpn = 0
Picture = ""
Luck = 0
Speed = 0
Strength = 0
Magic = 0
Spells = []
Mana = 0
MaxMana = 0

def save():
    f = open('Saves/Player.save', 'w')
    save = {
    'Name':Name,
    'Age':Age,
    'Health':Health,
    'Health':Health,
    'Helm':Helm,
    'Shirt':Shirt,
    'Boot':Boot,
    'Knowledge':Knowledge,
    'Karma':Karma,
    'Xp':Xp,
    'Xpl':Xpl,
    'Xpn':Xpn,
    'Picture':Picture,
    'Luck':Luck,
    'Speed':Speed,
    'Strength':Strength,
    'Magic':Magic,
    'Spells':Spells,
    'Mana':Mana,
    'MaxMana':MaxMana
    }

    for key in save.keys():
        if type(save[key]) == str:
            item = key + " = '" + save[key] + "'\n"
        else:
            item = key + " = " + str(save[key]) + "\n"
        f.write(item)
    f.close

def load():
    if os.path.isfile('Saves/Player.save'):
        globals().update(get_save('Saves/Player.save'))
        return True
    else:
        globals().update(get_save('Saves/DEFAULT_Player.save'))
        #save() #TEMP
        return False