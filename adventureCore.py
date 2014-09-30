#####
#The main core function/script file for the Legend Of Aiopa Text Adventure
#Most of the functions included in the game are here
#####

#####
#All Module Imports
#####
#Core Import All
from lightCore import * #@UnusedWildImport
#General Modules
import time #@UnusedImport
import random #@UnusedImport
import Core #@UnusedImport
import easygui #@UnresolvedImport @UnusedImport
import sys #@UnusedImport @Reimport
import atexit #@UnusedImport
#####
#End Module Imports
#####

class plr:

    def __init__(self):
        self.name = ""
        self.age = 15
        self.health = 20
        self.cloak = ""
        self.shirt = ""
        self.trouser = ""
        self.knowledge = []
        self.karma = 0
        self.xp = 0
        self.xpl = 1
        self.xpn = 10

    def damage(self, attacker, attackType, amount):
        print(attacker + " " + attackType + " " + self.name + ". " + self.name + " takes " + str(amount) + " damage")
        self.health -= amount

        if self.health < 1:
            self.die()

    def die(self):
        print("You collapse to the ground.")
        print("The world tumbles around you.")
        print("Your vision gets brighter and brighter, until...")
        Core.run(Last_Point)

    def refresh(self):
        if self.health < 1:
            self.die()

    def xpa(self, xp):
        self.xp += xp
        while self.xp > self.xpn:
            if self.xp > self.xpn:
                self.xpl += 1
                self.xp -= self.xpn
                self.xpn *= 1.2
                self.xpn = int(self.xpn)

    def defence(self):
        TheOut = 1
        try:
            TheOut += int(getmet(self.cloak, 1))
        except:
            TheOut += 0
        try:
            TheOut += int(getmet(self.shirt, 1))
        except:
            TheOut += 0
        try:
            TheOut += int(getmet(self.trouser, 1))
        except:
            TheOut += 0

        return int(TheOut)

    def unEquip(self, item):
        debug("Un Equip")

        if item == "cloak":
            inventory.add(self.cloak)
            self.cloak = ""

        if item == "shirt":
            inventory.add(self.shirt)
            self.shirt = ""

        if item == "trouser":
            inventory.add(self.trouser)
            self.trouser = ""

    def equip(self, item):
        debug("equiping:")

        if getmet(item, 0) == "cloak":
            if self.cloak == "":
                self.cloak = item

                inventory.remove(item)

            else:
                inventory.remove(item)
                inventory.add(self.cloak)
                self.cloak = item




        if getmet(item, 0) == "shirt":
            if self.shirt == "":
                self.shirt = item

                inventory.remove(item)

            else:
                inventory.remove(item)
                inventory.add(self.shirt)
                self.shirt = item



        if getmet(item, 0) == "trouser":
            if self.trouser == "":
                self.trouser = item

                inventory.remove(item)

            else:
                inventory.remove(item)
                inventory.add(self.trouser)
                self.trouser = item





    def attack(self, tgt):
        debug("ATTACKING")
        tatt = getmet(tgt, 1)
        tdef = getmet(tgt, 2)
        tlife = getmet(tgt, 3)
        trnk = getmet(tgt, 4)
        taln = getmet(tgt, 5)
        target = getnam(tgt)


        weapons = []
        wdamage = []

        for i in range(0, len(inventory.contents)):

            spl = getmet(inventory.contents[i], 0)

            if spl == "weapon":

                weapons.append(getnam(inventory.contents[i]))

                wdamage.append(getmet(inventory.contents[i], 1))

        weapons.append("Your Fists")
        wdamage.append("2")





        #pprint(Fight_Symbol, self.name + " (" + str(self.health) + ", " + str(self.defence()) + ")" + " Attacks " + target + " (" + str(tlife) + ", " + str(tdef) + ")" + "!")
        pprint(Fight_Symbol, self.name + " (Level " + str(self.xpl) + ")" + " Attacks " + str(target) + " (Level " + str(trnk) + ")" + "!")
        att_weapon = easygui.choicebox(msg="Chose your weapon", choices=(weapons))

        patt = 0

        for i in range(0, len(weapons)):
            if weapons[i] == att_weapon:
                patt = int(wdamage[i])



        while True:
            ###Choose Attacker###
            rnd = random.randint(1,2)

            PtE = int( patt * (1 + random.random())- int(tdef))

            EtP = int( int (tatt) * (1 + random.random()) - self.defence())

            tlife = int(tlife)

            if PtE < 0:
                Rdmg = 0

            if EtP < 0:
                Rdmg2 = 0

            if rnd == 1:
                ###Player Attacks###
                print(self.name + " Attacks!")
                print(self.name + " Deals " + str(PtE) + " Damage To " + target)
                tlife -= PtE
                print(target + " Is Now On " + str(tlife) + " Health.")


                if tlife < 1:
                    print("You defeat " + target + ".")
                    pxp = int((int(trnk) + 1) * (random.randint(1, 3) + random.random()))
                    print("you gain " + str(pxp) + " XP!")
                    pka = int(int(trnk) * (random.randint(1, 2) + random.random()))
                    self.xpa(pka)
                    if taln == "g":
                        print(target + " was good." + "You lose" + str(pka) + " karma")
                        self.karma -= pka
                    if taln == "e":
                        print(target + "was evil." + "You gain" + str(pka) + " karma")
                        self.karma += pka
                    return "win"

                print(target + " Deals " + str(EtP) + " Damage To " + self.name)
                self.health -= EtP
                print(self.name + " Is Now On " + str(self.health) + " Health.")


                if self.health < 1:

                    self.die()


            if rnd == 2:
                ###Opponent Attacks###
                print(target + " Attacks!")
                print(target + " Deals " + str(EtP) + " Damage To " + self.name)
                self.health -= EtP
                print(self.name + " Is Now On " + str(self.health) + " Health.")

                if self.health < 1:
                    self.die()

                print(self.name + " Deals " + str(PtE) + " Damage To " + target)
                tlife -= PtE
                print(target + " Is Now On " + str(tlife) + " Health.")


                if tlife < 1:
                    return "win"

