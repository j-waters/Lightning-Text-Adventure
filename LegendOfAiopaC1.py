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


def create_character():
    player_picture()
    player_name()

firstLoad()