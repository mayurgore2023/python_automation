
# Application to find out duplicate file and return their name from directory:

from sys import*
import os
import hashlib


def hashfile(path,blocksize=1024):
    afile=open(path,"rb")
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayChecksum(path):
    flag = os.path.isabs(path)
    if flag == False
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName,Subdirs,fileList in os.walk(path):
            print("Current folder is"+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
        print("Error:invalid number of arguments")
        exit()
        print(path)
        print(file_hash)
        


def main():
    print("------Marvellous Infosystem-----------")

    print("Application name:"+argv[0])

    if(len(argv) != 2):
        print("Error:Invalid number of arguments")
        exit()

    if(argv[1] == "-h")or(argv[1] == "-H"):
        print("This script use to traverse specific directory and display name of duplicate files")
        exit()

    if(argv[1] == "-u")or(argv[1] == "-H"):
        print("usage:Aapplication Name AbsolutePath_of_Directory Extention")
        exit()

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr)

    except ValueError:
        print("Error: Invalid datatype of input")

    #except Exception:
        #cdprint("Error:Invalid input")


if __name__=="__main__":
    main()
