#####
#The main core function/script file for the Legend Of Aiopa Text Adventure
#Most of the functions included in the game are here
#####

#####
#All Module Imports

#Core Import All
from lightCore import * #@UnusedWildImport
#General Modules
#import time #@UnusedImport
#import random #@UnusedImport
#import easygui #@UnresolvedImport @UnusedImport
#import sys #@UnusedImport @Reimport
#import atexit #@UnusedImport

#End Module Imports
#####

#####
#Setup print and pprint
#####
def print(string):  # @DontTrace @ReservedAssignment
    #easygui print
    easygui.msgbox(msg=string, title=world_time())

def pprint(pic, string):
    #easygui picture print
    easygui.msgbox(image=pic, msg=string, title=world_time())



#####
#PLAYER
#####
playerName = ""
playerAge = 0
playerHealth = 0
playerCloak = ""
playerShirt = ""
playerTrouser = ""
playerKnowledge = []
playerKarma = 0
playerXp = 0
playerXpl = 0
playerXpn = 0
playerPicture = ""

def player_damage(attacker, attackType, amount):
    #Deals damage to the player, displaying who did it
    print(attacker + " " + attackType + " " + playerName + ". " + playerName + " takes " + str(amount) + " damage")
    playerHealth -= amount

    if playerHealth < 1:
        player_die()

def player_die():
    #Displays the death message, and then returns you to your previous spot
    print("You collapse to the ground.")
    print("The world tumbles around you.")
    print("Your vision gets brighter and brighter, until...")
    #run(Last_Point)

def player_refresh():
    #Does a check of multiple player variables, checking if they make sense.
    if playerHealth < 1:
        player_die()

def player_Xpa(xp):
    #Adds 'xp' XP to the players xp, checking if the player level can be increased
    playerXp += xp
    while playerXp > playerXpn:
        if playerXp > playerXpn:
            playerXpl += 1
            playerXp -= playerXpn
            playerXpn *= 1.2
            playerXpn = int(playerXpn)

def player_defence():
    #Calculates the defence of a player
    TheOut = 1
    try:
        TheOut += int(getmet(playerCloak, 1))
    except:
        TheOut += 0
    try:
        TheOut += int(getmet(playerShirt, 1))
    except:
        TheOut += 0
    try:
        TheOut += int(getmet(playerTrouser, 1))
    except:
        TheOut += 0

    return int(TheOut)

def player_unEquip(item):
    #Unequips an item from the player
    debug("Un Equip")

    if item == "cloak":
        inventory_add(playerCloak)
        playerCloak = ""

    if item == "shirt":
        inventory_add(playerShirt)
        playerShirt = ""

    if item == "trouser":
        inventory_add(playerTrouser)
        playerTrouser = ""

def player_equip(item):
    #Equips an item to the player
    debug("equiping:")

    if getmet(item, 0) == "cloak":
        if playerCloak == "":
            playerCloak = item
            inventory_remove(item)

        else:
            inventory_remove(item)
            inventory_add(playerCloak)
            playerCloak = item




    if getmet(item, 0) == "shirt":
        if playerShirt == "":
            playerShirt = item
            inventory_remove(item)

        else:
            inventory_remove(item)
            inventory_add(playerShirt)
            playerShirt = item



    if getmet(item, 0) == "trouser":
        if playerTrouser == "":
            playerTrouser = item

            inventory_remove(item)

        else:
            inventory_remove(item)
            inventory_add(playerTrouser)
            playerTrouser = item

    else:
        print("Cannot equip a " + item)



