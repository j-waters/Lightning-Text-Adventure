#####
#Chapter One of the main Legend Of Aiopa game
#####

#####
#Import the Core modules
from lightCore import *  # @UnusedWildImport
from adventureCore import *  # @UnusedWildImport
#Import Variable Modules
import player, world, inventory  # @Reimport


def firstLoad():
    inventory.load()
    if player.load() == False:
        debug("#Player#")
        create_character()
        player.Health = player.MaxHealth
    if world.load() == False:
        debug("#World#")
        TN1_R1()


def create_character():
    debug("#Character#")
    player_picture()
    player_name()


def TN1_R1():
    debug("#TN1_R1#")
    world.Location = "TN1_R1"
    choices(world.Places[world.Location])

#try:
debug("BEGIN")
firstLoad()

#except:
    #t = time.strftime("%d %b %Y %H.%M.%S", time.gmtime())
    #erf = open("Crash Reports/Error Report at " + t + ".txt", "w")
    #erf.write("\n" + "=" * 20)
    #erf.write("\nCrash At " + t)
    #erf.write("\n")
    #traceback.print_exc(file=erf)
    #erf.close()
    #easygui.exceptionbox(msg="The Legend Of Aiopa Has Crashed.", title="Crash Report")