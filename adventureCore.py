#####
#The main core function/script file for the Legend Of Aiopa Text Adventure
#Most of the functions included in the game are here
#####

#####
#All Module Imports

#Core Import All
from lightCore import * #@UnusedWildImport
import player
import world
import inventory
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
    easygui.msgbox(msg=string, title=world.time())

def pprint(pic, string):
    #easygui picture print
    easygui.msgbox(image=pic, msg=string, title=world.time())

#####
#Pictures
#####
Full_Bag = "Pics/Bag Full.png"
Fight_Symbol = "Pics/Fight.png"
Coin = "Pics/BronzeCoin.png"

#####
#PLAYER
#####

def player_damage(attacker, attackType, amount):
    #Deals damage to the player, displaying who did it
    print(attacker + " " + attackType + " " + player.Name + ". " + player.Name + " takes " + str(amount) + " damage")
    player.Health -= amount

    if player.Health < 1:
        player_die()

def player_die():
    #Displays the death message, and then returns you to your previous spot
    print("You collapse to the ground.")
    print("The world tumbles around you.")
    print("Your vision gets brighter and brighter, until...")
    #run(Last_Point)

def player_refresh():
    #Does a check of multiple player variables, checking if they make sense.
    if player.Health < 1:
        player_die()

def player_Xpa(xp):
    #Adds 'xp' XP to the players xp, checking if the player level can be increased
    player.Xp += xp
    while player.Xp > player.Xpn:
        if player.Xp > player.Xpn:
            player.Xpl += 1
            player.Xp -= player.Xpn
            player.Xpn *= 1.2
            player.Xpn = int(player.Xpn)

def player_defence():
    #Calculates the defence of a player
    TheOut = 1
    try:
        TheOut += int(getmet(player.Helm, 1))
    except:
        TheOut += 0
    try:
        TheOut += int(getmet(player.Shirt, 1))
    except:
        TheOut += 0
    try:
        TheOut += int(getmet(player.Boot, 1))
    except:
        TheOut += 0

    return int(TheOut)

def player_unEquip(item):
    #Unequips an item from the player
    debug("Un Equip")

    if item == "helm":
        inventory_add(player.Helm)
        player.Helm = ""

    if item == "shirt":
        inventory_add(player.Shirt)
        player.Shirt = ""

    if item == "boot":
        inventory_add(player.Boot)
        player.boot = ""

def player_equip(item):
    #Equips an item to the player
    debug("equiping:")
    debug(item)
    debug(getmet(item, 0))

    if getmet(item, 0) == "helm":
        if player.Helm == "":
            player.Helm = item
            inventory_remove(item)

        else:
            inventory_remove(item)
            inventory_add(player.Helm)
            player.Helm = item
        return




    if getmet(item, 0) == "shirt":
        if player.Shirt == "":
            player.Shirt = item
            inventory_remove(item)

        else:
            inventory_remove(item)
            inventory_add(player.Shirt)
            player.Shirt = item
        return



    if getmet(item, 0) == "boot":
        if player.Boot == "":
            player.boot = item

            inventory_remove(item)

        else:
            inventory_remove(item)
            inventory_add(player.Boot)
            player.boot = item
        return

    else:
        print("Cannot equip a " + str(item))