def player_attack(tgt):
    #Player attacks 'tgt'
    debug("ATTACKING")
    tatt = getmet(tgt, 1)
    tdef = getmet(tgt, 2)
    tlife = getmet(tgt, 3)
    trnk = getmet(tgt, 4)
    taln = getmet(tgt, 5)
    target = getnam(tgt)

    weapons = []
    wdamage = []

    for i in range(0, len(inventoryContents)):
        spl = getmet(inventoryContents[i], 0)
        if spl == "weapon":
            weapons.append(getnam(inventoryContents[i]))
            wdamage.append(getmet(inventoryContents[i], 1))

    weapons.append("Your Fists")
    wdamage.append("2")

    #pprint(Fight_Symbol, playerName + " (" + str(playerHealth) + ", " + str(player_defence()) + ")" + " Attacks " + target + " (" + str(tlife) + ", " + str(tdef) + ")" + "!")
    pprint(Fight_Symbol, playerName + " (Level " + str(playerXpl) + ")" + " Attacks " + str(target) + " (Level " + str(trnk) + ")" + "!")
    att_weapon = easygui.choicebox(msg="Chose your weapon", choices=(weapons))

    patt = 0

    for i in range(0, len(weapons)):
        if weapons[i] == att_weapon:
            patt = int(wdamage[i])

    while True:
        ###Choose Attacker###
        rnd = random.randint(1,2)
        PtE = int( patt * (1 + random.random())- int(tdef))
        EtP = int( int (tatt) * (1 + random.random()) - player_defence())
        tlife = int(tlife)
        if PtE < 0:
            Rdmg = 0

        if EtP < 0:
            Rdmg2 = 0

        if rnd == 1:
            ###Player Attacks###
            print(playerName + " Attacks!")
            print(playerName + " Deals " + str(PtE) + " Damage To " + target)
            tlife -= PtE
            print(target + " Is Now On " + str(tlife) + " Health.")


            if tlife < 1:
                print("You defeat " + target + ".")
                pxp = int((int(trnk) + 1) * (random.randint(1, 3) + random.random()))
                print("you gain " + str(pxp) + " XP!")
                pka = int(int(trnk) * (random.randint(1, 2) + random.random()))
                player_Xpa(pka)
                if taln == "g":
                    print(target + " was good." + "You lose" + str(pka) + " karma")
                    playerKarma -= pka
                if taln == "e":
                    print(target + "was evil." + "You gain" + str(pka) + " karma")
                    playerKarma += pka
                return "win"

            print(target + " Deals " + str(EtP) + " Damage To " + playerName)
            playerHealth -= EtP
            print(playerName + " Is Now On " + str(playerHealth) + " Health.")


            if playerHealth < 1:

                player_die()


        if rnd == 2:
            ###Opponent Attacks###
            print(target + " Attacks!")
            print(target + " Deals " + str(EtP) + " Damage To " + playerName)
            playerHealth -= EtP
            print(playerName + " Is Now On " + str(playerHealth) + " Health.")

            if playerHealth < 1:
                player_die()

            print(playerName + " Deals " + str(PtE) + " Damage To " + target)
            tlife -= PtE
            print(target + " Is Now On " + str(tlife) + " Health.")


            if tlife < 1:
                return "win"


#####
#END PLAYER
#####

#####
#INVENTORY
#####
inventoryContents = []
inventorySize = 0
inventoryMoney = 0

def inventory_add(item):
    debug("ADD TO INVENTORY:")
    if 1 + len(inventoryContents) > inventorySize:
        spaceleft = inventorySize - len(inventoryContents)
        things = len(item)
        pprint(Full_Bag, "You Can't fit " + str(things) + " More item in a bag that can only hold " + str(spaceleft) + " more items!")

        INV_A_DC = easygui.choicebox(msg="What to discard: (cancel to not discard anything)", choices=(inventoryContents))
        if not INV_A_DC == None:
            inventory_remove(INV_A_DC)
        if INV_A_DC == None:
            return

    else:
        if type(item) == tuple:
            inventoryContents.append(item)

        if type(item) == list:
            for i in range(len(item)):

                inventoryContents.append(item[i])




