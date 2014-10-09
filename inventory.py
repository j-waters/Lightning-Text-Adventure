from lightCore import get_save
import os.path
Contents = []
Size = 0
Money = 0


def save():
    f = open('Saves/Inventory.save', 'w')

    save = {
    'Contents':Contents,
    'Size':Size,
    'Money':Money
    }

    for key in save.keys():
        if type(save[key]) == str:
            item = key + " = '" + save[key] + "'\n"
        else:
            item = key + " = " + str(save[key]) + "\n"
        f.write(item)
    f.close

def load():
    if os.path.isfile('Saves/Inventory.save'):
        globals().update(get_save('Saves/Inventory.save'))
        return True
    else:
        globals().update(get_save('Saves/DEFAULT_Inventory.save'))
        print(Size)
        #save() #TEMP
        return False