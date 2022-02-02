import os
import sys
import time
print ("Current Directory is:", os.getcwd())
cont = input("Organize Flac files in current directory (Y)es, (N)o\n")
path =  os.getcwd()
if cont in ["Y", "y", "Yes", "yes"]:
    separator = input("Input separator for Artist/Album/Song \nOnly supports a single type of separator\n")
    files = os.listdir(path)
    for origName in files:
        if origName.endswith('.flac'):
            artistName = origName.split(separator,3)[0]
            albumName = origName.split(separator,3)[1]
            trackNumber = origName.split(separator,3)[2]
            songName = origName.split(separator,3)[3]
            if not os.path.exists(artistName):
                os.makedirs(artistName)
            if not os.path.exists(artistName +"\\"+albumName):
                os.makedirs(artistName +"\\"+albumName)
            newName = albumName +"_"+ trackNumber +"_"+ songName
            os.rename(origName, artistName + "\\" + albumName + "\\" + newName)
        else:
            print("Skipping: " + origName)
            pass
else:
    quit()