def player_attack(tgt):
    #Player attacks 'tgt'
    debug("ATTACKING")
    tatt = int(getmet(tgt, 1))
    tdef = int(getmet(tgt, 2))
    tlife = int(getmet(tgt, 3))
    trnk = int(getmet(tgt, 4))
    taln = getmet(tgt, 5)
    tspd = int(getmet(tgt, 6))
    tlck = int(getmet(tgt, 7))
    target = getnam(tgt)

    weapons = []
    wdamage = []
    wpics = []

    for i in range(0, len(inventory.Contents)):
        spl = getmet(inventory.Contents[i], 0)
        if spl == "weapon":
            weapons.append(getnam(inventory.Contents[i]))
            wdamage.append(getmet(inventory.Contents[i], 1))
            wpics.append(getpic(inventory.Contents[i]))

    weapons.append("Your Fists")
    wdamage.append(player.Strength)
    wpics.append("Fist01.png")

    #pprint(Fight_Symbol, player.Name + " (" + str(player.Health) + ", " + str(player_defence()) + ")" + " Attacks " + target + " (" + str(tlife) + ", " + str(tdef) + ")" + "!")
    pprint(Fight_Symbol, player.Name + " (Level " + str(player.Xpl) + ")" + " Attacks " + str(target) + " (Level " + str(trnk) + ")" + "! Choose your weapon!")
    #att_weapon = easygui.choicebox(msg="Chose your weapon", choices=(weapons))
    patt = weaponselect(weapons, wdamage, wpics)
    debug(patt)
    debug(type(patt))

    while True:
        PtE = int( patt * (1 + random.random())- int(tdef))
        EtP = int( int (tatt) * (1 + random.random()) - player_defence())
        tlife = int(tlife)
        Pcrit = False
        Ecrit = False

        des = easygui.buttonbox(msg="Your Turn!", choices=("Attack", "Defend", "Magic", "Retreat", "Change Weapon"))

        if des == "Attack":
            if tspd + random.randint(-2, 2) > player.Speed + random.randint(-2, 2):
                order = "target"
            elif tspd + random.randint(-2, 2) < player.Speed + random.randint(-2, 2):
                order = "player"
            else:
                rdm = random.randint(1,2)
                if rdm == 1:
                    order = "target"
                if rdm == 1:
                    order = "player"

            if PtE < 0:
                PtE = 0

            if EtP < 0:
                EtP = 0

            if random.randint(0, 100) < player.Luck:
                PtE = PtE * [int(i) for i in str(player.Luck)][0]
                Pcrit = True
            if random.randint(0, 100) < player.Luck:
                EtP = EtP * [int(i) for i in str(tlck)][0]
                Ecrit = True

            if order == "player":
                print(player.Name + " Attacks!")
                if Pcrit == True:
                    print("Critical Hit! x" + list(str(player.Luck))[0])
                print(player.Name + " Deals " + str(PtE) + " Damage To " + target)
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
                        player.Karma -= pka
                    if taln == "e":
                        print(target + "was evil." + "You gain" + str(pka) + " karma")
                        player.Karma += pka
                    return "win"

                print(target + "Attacks!")
                if Ecrit == True:
                    print("Critical Hit! x" + list(str(tlck))[0])

                print(target + " Deals " + str(EtP) + " Damage To " + player.Name)
                player.Health -= EtP
                print(player.Name + " Is Now On " + str(player.Health) + " Health.")

                if player.Health < 1:

                    player_die()

            if order == "target":
                print(target + " Attacks!")
                if Ecrit == True:
                    print("Critical Hit! x" + list(str(tlck))[0])
                print(target + " Deals " + str(EtP) + " Damage To " + player.Name)
                player.Health -= EtP
                print(player.Name + " Is Now On " + str(player.Health) + " Health.")

                if player.Health < 1:

                    player_die()

                print(player.Name + "Attacks!")
                if Pcrit == True:
                    print("Critical Hit! x" + list(str(player.Luck))[0])

                print(player.Name + " Deals " + str(PtE) + " Damage To " + target)
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
                        player.Karma -= pka
                    if taln == "e":
                        print(target + "was evil." + "You gain" + str(pka) + " karma")
                        player.Karma += pka

                    return "win"



#####
#END PLAYER
#####

#####
#INVENTORY
#####

def inventory_add(item):

    debug("ADD TO INVENTORY:")
    #This bit will have problems with lists of items due to the 1
    if 1 + len(inventory.Contents) > inventory.Size:
        debug(inventory.Size)
        spaceleft = inventory.Size - len(inventory.Contents)
        things = len(item)
        pprint(Full_Bag, "You Can't fit " + str(things) + " More item in a bag that can only hold " + str(spaceleft) + " more items!")

        INV_A_DC = easygui.choicebox(msg="What to discard: (cancel to not discard anything)", choices=(inventory.Contents))
        if not INV_A_DC == None:
            inventory_remove(INV_A_DC)
        if INV_A_DC == None:
            return

    else:
        if type(item) == tuple:
            inventory.Contents.append(item)

        if type(item) == list:
            for i in range(len(item)):

                inventory.Contents.append(item[i])