def inventory_get():
    debug("INVENTORY")
    debug("CONTENTS:\n" + str(inventoryContents))
    ##Finding Money##
    for i in range(0, len(inventoryContents)):
        spl = getmet(inventoryContents[i], 0)
        if spl == "money":
            amt = getmet(inventoryContents[i], 1)
            amti = int(amt)
            type(amti)
            inventoryMoney += amti
            del inventoryContents[i]
            break

    if inventoryMoney % 10 == 0:
        inventoryMoney = 0

    ##adding money string to inventory###

    mstring = "You Have: " + str(inventoryMoney) + " Gold"
    mstringd = "Your small bag of money full of coins that are known as 'gold' by the comoners"
    mstringm = ""
    inventoryContents.append((mstring, mstringd, mstringm))

    ##done money##

    ##adding equipped items to inventory##

    estring1 = "You Have Equipped: "
    try:
        if not playerCloak == "":
            estring2 = playerCloak[0]
            estring2d = playerCloak[1]
            estring2m = "e|cloak"

        if playerCloak == "":
            estring2 = "No Cloak"
            estring2d = "Your not wearing a cloak"
            estring2m = ""
    except:
        estring2 = "No Cloak"
        estring2d = "Your not wearing a cloak"
        estring2m = ""

    try:
        if not playerShirt == "":
            estring3 = playerShirt[0]
            estring3d = playerShirt[1]
            estring3m = "e|shirt"

        if playerShirt == "":
            estring3 = "No Extra Shirt"
            estring3d = "Your not wearing any extra shirt"
            estring3m = ""
    except:
        estring3 = "No Extra Shirt"
        estring3d = "Your not wearing an extra shirt"
        estring3m = ""

    try:
        if not playerTrouser == "":
            estring4 = playerTrouser[0]
            estring4d = playerTrouser[1]
            estring4m = "e|trouser"

        if playerTrouser == "":
            estring4 = "No Extra Trouser"
            estring4d = "Your not wearing any over trousers"
            estring4m = ""
    except:
        estring4 = "No Extra Trouser"
        estring4d = "Your not wearing any over trousers"
        estring4m = ""

    inventoryContents.append((estring1 + estring2,estring2d, estring2m))
    inventoryContents.append((estring1 + estring3,estring3d, estring3m))
    inventoryContents.append((estring1 + estring4,estring4d, estring4m))

    ##adding player stats##
    pstring = "Your Statistics"
    pstringd = "Your Stats:\n" + "Health: " + str(playerHealth) + "\nDefence: " + str(player_defence())
    pstringm = ""
    inventoryContents.append((pstring, pstringd, pstringm))

    ##showing inventory##

    vop = easygui.choicebox(msg = "Your Inventory:", choices=(getnam(inventoryContents)))

    vop = find_tup(vop, inventoryContents)

    inventoryContents.remove((mstring, mstringd, mstringm))
    inventoryContents.remove((pstring, pstringd, pstringm))
    inventoryContents.remove((estring1 + estring2,estring2d, estring2m))
    inventoryContents.remove((estring1 + estring3,estring3d, estring3m))
    inventoryContents.remove((estring1 + estring4,estring4d, estring4m))

    debug("\n VOP:")
    debug(vop)

    if vop == None:
        return "exit"

    if type(vop) == list:
        vop = vop[0]

    if getmet(vop, "all") == "i":
        #Is it an average item?
        pprint(Full_Bag, getdes(vop))

    if searchmet("e", vop) == "T":
        #Is it an equipped item?
        IgI = easygui.buttonbox(image=Full_Bag, msg=getdes(vop), choices=("Back", "Un Equip"))
        if IgI == "Un Equip":
            player_unEquip(getmet(vop, 1))

    if searchmet("c", vop) == "T":
        #Is it an eqipable item?
        IgI = easygui.buttonbox(image=Full_Bag, msg=getdes(vop), choices=("Back", "Equip"))
        if IgI == "Equip":
            player_equip(vop)

    else:
        verb = "Use"
        if searchmet("book", vop) == "T":
            verb = "Read"

        IgI = options(Full_Bag, getdes(vop), "Discard", verb, "Back")

        if IgI == "Discard":
            inventory_remove(vop)
        if IgI == verb:
            if getmet(vop, 0) == "book":
                read(vop)
            #other items


    inventory_get()
    return

def inventory_remove(item):
    inventoryContents.remove(item)

#####
#END INVENTORY
#####

#####
#WORLD
#####
worldMinute = 0
worldHour = 0
worldDay = 0
worldDayp = ""
worldMonth = 0
int(worldDay)
int(worldMinute)
int(worldHour)
worldWeather = "clear"

