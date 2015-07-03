from lightCore import *


class Item:

    def __init__(self, name, nameish, description, weight, cost, image):
        self.weight = weight
        self.cost = cost
        self.name = name
        self.nameish = nameish
        self.description = description
        self.image = image
        self.cat = "Item"

class Equipped():

    def __init__(self, item, itype=None):
        if item == None:
            self.image = None
            self.defence = 0
            self.description = "You're not wearing any " + itype
            self.name = "No extra " + itype
            self.type = "UnEquiped " + itype
        else:
            self.item = item
            self.image = self.item.image
            self.defence = self.item.defence
            self.description = self.item.description
            self.name = "You Have Equiped: " + self.item.name
            self.type = "Equiped " + self.item.type

class InventoryString():

    def __init__(self, name, type, description=""):
        self.name = name
        self.type = type
        self.description = description
        self.cat = "Empty"



class Shirt(Item):

    def __init__(self, name, nameish, description, defence, weight, cost, image, enchantments=[]):
        self.defence = defence
        Item.__init__(self, name, nameish, description, weight, cost, image)
        self.enchantments = enchantments
        self.type = "Shirt"

class Helmet(Item):

    def __init__(self, name, nameish, description, defence, weight, cost, image, enchantments=[]):
        self.defence = defence
        Item.__init__(self, name, nameish, description, weight, cost, image)
        self.enchantments = enchantments
        self.type = "Helmet"

class Leggins(Item):

    def __init__(self, name, nameish, description, defence, weight, cost, image, enchantments=[]):
        self.defence = defence
        Item.__init__(self, name, nameish, description, weight, cost, image)
        self.enchantments = enchantments
        self.type = "Leggins"

class Boots(Item):

    def __init__(self, name, nameish, description, defence, weight, cost, image, enchantments=[]):
        self.defence = defence
        Item.__init__(self, name, nameish, description, weight, cost, image)
        self.enchantments = enchantments
        self.type = "Boots"

class Weapon(Item):

    def __init__(self, name, nameish, description, damage, weight, cost, image, enchantments=[]):
        self.damage = damage
        Item.__init__(self, name, nameish, description, weight, cost, image)
        self.enchantments = enchantments
        self.type = "Weapon"

class Money(Item):

    def __init__(self, name, nameish, description, amount, weight, cost, image):
        self.amount = amount
        Item.__init__(self, name, nameish, description, weight, cost, image)
        self.type = "Money"

class Book(Item):

    def __init__(self, name, nameish, description, knowlege, weight, cost, image, contents):
        self.knowlege = knowlege
        self.contents = contents
        Item.__init__(self, name, nameish, description, weight, cost, image)
        self.type = "Book"

class Map(Item):

    def __init__(self, name, nameish, description, weight, cost, image, mapcontents):
        self.map = mapcontents
        Item.__init__(self, name, nameish, description, weight, cost, image)
        self.type = "Map"

class NPC():

    def __init__(self, name, description, attack, defence, health, maxhealth, level, alignment, speed, luck, magic, spells=[], inventory=[]):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health
        self.maxhealth = maxhealth
        self.level = level
        self.alignment = alignment
        self.speed = speed
        self.luck = luck
        self.magic = magic
        self.spells = spells
        self.inventory = inventory
        self.cat = "NPC"

class Person(NPC):

    def __init__(self, name, description,  attack, defence, health, maxhealth, level, alignment, speed, luck, magic, spells=[], inventory=[], conversation=[]):
        self.conversation = conversation
        NPC.__init__(self, name, description,  attack, defence, health, maxhealth, level, alignment, speed, luck, magic, spells, inventory)
        self.type = "Person"
