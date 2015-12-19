import os
from typing import List
def listDirectory (path=None, showHidden=False) -> List[str]:
    if path == None:
        path = "./" #current directory.

    dirs = os.listdir(path)
    if not showHidden:
        dirs = list (filter (lambda f : f[0] != '.', dirs))

    return dirs

def move(filename, moveTo):
    os.system("mv -b \"%s\" \"%s\" &" % (filename, os.path.join(moveTo, filename)))

def getTVShowNames (path="/media/HDD/TV") -> List[str]:
    if not os.path.exists (path):
        raise Exception ("Error, TV Paths does not exist!")

    shows = os.listdir(path)
    shows.sort()
    return shows