def world_time():
    if worldDay % 10 == 1:
        worldDayp = "st"
    if worldDay % 10 == 2:
        worldDayp = "nd"
    if worldDay % 10 == 3:
        worldDayp = "rd"
    if worldDay % 10  == 0:
        worldDayp = "th"
    if worldDay % 10 > 3:
        worldDayp = "th"

    TheOut = str(worldHour) + ":" + str(worldMinute) + "0" + " " + str(worldDay) + str(worldDayp) + " of " + str(worldMonth)

    #str(TheOut)
    return TheOut

#####
#END WORLD
#####

def getmet(item, metno):
    #Gets the metadata from a tuple (item)
    #finds the correct metadata by number (metno)
    TheOut = None

    if type(item) == tuple:
        TheOut = item[2].split('|')[metno]

        if metno == "all":
            TheOut = item[2]

    if type(item) == list:
        TheOut = item[0][2].split('|')[metno]
        if metno == "all":
            TheOut = item[0][2]

    return TheOut

def getdes(item):
    #Gets the description from a tuple (item)
    TheOut = item[1]
    return TheOut

def getnam(item):
    #Gets the name from a tuple (item)
    if type(item) == tuple:
        TheOut = item[0]
        return TheOut
    if type(item) == list:
        TheOut = t(item, 0)
        return TheOut

def searchmet(string, item):
    #string = what we want to find
    #item = tuple/string we want to search
    if type(item) == tuple:
        item = getmet(item, "all")

    for i in len(item.split('|')):
        if item.split('|')[i] == string:
            return "T"

    return "F"

def input(string):  # @ReservedAssignment
    #Creates an enter box with a string, and the time as the title
    TheInput = easygui.enterbox(msg=string, title=world_time())
    return TheInput

def options(pic, string, op1, op2, op3=None, op4=None):
    #creates an button box with 2, up to 4 choices
    if not op4 == None:
        TheOut = easygui.buttonbox(choices=(op1, op2, op3, op4, "Inventory"), msg=string, image=pic, title=world_time())
    if op4 == None:
        TheOut = easygui.buttonbox(choices=(op1, op2, op3, "Inventory"), msg=string, image=pic, title=world_time())
    if op4 and op3 == None:
        TheOut = easygui.buttonbox(choices=(op1, op2, "Inventory"), msg=string, image=pic, title=world_time())

    if TheOut == "Inventory":
        inventory_get()
        TheOut = options(pic, string, op1, op2, op3, op4)

    return TheOut

def move(choices):
    #Shows a choicebox with places that the player can move to
    #returns the selection

    choices = [i for i in choices if searchmet("building", i) == "T"]

    TheOut = easygui.choicebox(msg="Move To:", choices=(t(choices, 0)))

    TheOut = find_tup(TheOut, choices)

    return TheOut

def find_tup(item, lis):
    #gets a one or multiple string/s
    #item = the string/s
    #lis = the list it has to search through
    TheOut = []

    if type(item) == list:

        for i in range(0, len(item)):

            for t in range(0, len(lis)):

                if lis[t][0] == item[i]:

                    TheOut.append(lis[t])
                    break
        return TheOut

    if type(item) == str:


        for t in range(0, len(lis)):

            if lis[t][0] == item:

                TheOut = lis[t]

                return TheOut

def view(items, string=""):
    #Creates a choicebox from a list
    #Can use a string, by default shows 'you can see:'

    TheOut = ""
    str(TheOut)

    if string == "":
        TheOut = easygui.choicebox(msg="You Can See:", choices=(t(items, 0)), title=world_time())

    else:
        TheOut = easygui.choicebox(msg=string, choices=(t(items, 0)), title=world_time())


    TheOut = find_tup(TheOut, items)

    print(TheOut[1])


    return TheOut

