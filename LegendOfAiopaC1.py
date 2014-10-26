#####
#Chapter One of the main Legend Of Aiopa game
#####

#####
#Import the Core modules
from lightCore import *  # @UnusedWildImport
from adventureCore import *  # @UnusedWildImport
#Import Variable Modules
import player, world, inventory
import ConversationTreeMaker


def firstLoad():
    inventory.load()
    if player.load() == False:
        create_character()
    if world.load() == False:
        TN1_R1()



def create_character():
    player_picture()
    player_name()


def TN1_R1():
    choices(world.TN1_R1)

#firstLoad()

world.load()
dic = world.TN1_R1[6][3]
ConversationTreeMaker.printTree(dic)