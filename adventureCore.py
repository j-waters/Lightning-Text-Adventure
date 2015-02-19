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
    easygui.msgbox(msg=string, title=turns())

def pprint(pic, string):
    #easygui picture print
    easygui.msgbox(image=pic, msg=string, title=turns())

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

    if player.Health > player.MaxHealth:
            player.Health = player.MaxHealth

    if player.Mana > player.MaxMana:
        player.Mana = player.MaxMana

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
    TheOut = 0
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
    debug(item)

    if item == "helm":
        inventory_add(player.Helm)
        player.Helm = ""

    if item == "shirt":
        inventory_add(player.Shirt)
        player.Shirt = ""

    if item == "boot":
        inventory_add(player.Boot)
        player.Boot = ""

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
            player.Boot = item

            inventory_remove(item)

        else:
            inventory_remove(item)
            inventory_add(player.Boot)
            player.boot = item
        return

    else:
        print("Cannot equip a " + str(item))

def battle(tgt):
    #Player attacks 'tgt'

    global tlife

    debug("ATTACKING")
    tatt = int(tgt[3]["att"])
    tdef = int(tgt[3]["def"])
    tlife = int(tgt[3]["hlt"])
    tmhlt = int(tgt[3]["mhlt"])
    trnk = int(tgt[3]["rnk"])
    taln = tgt[3]["aln"]
    tspd = int(tgt[3]["spd"])
    tlck = int(tgt[3]["lck"])
    tmgc = int(tgt[3]["mgc"])
    tspl = tgt[3]["spl"]
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
    wpics.append("Pics/Fist01.png")

    #pprint(Fight_Symbol, player.Name + " (" + str(player.Health) + ", " + str(player_defence()) + ")" + " Attacks " + target + " (" + str(tlife) + ", " + str(tdef) + ")" + "!")
    pprint(Fight_Symbol, player.Name + " (Level " + str(player.Xpl) + ")" + " Attacks " + str(target) + " (Level " + str(trnk) + ")" + "! Choose your weapon!")
    #att_weapon = easygui.choicebox(msg="Chose your weapon", choices=(weapons))
    patt = weaponselect(weapons, wdamage, wpics)
    patt = int(patt + int(player.Strength / 2))

    #Calculate personality
    total = tatt + tdef + tmgc
    mgcp = int((tmgc / total) * 100)
    attp = int((tatt / total) * 100) + mgcp
    defp = int((tdef / total) * 100) + attp

    global tempdef
    global tartempdef

    tempdef = 0
    tartempdef = 0

    while True:
        debug("PATT " + str(patt))
        debug("TDEF " + str(tdef))
        debug("PDEF " + str(player_defence() + tempdef))
        PtE = int( patt * (1 + random.random())- (tdef + tartempdef))
        EtP = int( int (tatt) * (1 + random.random()) - (player_defence() + tempdef))
        debug("PtE " + str(PtE))
        debug("EtP " + str(EtP))
        if PtE < 0:
            PtE = 0
        if EtP < 0:
            EtP = 0
        tlife = int(tlife)
        Pcrit = False
        Ecrit = False

        if tspd + random.randint(-2, 2) > player.Speed + random.randint(-2, 2):
            order = "target"
        else:
            order = "player"
        debug(order)

        if random.randint(0, 100) < player.Luck:
            if PtE == 0:
                PtE = 1
            PtE = PtE * ((player.Luck + 10) / 10)
            Pcrit = True
        if random.randint(0, 100) < tlck:
            if EtP == 0:
                EtP = 1
            EtP = EtP * ((tlck + 10) / 10)
            Ecrit = True

        tempdef = 0
        tartempdef = 0

        #NPC decide action
        rdn = random.randint(1, 100)
        if rdn <= attp:
            taction = "Attack"
        elif rdn <= defp:
            taction = "Defend"
        elif rdn <= mgcp:
            taction = "Magic"
        else:
            debug("npc ai error")
            debug("rdn: " + str(rdn))
            debug("defp: " + str(defp))
            debug("attp: " + str(attp))
            debug("mgcp: " + str(mgcp))

        des = easygui.buttonbox(msg="Your Turn!", choices=("Attack", "Defend", "Magic", "Retreat", "Change Weapon"))

        if order == "player":
            player_attack(des, Pcrit, PtE, target, tgt)

            if tlife < 1:
                print("You defeat " + target + ".")
                pxp = int((int(trnk) + 1) * (random.randint(1, 3) + random.random()))
                print("you gain " + str(pxp) + " XP!")
                pka = int(int(trnk) * (random.randint(1, 2) + random.random()))
                player_Xpa(pka)
                if taln == "G":
                    print(target + " was good. " + "You lose " + str(pka) + " karma")
                    debug("Pre karma: " + str(player.Karma))
                    player.Karma -= pka
                    debug("Post karma: " + str(player.Karma))
                if taln == "E":
                    print(target + "was evil. " + "You gain " + str(pka) + " karma")
                    player.Karma += pka
                return "win"

            enemy_attack(taction, Ecrit, target, tlck, EtP, tdef, tatt, tlife, tmhlt, tmgc, tspl)
            player_refresh()

        if order == "target":
            enemy_attack(taction, Ecrit, target, tlck, EtP, tdef, tatt, tlife, tmhlt, tmgc, tspl)
            player_refresh()
            player_attack(des, Pcrit, PtE, target, tgt)

            if tlife < 1:
                print("You defeat " + target + ".")
                pxp = int((int(trnk) + 1) * (random.randint(1, 3) + random.random()))
                print("you gain " + str(pxp) + " XP!")
                pka = int(int(trnk) * (random.randint(1, 2) + random.random()))
                player_Xpa(pka)
                if taln == "G":
                    print(target + " was good. " + "You lose " + str(pka) + " karma")
                    debug("Pre karma: " + str(player.Karma))
                    player.Karma -= pka
                    debug("Post karma: " + str(player.Karma))
                if taln == "E":
                    print(target + "was evil. " + "You gain " + str(pka) + " karma")
                    player.Karma += pka
                return "win"

