from lightCore import get_save
import os.path
Name = ""
Age = 0
Health = 0
Helm = ""
Shirt = ""
Boot = ""
Knowledge = []
Karma = 0
Xp = 0
Xpl = 0
Xpn = 0
Picture = ""

def save():
    f = open('Saves/Player.save', 'w')
    save = {
    'Name':Name,
    'Age':Age,
    'Health':Health,
    'Health':Health,
    'Helm':Helm,
    'Shirt':Shirt,
    'boot':boot,
    'Knowledge':Knowledge,
    'Karma':Karma,
    'Xp':Xp,
    'Xpl':Xpl,
    'Xpn':Xpn,
    'Picture':Picture,
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