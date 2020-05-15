import os
import sys
import time

print ("Current Directory is:", os.getcwd())
cont = input("Organize Files in current directory (Y)es, (N)o\n")
path =  os.getcwd()
if cont in ["Y", "y", "Yes", "yes"]:
    files = os.listdir(path)
    for origName in files:
        if origName.endswith('.flac'):
            artistName = origName.split("_-_",3)[0]
            albumName = origName.split("_-_",3)[1]
            trackNumber = origName.split("_-_",3)[2]
            songName = origName.split("_-_",3)[3]
            if not os.path.exists(artistName):
                os.makedirs(artistName)
            if not os.path.exists(artistName +"\\"+albumName):
                os.makedirs(artistName +"\\"+albumName)
            os.rename(origName, artistName + "\\" + albumName + "\\" + albumName + trackNumber + songName)
        else:
            print("Skipping: " + origName)
            pass
else:
    quit()