def player_attack(des, Pcrit, PtE, target, tgt):
    global tempdef
    global tlife
    if des == "Attack":
        print(player.Name + " Attacks!")
        if Pcrit == True:
            print("Critical Hit! x" + str(((player.Luck + 10) / 10)))
        print(player.Name + " Deals " + str(PtE) + " Damage To " + target)
        tlife -= PtE
        print(target + " Is Now On " + str(tlife) + " Health.")

    if des == "Defend":
        print(player.Name + " Is Defending.")
        tempdef = int(player.Strength / 2)
        debug("tempdef " + str(tempdef))

    if des == "Magic":
        if not player.Spells == []:
            spl = easygui.choicebox(msg="Choose A Spell To Cast", title=turns(), choices=player.Spells)
            player_magicCast(spl)
        else:
            print("You have no spells")

    if des == "Retreat":
        world.Places[world.Location][lfind(world.Places[world.Location], tgt)][3]["hlt"] = tlife
        return "Retreat"

    if des == "Change Weapon":
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
        wpics.append("Pics/Fist01.png")
        patt = weaponselect(weapons, wdamage, wpics)
        patt = int(patt + player.Strength)




def enemy_attack(taction, Ecrit, target, tlck, EtP, tdef, tatt, tlife, tmhlt, tmgc, tspl):
    global tartempdef
    if taction == "Attack":
        print(target + " Attacks!")
        if Ecrit == True:
            print("Critical Hit! x" + str(((tlck + 10) / 10)))

        print(target + " Deals " + str(EtP) + " Damage To " + player.Name)
        player.Health -= EtP
        print(player.Name + " Is Now On " + str(player.Health) + " Health.")

    if taction == "Defend":
        print(target + " Is Defending.")
        tartempdef = int(tatt / 2)

    if taction == "Magic":
        spell = target_magicCast(target, tlife, tmhlt, tmgc, tspl)
        if spell == "heal":
            amount = tmgc * random.randint(1, 2)
            print(target + "casts 'heal' and recovers " + str(amount) + " health")
            tlife += amount
            if tlife > tmhlt:
                tlife = tmhlt
            print(target + "is now on " + str(tlife) + " Health")

