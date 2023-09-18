import glob
from os import path
from utils import load_json, save_json

charpaths = glob.glob("chardata/*.json")
for charpath in charpaths:
	targetname = path.basename(charpath).split("_")[-1]
	targetpath = path.join("..", "site", "static", 
		"data", "chardata", targetname)
	data = load_json(charpath)
	save_json(data, targetpath, False)

	print("Succesfully moved", targetname)
