import glob
from os import path
import subprocess
from utils import load_json, save_json

def move_chardata():
    charpaths = glob.glob("chardata/*.json")
    for charpath in charpaths:
        targetname = path.basename(charpath).split("_")[-1]
        targetpath = path.join("..", "site", "static", 
            "data", "chardata", targetname)
        data = load_json(charpath)
        save_json(data, targetpath, False)

        print("Succesfully moved", targetname)

    print("Succesfully moved all chardata")

def move_charlist():
    charlist = load_json("charlist.json")
    # Some selections for testing
    # chosens = ["indigo", "texas", "lmlee", "jnight", 
    # "lolxh", "ncdeer", "aprot2"]
    #charlist = [char for char in charlist if char["nameid"] in chosens]

    save_json(charlist, path.join("..", "site", "static", 
            "data", "charlist.json"), False)
    print("Character list moved!")

def ffmpeg_convert(sourcefile, targetfile, skipoverwrite = False):
    if (skipoverwrite):
        subprocess.run(f"ffmpeg -i {sourcefile} {targetfile} -quality 90 -n")
    else:
        subprocess.run(f"ffmpeg -i {sourcefile} {targetfile} -quality 90")

def move_avatars():
    avapaths = glob.glob("images/avatars/*.png")
    for avapath in avapaths:
        targetname = path.basename(avapath).split("_")[-1]
        targetname = path.splitext(targetname)[0] + ".webp"
        targetpath = path.join("..", "site", "static", 
            "images", "avatars", targetname)
        ffmpeg_convert(avapath, targetpath)

        print("Succesfully moved", targetname)

if __name__ == "__main__":  
    move_chardata()