def player_magicCast(spell):
    if player.Spells.__contains__(spell) == False:
        return "No Spell"
    if spell == "heal":
        if player.Mana >= 3:
            player.Mana -= 3
            player_refresh()
            amount = player.Magic * random.randint(1, 2)
            print("You cast 'heal' recovering " + str(amount) + " health")
            player.Health += amount
            player_refresh()
            print("You now have " + str(player.Health) + " Health")
        else:
            print("You do not have enough Mana to cast the spell heal! You only have " + player.Mana + " Mana!")

def player_addMana():
    amount = player.Magic + int(player.Luck / 10)
    player.Mana += amount
    player_refresh()
#####
#END PLAYER
#####

def target_magicCast(name, tlife, tmlife, tmgc, tspl):
    if tspl.__contains__("heal") == True:
        if tlife < tmlife / 2:
            return "heal"

#####
#INVENTORY
#####

def inventory_add(item):

    debug("ADD TO INVENTORY:")
    #This bit will have problems with lists of items due to the 1
    if 1 + len(inventory.Contents) > inventory.Size:
        debug(inventory.Size)
        pprint(Full_Bag, "You can't fit anything else into a bag that can only hold " + str(inventory.Size) + " items!")

        INV_A_DC = easygui.choicebox(msg="What to drop: (cancel to not drop anything)", choices=(getnam(inventory.Contents)))
        if not INV_A_DC == None:
            INV_A_DC = find_tup(INV_A_DC, inventory.Contents)
            inventory_remove(INV_A_DC)
        if INV_A_DC == None:
            return False

    inventory.Contents.append(item)
    return True




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
    mstringm = []
    inventory.Contents.append((mstring, mstringd, mstringm))

    ##done money##

    ##adding equipped items to inventory##

    estring1 = "You Have Equipped: "
    try:
        if not player.Helm == "":
            estring2 = player.Helm[0]
            estring2d = player.Helm[1]
            estring2m = ["e", "helm", player.Helm[2][1]]
            estring2p = player.Helm[3]

        if player.Helm == "":
            estring2 = "No helm"
            estring2d = "Your not wearing a helmet"
            estring2m = []
            estring2p = ""
    except:
        estring2 = "No helm"
        estring2d = "Your not wearing a helmet"
        estring2m = []
        estring2p = ""

    try:
        if not player.Shirt == "":
            estring3 = player.Shirt[0]
            estring3d = player.Shirt[1]
            estring3m = ["e", "shirt", player.Shirt[2][1]]
            estring3p = player.Shirt[3]

        if player.Shirt == "":
            estring3 = "No Extra Shirt"
            estring3d = "Your not wearing any extra shirt"
            estring3m = []
            estring3p = ""
    except:
        estring3 = "No Extra Shirt"
        estring3d = "Your not wearing an extra shirt"
        estring3m = []
        estring3p = ""

    try:
        if not player.Boot == "":
            estring4 = player.Boot[0]
            estring4d = player.Boot[1]
            estring4m = ["e", "boot", player.Boot[2][1]]
            estring4p = player.Boot[3]

        if player.Boot == "":
            estring4 = "No Extra boots"
            estring4d = "Your not wearing any boots"
            estring4m = []
            estring4p = ""
    except:
        estring4 = "No Extra boot"
        estring4d = "Your not wearing any boots"
        estring4m = []
        estring4p = ""

    inventory.Contents.append((estring1 + estring2,estring2d, estring2m, estring2p))
    inventory.Contents.append((estring1 + estring3,estring3d, estring3m, estring3p))
    inventory.Contents.append((estring1 + estring4,estring4d, estring4m, estring4p))

    ##adding player stats##
    pstring = "Your Statistics"
    pstringd = "Ooops"
    pstringm = ["stats"]
    inventory.Contents.append((pstring, pstringd, pstringm))

    ##showing inventory##

    selected = easygui.choicebox(msg = "Your Inventory:", choices=(getnam(inventory.Contents)))

    selected = find_tup(selected, inventory.Contents)

    inventory.Contents.remove((mstring, mstringd, mstringm))
    inventory.Contents.remove((pstring, pstringd, pstringm))
    inventory.Contents.remove((estring1 + estring2,estring2d, estring2m, estring2p))
    inventory.Contents.remove((estring1 + estring3,estring3d, estring3m, estring3p))
    inventory.Contents.remove((estring1 + estring4,estring4d, estring4m, estring4p))

    debug("\n selected:")
    debug(selected)

    if selected == None:
        return "exit"

    IgI = None
    verb = "Use"

    if type(selected) == list:
        selected = selected[0]

    debug(getmet(selected, "all"))

    if getmet(selected, "all") == ['stats']:
        statistics()
    elif getnam(selected) == mstring:
        pprint(Coin, getdes(selected))
    elif getmet(selected, "all") == []:
        print(getdes(selected))
    elif getmet(selected, "all") == ["i"]:
        #Is it an average item?
        easygui.buttonbox(image=getpic(selected), msg=getdes(selected), choices=("Back", "Discard"))
    elif searchmet("e", selected) == True:
        #Is it an equipped item?
        IgI = easygui.buttonbox(image=getpic(selected), msg=getdes(selected), choices=("Back", "Un Equip"))
        if IgI == "Un Equip":
            player_unEquip(getmet(selected, 1))
    elif searchmet("c", selected) == True:
        #Is it an eqipable item?
        IgI = easygui.buttonbox(image=getpic(selected), msg=getdes(selected), choices=("Back", "Equip", "Discard"))
        if IgI == "Equip":
            player_equip(selected)
    elif searchmet("u", selected):

        if searchmet("book", selected) == True:
            verb = "Read"
        if searchmet("map", selected) == True:
            verb = "Read"

        IgI = easygui.buttonbox(image = getpic(selected), msg = getdes(selected), choices =("Back", verb, "Discard"))

    if IgI == "Discard":
        inventory_remove(selected)
    if IgI == verb:
        if getmet(selected, 0) == "book":
            read(selected)
        if getmet(selected, 0) == "map":
            read(selected)
        #other items


    inventory_get()
    return

