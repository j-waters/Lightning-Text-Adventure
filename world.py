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
        #save() #TEMPORARY
        return False


TN1_R1 = []