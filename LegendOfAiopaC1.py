#####
#Chapter One of the main Legend Of Aiopa game
#####

#####
#Import the Core modules
from lightCore import *  # @UnusedWildImport
from adventureCore import *  # @UnusedWildImport
#Import Variable Modules
import player, world, inventory



def firstLoad():
    if player.load() == False:
        create_character()
    if world.load() == False:
        TN1_R1()


def create_character():
    player_picture()
    player_name()


def TN1_R1():
    options()







firstLoad()