def inventory_get():
    debug("INVENTORY")
    debug("CONTENTS:\n" + str(inventory.Contents))
    ##Finding Money##
    for i in range(0, len(inventory.Contents)):
        spl = getmet(inventory.Contents[i], 0)
        if spl == "money":
            amt = getmet(inventory.Contents[i], 1)
            amti = int(amt)
            type(amti)
            inventory.Money += amti
            del inventory.Contents[i]
            break

    if inventory.Money % 10 == 0:
        inventory.Money = 0

    ##adding money string to inventory###

    mstring = "You Have: " + str(inventory.Money) + " Gold"
    mstringd = "Your small bag of money full of coins that are known as 'gold' by the comoners"
    mstringm = ""
    inventory.Contents.append((mstring, mstringd, mstringm))

    ##done money##

    ##adding equipped items to inventory##

    estring1 = "You Have Equipped: "
    try:
        if not player.Helm == "":
            estring2 = player.Helm[0]
            estring2d = player.Helm[1]
            estring2m = "e|helm"

        if player.Helm == "":
            estring2 = "No helm"
            estring2d = "Your not wearing a helm"
            estring2m = ""
    except:
        estring2 = "No helm"
        estring2d = "Your not wearing a helm"
        estring2m = ""

    try:
        if not player.Shirt == "":
            estring3 = player.Shirt[0]
            estring3d = player.Shirt[1]
            estring3m = "e|shirt"

        if player.Shirt == "":
            estring3 = "No Extra Shirt"
            estring3d = "Your not wearing any extra shirt"
            estring3m = ""
    except:
        estring3 = "No Extra Shirt"
        estring3d = "Your not wearing an extra shirt"
        estring3m = ""

    try:
        if not player.Boot == "":
            estring4 = player.Boot[0]
            estring4d = player.Boot[1]
            estring4m = "e|boot"

        if player.Boot == "":
            estring4 = "No Extra boots"
            estring4d = "Your not wearing any over boots"
            estring4m = ""
    except:
        estring4 = "No Extra boot"
        estring4d = "Your not wearing any over boots"
        estring4m = ""

    inventory.Contents.append((estring1 + estring2,estring2d, estring2m))
    inventory.Contents.append((estring1 + estring3,estring3d, estring3m))
    inventory.Contents.append((estring1 + estring4,estring4d, estring4m))

    ##adding player stats##
    pstring = "Your Statistics"
    pstringd = "Your Stats:\n" + "Health: " + str(player.Health) + "\nDefence: " + str(player_defence())
    pstringm = ""
    inventory.Contents.append((pstring, pstringd, pstringm))

    ##showing inventory##

    vop = easygui.choicebox(msg = "Your Inventory:", choices=(getnam(inventory.Contents)))

    vop = find_tup(vop, inventory.Contents)

    inventory.Contents.remove((mstring, mstringd, mstringm))
    inventory.Contents.remove((pstring, pstringd, pstringm))
    inventory.Contents.remove((estring1 + estring2,estring2d, estring2m))
    inventory.Contents.remove((estring1 + estring3,estring3d, estring3m))
    inventory.Contents.remove((estring1 + estring4,estring4d, estring4m))

    debug("\n VOP:")
    debug(vop)

    if vop == None:
        return "exit"

    if type(vop) == list:
        vop = vop[0]

    if getnam(vop) == pstring:
        pprint(player.Picture, getdes(vop))
    elif getnam(vop) == mstring:
        pprint(Coin, getdes(vop))
    elif getmet(vop, "all") == "i":
        #Is it an average item?
        pprint(getpic(vop), getdes(vop))
    elif searchmet("e", vop) == "T":
        #Is it an equipped item?
        IgI = easygui.buttonbox(image=getpic(vop), msg=getdes(vop), choices=("Back", "Un Equip"))
        if IgI == "Un Equip":
            player_unEquip(getmet(vop, 1))
    elif searchmet("c", vop) == "T":
        #Is it an eqipable item?
        IgI = easygui.buttonbox(image=getpic(vop), msg=getdes(vop), choices=("Back", "Equip"))
        if IgI == "Equip":
            player_equip(vop)
    else:
        verb = "Use"
        if searchmet("book", vop) == "T":
            verb = "Read"
        if searchmet("map", vop) == "T":
            verb = "Read"

        IgI = options(getpic(vop), getdes(vop), "Discard", verb, "Back")

        if IgI == "Discard":
            inventory_remove(vop)
        if IgI == verb:
            if getmet(vop, 0) == "book":
                read(vop)
            if getmet(vop, 0) == "map":
                read(vop)
            #other items


    inventory_get()
    return

