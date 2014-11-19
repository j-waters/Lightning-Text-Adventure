from lightCore import get_save
import os.path

Location = ""
Turn = 0
TurnString = ""
#TN1_R1 =[] probably not for api

def save():
    f = open('Saves/World.save', 'w')

    save = {
    'Location':Location,
    'Turn':Turn,
    'TurnString':TurnString,
    }

    for key in save.keys():
        if type(save[key]) == str:
            item = key + " = '" + save[key] + "'\n"
        else:
            item = key + " = " + str(save[key]) + "\n"
        f.write(item)
    f.close

def load():
    if os.path.isfile('Saves/World.save'):
        globals().update(get_save('Saves/World.save'))
        return True
    else:
        globals().update(get_save('Saves/DEFAULT_World.save'))
        #save() #TEMPORARY
        return False

