from os.path import isdir
from os import mkdir
from pickle import dump,load
from shutil import rmtree

"""
Functions for necessary file operations pertaining to the NDimPoint(Scriptor|Descriptor)
classes.
"""

def create_dirpath(dirPath):

    def find_slash(dp):
        indices = []
        s = 0
        l = len(dp)
        while s < l:
            i = dp[s:].find("/")
            if i == -1: break
            s = s + i
            indices.append(s)
            s += 1
        return indices

    if dirPath in ["","/"]: return

    assert " " not in dirPath and "." not in dirPath, "invalid dir. path 1"
    assert dirPath[0] != "/", "invalid dir. path 2"

    folders = find_slash(dirPath)
    while len(folders) > 0:
        i = folders.pop(0)
        dp = dirPath[:i]
        if not isdir(dp):
            # make directory
            mkdir(dp)

    if not isdir(dirPath):
        mkdir(dirPath)

def delete_dirpath(dp):
    assert dp not in ["", "/"], "permission denied"

    try:
        rmtree(dp, ignore_errors=True)
    except:
        pass

def pickle_obj_to_file(obj,fp):
    # case: fp is folder, create directory path
    if "/" in fp:
        q = fp[::-1]
        r = q.find("/")
        q = q[r + 1:]
        q = q[::-1]
        print("dir is: ",q)
        create_dirpath(q)

    fobj = open(fp,"wb")
    dump(obj,fobj)
    fobj.close()

def pickle_obj_from_file(fp):
    fobj = open(fp,"rb")
    obj = load(fobj)
    fobj.close()
    return obj