def inventory_remove(item):
    inventory.Contents.remove(item)

#####
#END INVENTORY
#####

def getmet(item, metno):
    #Gets the metadata from a tuple (item)
    #finds the correct metadata by number (metno)
    TheOut = None

    if type(item) == tuple:
        if metno == "all":
            TheOut = item[2]
            return TheOut

        TheOut = item[2].split('|')[metno]

    if type(item) == list:
        if metno == "all":
            TheOut = item[0][2]
            return TheOut
        TheOut = item[0][2].split('|')[metno]

    return TheOut

def getdes(item):
    #Gets the description from a tuple (item)
    TheOut = item[1]
    return TheOut

def getpic(item):
    #Gets the image from a tuple (item)
    debug(item)
    if type(item) == tuple:
        TheOut = item[3]
        TheOut = "Pics/" + TheOut
        return TheOut
    if type(item) == str:
        TheOut = "Pics/" + TheOut
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

    for i in range(0, len(item.split('|'))):
        if item.split('|')[i] == string:
            return "T"

    return "F"

def input(string):  # @ReservedAssignment
    #Creates an enter box with a string, and the time as the title
    TheInput = easygui.enterbox(msg=string, title=world.time())
    return TheInput

def options(pic, string, op1, op2, op3=None, op4=None):
    #creates an button box with 2, up to 4 choices
    if not op4 == None:
        TheOut = easygui.buttonbox(choices=(op1, op2, op3, op4, "Inventory"), msg=string, image=pic, title=world.time())
    if op4 == None:
        TheOut = easygui.buttonbox(choices=(op1, op2, op3, "Inventory"), msg=string, image=pic, title=world.time())
    if op4 and op3 == None:
        TheOut = easygui.buttonbox(choices=(op1, op2, "Inventory"), msg=string, image=pic, title=world.time())

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

def view(items, string="You Can See:"):
    #Creates a choicebox from a list
    #Can use a string, by default shows 'you can see:'

    while True:
        TheOut = ""
        str(TheOut)

        TheOut = easygui.choicebox(msg=string, choices=(t(items, 0)), title=world.time())

        if TheOut == None:
            return

        TheOut = find_tup(TheOut, items)
        pprint(getpic(TheOut), getdes(TheOut))

def take(choices, mmax=0, string="You Can Take:"):
    #Takes an item and places it into the players inventory
    #Returns the item
    debug("TAKING")

    choices = [i for i in choices if searchmet("i", i) == "T"]

    TheOut = easygui.multchoicebox(msg=string, choices=(t(choices, 0)))
    debug(TheOut)

    if TheOut == None:
        return

    if len(TheOut) > mmax:
        if not mmax == 0:
            print("You can only take " + mmax + " items.")
            return

    inventory_add(find_tup(TheOut, choices))
    return find_tup(TheOut, choices)

def read(item):
    book = getmet(item, 1)
    book = "Books/" + book
    importVar(book)
    if getmet(item, 0) == "book":
        print("Knowledge Acquired! " + getmet(item, 1) + "!")
        player.Knowledge.append(getmet(item, 1))

def player_picture():
    pic1 = "Pics/Player_1.png"
    pic2 = "Pics/Player_2.png"
    pic3 = "Pics/Player_3.png"
    pic4 = "Pics/Player_4.png"

    picno = 1

    while True:
        if picno == 1:
            c = easygui.buttonbox(msg="What will you look like?", title="Character Creation", choices=("<---", "SELECT", "--->"), image=pic1)
            if c == "<---":
                picno = 4
            if c == "SELECT":
                player.Picture = pic1
                return
            if c == "--->":
                picno += 1
        if picno == 2:
            c = easygui.buttonbox(msg="What will you look like?", title="Character Creation", choices=("<---", "SELECT", "--->"), image=pic2)
            if c == "<---":
                picno -= 1
            if c == "SELECT":
                player.Picture = pic2
                return
            if c == "--->":
                picno += 1
                if picno > 4:
                    picno = 1
        if picno == 3:
            c = easygui.buttonbox(msg="What will you look like?", title="Character Creation", choices=("<---", "SELECT", "--->"), image=pic3)
            if c == "<---":
                picno -= 1
            if c == "SELECT":
                player.Picture = pic3
                return
            if c == "--->":
                picno += 1
                if picno > 4:
                    picno = 1
        if picno == 4:
            c = easygui.buttonbox(msg="What will you look like?", title="Character Creation", choices=("<---", "SELECT", "--->"), image=pic4)
            if c == "<---":
                picno -= 1
            if c == "SELECT":
                player.Picture = pic4
                return
            if c == "--->":
                picno += 1
                if picno > 4:
                    picno = 1

