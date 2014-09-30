import sys
from urllib.request import urlretrieve

#####
#Light-Core, by Lightning3105
#Contains Several important functions
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
