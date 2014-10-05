from lightCore import get_save
import os.path
Minute = 0
Hour = 0
Day = 0
Dayp = ""
Month = 0
int(Day)
int(Minute)
int(Hour)
Weather = "clear"

def save():
    f = open('Saves/World.save', 'w')

    save = {
    'Minute':Minute,
    'Hour':Hour,
    'Day':Day,
    'Dayp':Dayp,
    'Month':Month,
    'Weather':Weather
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
        save()
        return False


TN1_R1 = [
          ("A Knife", "A slightly blunt knife", "weapon|2|i"),
          ("A Cloak", "A spare cloak", "cloak|1|c|i"),
          ("A Pair Of Trousers", "A spare pair of trousers", "trouser|1|c|i"),
          ("A Shirt", "A spare shirt", "shirt|1|c|i"),
          ("A Pouch Of Money", "A disappointingly small pouch of coppers", "money|15|i")
          ]