def player_name():
    player.Name = easygui.enterbox(msg="What will you be known as?", title="Character Creation", image=player.Picture)
    if player.Name == "":
        player.Name = "Person"
    return

def choices(things):
    while True:
        chs = ["Look Around","Take Something", "Move Somewhere", "View Inventory"]
        for i in things:
            if getmet(i, 0) == "npc":
                chs.append("Interact With Something")
                break

        des = easygui.buttonbox(msg="What Will You Do?", title=world.time(), choices=(chs))

        if des == "Look Around":
            view(things)
        if des == "Take Something":
            take(things)
        if des == "Move Somewhere":
            move(things)
        if des == "View Inventory":
            inventory_get()
        if des == "Interact With Something":
            soth = []
            for i in things:
                if getmet(i, 0) == "npc":
                    soth.append(i)

            something = easygui.choicebox(msg="You can interact with...", title=world.time(), choices=t(soth, 0))
            something = find_tup(something, things)
            if getmet(something, 0) == "npc":
                des = easygui.buttonbox(msg="Interact With " + getnam(something), title=world.time(), choices=("Talk", "Attack"))
                if des == "Talk":
                    talk(something)
                if des == "Attack":
                    player_attack(something)

def selector(things, pictures, string, metno, title):
    #insert %m in string to replace that with output from metno
    #insert %t in string to replace that with thing name
    items = []
    names = []
    nmax = len(things)
    for i in range(0, len(things)):
        item = getnam(things[i])
        met = getmet(things[i], metno)
        line = string
        line.replace("%m", met)
        line.replace("%t", item)
        items.append(line)
        names.append(item)

    num = 0
    while True:

        out = easygui.buttonbox(msg=items[num], title=title, choices=("<---", "SELECT", "--->"), image=pictures[num])
        if out == "<---":
            num -= 1
            if num < 0:
                num = nmax
            if out == "SELECT":
                for i in names:
                    for t in things:
                        if getnam(t) == i[num]:
                            TheOut = t
                return TheOut
        if out == "--->":
            num += 1
            if num > nmax:
                num = 0

def weaponselect(weapon, wdamage, pic):
    nmax = len(weapon) - 1
    num = 0
    while True:
        string = weapon[num] + ": Does " + str(wdamage[num]) + " Damage."
        out = easygui.buttonbox(msg=string, title="Choose Your Weapon:", choices=("<---", "SELECT", "--->"), image=pic[num])
        if out == "<---":
            num -= 1
            if num < 0:
                num = nmax
        if out == "SELECT":
            return wdamage[num]
        if out == "--->":
            num += 1
            if num > nmax:
                num = 0

def talk(person):
    dic = person[3]
    printTree(dic)
    #rdm = random.randint(1, len(dic))
    otn = []
    otndic = []
    for key in dic:
        if list(key)[0] == "O":
            otn.append(dic[key]["B"])
            otndic.append(dic[key])
    c = easygui.buttonbox(msg=dic["T"], title=world.time(), choices=otn)

    for d in otndic:
        if d["B"] == c:
            cur = d

    while True:
        otn = []
        otndic = []
        hi = {}
        for key in cur:
            if list(key)[0] == "O":
                otn.append(cur[key]["B"])
                otndic.append(cur[key])

            if list(key)[0] == "R":
                exec(cur[key]["R"])

            if list(key)[0] == "E":
                for i in cur[key]:
                    hi = dic[i]
                cur = hi
        if hi == {}:
            if otn == []:
                otn.append("...")
            c = easygui.buttonbox(msg=cur["T"], title=world.time(), choices=otn)

            for d in otndic:
                if d["B"] == c:
                    cur = d
