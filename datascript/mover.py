import glob
from os import path
import subprocess
from utils import load_json, save_json

def get_extravoice_path(basename):
    splitname = basename.split("_")
    base = splitname[-2]
    brand = splitname[-1].split("#")[0]
    targetname = base + "-" + brand

    return targetname

def move_chardata():
    charpaths = glob.glob("chardata/*.json")
    for charpath in charpaths:
        targetname = path.basename(charpath).split("_")[-1]

        if "#" in targetname:
            # Ending in 1 is either e2, or Chongyue's special outfit
            if (targetname.split("#")[-1] == "1.json") and (path.basename(charpath).split("_")[-2] != "chyue"):
                targetname = targetname.split("#")[0] + "-e2.json"
            else:
                targetname = get_extravoice_path(path.basename(charpath)) \
                    + ".json"

        targetpath = path.join("..", "site", "static", 
            "data", "chardata", targetname)
        data = load_json(charpath)
        save_json(data, targetpath, False)

        print("Succesfully moved", targetname)

    print("Succesfully moved all chardata")

def move_charlist():
    charlist = load_json("charlist.json")

    save_json(charlist, path.join("..", "site", "static", 
            "data", "charlist.json"), False)
    print("Character list moved!")

def ffmpeg_convert(sourcefile, targetfile, skipoverwrite = False):
    if (skipoverwrite):
        subprocess.run(f"ffmpeg -i {sourcefile} {targetfile} -quality 90 -n")
    else:
        subprocess.run(f"ffmpeg -i {sourcefile} {targetfile} -quality 90")

def move_avatars():
    avapaths = glob.glob("images/avatars3/*.png")
    for avapath in avapaths:
        targetname = path.basename(avapath).split("_")[-1]

        if "#" in targetname:
            targetname = get_extravoice_path(path.basename(avapath))

        targetname = path.splitext(targetname)[0] + ".webp"
        targetpath = path.join("..", "site", "static", 
            "images", "avatars", targetname)

        if path.isfile(targetpath):
            print(targetname, "already exists, skipping...")
        else:
            ffmpeg_convert(avapath, targetpath, True)

            print("Succesfully moved", targetname)

def move_factions():
    factionpaths = glob.glob("images/factions/*.png") 
    for factionpath in factionpaths:
        targetname = path.basename(factionpath).split("_")[-1]
        targetname = path.splitext(targetname)[0] + ".webp"
        targetpath = path.join("..", "site", "static", 
            "images", "factions", targetname)
        ffmpeg_convert(factionpath, targetpath, True)

        print("Succesfully moved", targetname)

if __name__ == "__main__":  
    move_charlist()
    move_chardata()
    move_avatars()