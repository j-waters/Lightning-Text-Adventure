from lightcore import *


class Item():

    def __init__(self, name, nameish, description, weight, cost, image):
        self.weight = weight
        self.cost = cost

class Equiped(): #TODO: finish

    def __init__(self, name, description, defence, weight, cost, image, enchantments=[]):


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

    def __init__(self, name, nameish, description, knowlege, weight, cost, image, book):
        self.knowlege = knowlege
        self.book = book
        Item.__init__(self, name, nameish, description, weight, cost, image)
        self.type = "Book"

class Map(Item):

    def __init__(self, name, nameish, description, weight, cost, image, mapcontents):
        self.map = mapcontents
        Item.__init__(self, name, nameish, description, weight, cost, image)
        self.type = "Map"

class NPC():

    def __init__(self, name, description, attack, defense, health, maxhealth, level, alignment, speed, luck, mana, maxmana, spells=[], inventory=[]):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
        self.maxhealth = maxhealth
        self.level = level
        self.alignment = alignment
        self.speed = speed
        self.luck = luck
        self.mana = mana
        self.maxmana = maxmana
        self.spells = spells
        self.inventory = inventory

class Person(NPC):

    def __init__(self, name, description,  attack, defense, health, maxhealth, level, alignment, speed, luck, magic, spells=[], inventory=[], conversation=[]):
        self.conversation = conversation
        NPC.__init__(self, name, description,  attack, defense, health, maxhealth, level, alignment, speed, luck, magic, spells, inventory)
        self.type = "Person"
