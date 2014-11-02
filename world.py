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
Weather = ""

Location = ""

TN1_R1 =[]

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

def time():
    if Day % 10 == 1:
        Dayp = "st"
    if Day % 10 == 2:
        Dayp = "nd"
    if Day % 10 == 3:
        Dayp = "rd"
    if Day % 10  == 0:
        Dayp = "th"
    if Day % 10 > 3:
        Dayp = "th"

    TheOut = str(Hour) + ":" + str(Minute) + "0" + " " + str(Day) + str(Dayp) + " of " + str(Month)

    #str(TheOut)
    return TheOut


TN1_R1 = []