def inventory_remove(item):
    world.Places[world.Location].append(item)
    inventory.Contents.remove(item)

#####
#END INVENTORY
#####

#####
#WORLD
#####

def turns():
    return world.TurnString + str(world.Turn)

def world_refresh():
    for i in world.Places[world.Location]:
        if getmet(i, 0) == "npc":
            if i[3]["hlt"] < 1:
                world.Places[world.Location].remove(i)

#####
#END WORLD
#####

def getmet(item, metno):
    #Gets the metadata from a tuple (item)
    #finds the correct metadata by number (metno)
    TheOut = None

    if type(item) == tuple:
        if metno == "all":
            TheOut = item[2]
            return TheOut

        TheOut = item[2][metno]

    if type(item) == list:
        debug("GETMET HAS DONE A LIST")
        Error()
        if metno == "all":
            TheOut = item[0][2]
            return TheOut
        TheOut = item[0][2][metno]

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

    for i in item:
        if i == string:
            return True

    return False

def input(string):  # @ReservedAssignment
    #Creates an enter box with a string, and the time as the title
    TheInput = easygui.enterbox(msg=string, title=turns())
    return TheInput

def options(pic, string, op1, op2, op3=None, op4=None):
    #creates an button box with 2, up to 4 choices
    if not op4 == None:
        TheOut = easygui.buttonbox(choices=(op1, op2, op3, op4, "Inventory"), msg=string, image=pic, title=turns())
    if op4 == None:
        TheOut = easygui.buttonbox(choices=(op1, op2, op3, "Inventory"), msg=string, image=pic, title=turns())
    if op4 and op3 == None:
        TheOut = easygui.buttonbox(choices=(op1, op2, "Inventory"), msg=string, image=pic, title=turns())

    if TheOut == "Inventory":
        inventory_get()
        TheOut = options(pic, string, op1, op2, op3, op4)

    return TheOut