def take(string, choices, mmax):
    #Takes an item and places it into the players inventory
    #Returns the item
    debug("TAKING")

    choices = [i for i in choices if searchmet("i", i) == "T"]

    TheOut = easygui.multchoicebox(msg=string, choices=(t(choices, 0)))

    if TheOut == None:
        return

    if len(TheOut) > mmax:
        return

    else:

        inventory_add(find_tup(TheOut, choices))
        return find_tup(TheOut, choices)

def read(item):
    book = getnam(item)
    book = book.split(':')[1]
    book = book.replace(" ", "")
    importVar(book)
    print("Knowledge Acquired! " + getmet(item, 1) + "!")
    playerKnowledge.append(getmet(item, 1))

def psave():
    p = open('Saves/Player.save', 'w')

    playersave = {
    'playerName':playerName,
    'playerAge':playerAge,
    'playerHealth':playerHealth,
    'playerHealth':playerHealth,
    'playerCloak':playerCloak,
    'playerShirt':playerShirt,
    'playerTrouser':playerTrouser,
    'playerKnowledge':playerKnowledge,
    'playerKarma':playerKarma,
    'playerXp':playerXp,
    'playerXpl':playerXpl,
    'playerXpn':playerXpn,
    'playerPicture':playerPicture,
    'inventoryContents':inventoryContents,
    'inventorySize':inventorySize,
    'inventoryMoney':inventoryMoney
    }

    for key in playersave.keys():
        if type(playersave[key]) == str:
            item = key + " = '" + playersave[key] + "'\n"
        else:
            item = key + " = " + str(playersave[key]) + "\n"
        p.write(item)
    p.close

def wsave():
    w = open('Saves/World.save', 'w')

    worldsave = {
    'worldMinute':worldMinute,
    'worldHour':worldHour,
    'worldDay':worldDay,
    'worldDayp':worldDayp,
    'worldMonth':worldMonth,
    'worldWeather':worldWeather
    }

    for key in worldsave.keys():
        if type(worldsave[key]) == str:
            item = key + " = '" + worldsave[key] + "'\n"
        else:
            item = key + " = " + str(worldsave[key]) + "\n"
        w.write(item)
    w.close

def load():
    if os.path.isfile('Saves/Player.save'):
        globals().update(get_save('Saves/Player.save'))
    else:
        globals().update(get_save('Saves/DEFAULT_Player.save'))
        psave()
    if os.path.isfile('Saves/World.save'):
        globals().update(get_save('Saves/World.save'))
    else:
        globals().update(get_save('Saves/DEFAULT_World.save'))
        wsave()

def player_picture(img1,img2,img3=None,img4=None):
    picno = 1
    maxpics = 2
    pic1 = img1
    pic2 = img2
    if not img3 == None:
        maxpics = 3
        pic3 = img3
    if not img4 == None:
        maxpics = 4
        pic4 = img4

    while True:
        if picno == 1:
            c = easygui.buttonbox(msg="Select Face:", title="Character Creation", choices=("<---", "SELECT", "--->"), image=pic1)
            if c == "<---":
                picno = maxpics
            if c == "SELECT":
                playerPicture = pic1
                return
            if c == "--->":
                picno += 1
        if picno == 2:
            c = easygui.buttonbox(msg="Select Face:", title="Character Creation", choices=("<---", "SELECT", "--->"), image=pic2)
            if c == "<---":
                picno -= 1
            if c == "SELECT":
                playerPicture = pic2
                return
            if c == "--->":
                picno += 1
                if picno > maxpics:
                    picno = 1
        if picno == 3:
            c = easygui.buttonbox(msg="Select Face:", title="Character Creation", choices=("<---", "SELECT", "--->"), image=pic3)
            if c == "<---":
                picno -= 1
            if c == "SELECT":
                playerPicture = pic3
                return
            if c == "--->":
                picno += 1
                if picno > maxpics:
                    picno = 1
        if picno == 4:
            c = easygui.buttonbox(msg="Select Face:", title="Character Creation", choices=("<---", "SELECT", "--->"), image=pic4)
            if c == "<---":
                picno -= 1
            if c == "SELECT":
                playerPicture = pic4
                return
            if c == "--->":
                picno += 1
                if picno > maxpics:
                    picno = 1

load()
debug(playerName)