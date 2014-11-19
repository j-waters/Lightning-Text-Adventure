
import sys  # @UnusedImport
from urllib.request import urlretrieve

#####
#Light-Core, by Lightning3105
#Contains Several important functions
#####

#####
#All Module Imports
#####
#General Modules
import time #@UnusedImport
import random #@UnusedImport
import easygui #@UnresolvedImport @UnusedImport
import sys #@UnusedImport @Reimport
import atexit #@UnusedImport
import ast #@UnusedImport
import os.path #@UnusedImport
import traceback #@UnusedImport
from functools import reduce #@UnusedImport
#####
#End Module Imports
#####

def debug(string):
    #Normal print function, outputting to the console
    if string == None:
        string = "*None*"
    sys.stdout.write(str(string))
    sys.stdout.write("\n")

def reporthook(blocknum, blocksize, totalsize):
    #Shows percentage of download
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize: # near the end
            sys.stderr.write("\n")
    else: # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))

def download(url, name):
    #Downloads a file from a URL, with a name
    debug("Begin Download")
    urlretrieve(url, name, reporthook)

def run(func):
    #Runs a function by name, 'func'
    globals()[func]()

def t(L, N):
    # get Nth item in tuple in list of tuples
    #eg: L = [('a','1'),('b','2'),('c','3')]
    #    N = 0
    #    returned ['a','b','c']
    return [x[N] for x in L]

def print(string, title=None):  # @DontTrace @ReservedAssignment
    #easygui print
    easygui.msgbox(msg=string, title=title)

def pprint(pic, string, title=None):
    #easygui picture print
    easygui.msgbox(image=pic, msg=string, title=title)

def importVar(m):
    #Imports a function by name, m
    m = __import__(m)

def get_save(filename):
    result = {}
    with open(filename) as f:
        for line in f:
            try:
                line = line.split(' = ',1)
                result[line[0]] = ast.literal_eval(line[1].strip())
            except:
                pass
    return result

def printTree(tree, depth = 0):
    if tree == None or len(tree) == 0:
        debug ("\t" * depth + "-")
    elif type(tree) == str:
        debug ("\t" * depth + tree)
    elif type(tree) == list:
        debug ("\t" * depth + str(tree))
    else:
        for key, val in tree.items():
            debug ("\t" * depth + key)
            printTree(val, depth+1)

class Error(Exception):
    pass