def move(choices):
    #Shows a choicebox with places that the player can move to
    #returns the selection

    choices = [i for i in choices if searchmet("building", i) == True]

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

        TheOut = easygui.choicebox(msg=string, choices=(t(items, 0)), title=turns())

        if TheOut == None:
            return

        TheOut = find_tup(TheOut, items)

        if searchmet("i", TheOut) == True:
            choice = easygui.buttonbox(image=getpic(TheOut), msg=getdes(TheOut), choices=("Take", "Back"))
        else:
            choice = easygui.buttonbox(image=getpic(TheOut), msg=getdes(TheOut), choices=("Back"))

        if choice == "Take":
            if inventory_add(TheOut) == True:
                world.Places[world.Location].remove(TheOut)
                return "Take"
        else:
            return

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
    player_refresh()
    world_refresh()
    while True:
        chs = ["Look Around", "Move Somewhere", "View Inventory"]
        for i in things:
            if getmet(i, 0) == "npc":
                chs.append("Interact With Something")
                break

        des = easygui.buttonbox(msg="What Will You Do?", title=turns(), choices=(chs))
        if des == "Look Around":
            view(things)
        if des == "Move Somewhere":
            move(things)
        if des == "View Inventory":
            inventory_get()
        if des == "Interact With Something":
            soth = []
            for i in things:
                if getmet(i, 0) == "npc":
                    soth.append(i)
            something = easygui.choicebox(msg="You can interact with...", title=turns(), choices=t(soth, 0))
            something = find_tup(something, things)
            if getmet(something, 0) == "npc":
                des = easygui.buttonbox(msg="Interact With " + getnam(something), title=turns(), choices=("Talk", "Attack"))
                if des == "Talk":
                    talk(something)
                if des == "Attack":
                    battle(something)

        if des == None:
            exit()

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
    dic = person[4]
    printTree(dic)
    #rdm = random.randint(1, len(dic))
    otn = []
    otndic = []
    for key in dic:
        if list(key)[0] == "O":
            otn.append(dic[key]["B"])
            otndic.append(dic[key])
    c = easygui.buttonbox(msg=dic["T"], title=turns(), choices=otn)

    for d in otndic:
        if d["B"] == c:
            cur = d

    while True:
        otn = []
        otndic = []
        end = False
        debug(cur)
        for key in cur:
            if list(key)[0] == "O":
                otn.append(cur[key]["B"])
                otndic.append(cur[key])

            if list(key)[0] == "R":
                exec(cur[key]["R"])

            if list(key)[0] == "E":
                if cur[key] == "E":
                    return
                if type(cur[key]) == list:
                    cur = reduce(lambda a, b: a[b], cur[key], dic)
                    end = True
        if end == False:
            if cur.get("T") == None:
                return
            if type(cur["T"]) == list:
                for i in cur["T"]:
                    c = easygui.buttonbox(msg=i, title=turns(), choices=otn)
            else:
                c = easygui.buttonbox(msg=cur["T"], title=turns(), choices=otn)

            for d in otndic:
                if d["B"] == c:
                    cur = d

def statistics():
    cur = 0
    items = ["Your Physical Attributes:" + "\nStrength: " + str(player.Strength) + "\nHealth: " + str(player.Health) + "/" + str(player.MaxHealth) + "\nSpeed: " + str(player.Speed) + "\nDefence: " + str(player_defence()),
             "Your Mental Attributes:" + "\nMagical Strength: " + str(player.Magic) + "\nMana: " + str(player.Mana) + "/" + str(player.MaxMana) + "\nKarma: " + str(player.Karma) + "\nLuck: " + str(player.Luck),
             "Your Spells:\n" + '\n'.join(player.Spells),
             "Your Knowledge:\n" + '\n'.join(player.Knowledge)]
    while True:
        debug(cur)
        choice = easygui.buttonbox(msg=items[cur], title=turns(), choices=("<---", "Back", "--->"), image=player.Picture)

        if choice == "<---":
            cur -= 1
        if choice == "--->":
            cur += 1
        if choice == "Back":
            return

        if cur > len(items) - 1:
            cur = 0
        if cur < 0:
            cur = len(items) - 1

def exit():
    if easygui.ynbox(msg="Are You Sure You Want To Exit? The Game Will Save.") == True:
        #player.save()
        #inventory.save()
        #world.save()
        sys.exit()