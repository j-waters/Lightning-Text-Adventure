from lightCore import debug, print
from lightCore import easygui as eg
from Classes import *

def begin():
    global places
    global locationData
    places = {"TN1_R1": ['Weapon("Sword", "Swords", "A standard shortsword", "3", "1", "10", "Rdagger.png")', 'Money("Some Coins", "", "A small pouch of money", 5, "1", "1", "")', 'Person("Bob", "An Old Man",  3, 2, 10, 10, 1, "Good", 1, 5, 1)']}
    locationData = {}
    editWorld()

def editWorld():
    while True:
        options = []
        options.extend(places.keys())
        options.append("<Add Room>")
        decision = eg.choicebox(msg="Select an item to edit:", choices=options)

        if decision == "<Add Room>":
            rname = eg.enterbox(msg="Enter Room Name:")
            places[rname] = []
        else:
            editRoom(decision)


def editRoom(room):
    options = []
    options.append("Edit Location Data")
    options.append("Edit Items")

    decision = eg.buttonbox(msg="Select what to edit about " + room, choices=options)

    if decision == "Edit Items":
        room = places[room]
        options = []
        for item in room:
            name = item.split(',')[0]
            name = name.replace("(", " - ")
            name = name.replace('"', "")
            options.append(name)
        options.append("<New Item>")
        decision = eg.choicebox(msg="Select an item to edit:", choices=options)
        if decision == "<New Item>":
            editItem()
        else:
            for item in room:
                name = item.split(',')[0]
                name = name.replace("(", " - ")
                name = name.replace('"', "")
                if name == decision:
                    item = item
                    break
            editItem(item)


def editItem(item=None):
    if item == None:
        exists = False
        itemTypes = ["Weapon",
                     "Shirt",
                     "Leggins",
                     "Helmet",
                     "Boots"
                     ]
        type = eg.choicebox(msg="Select Item Type:", choices=itemTypes)
    else:
        exists = True
        debug(item)
        item = eval(item)
        debug(item)
        type = item.type

    if type == "Weapon":
        f = ["name", "nameish", "damage", "weight", "cost", "image"]
        v = []
        if exists:
            for key in f:
                v.append(item.__dict__[key])
        edit = eg.multenterbox(msg="Edit Item:", fields=f, values=v)
        for i in range(0, 5):
            item.__dict__[f[i]] = edit[i]

begin()