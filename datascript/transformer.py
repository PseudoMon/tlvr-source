import json
from os import path
import grabfiles

langs = ["en", "jp", "kr", "cn"] 
mute_chars = ["rguard", "rdfend" "rsnipe", "rmedic", "rcast"]

def save_json(data, target):
	with open(target, "w", encoding="utf-8") as targetfile:
		json.dump(data, targetfile, ensure_ascii=False, indent=4)

def load_json(source):
	with open(source, "r", encoding="utf-8") as sourcefile:
		data = json.load(sourcefile)
	return data 

def loadchardict(region):
	sourcepath = path.join(region, "chardict.json")
	return load_json(sourcepath)

def load_wordtable(region):
	sourcepath = path.join(region, "charword_table.json")
	return load_json(sourcepath)

def loadchardicts(regions):
	dicts = {}
	for region in regions:
		dicts[region] = loadchardict(region)
	return dicts

def make_charlist():
	chardicts = loadchardicts(langs)
	charlist = []

	# Use EN as base
	for char in chardicts["en"]:
		if char in mute_chars:
			print("Found mute char", char)
			continue

		newchar = {
			"nameid": char,
			"numberid": chardicts["en"][char]["id"],
			"name": {
				"en": chardicts["en"][char]["name"],
			}
		}

		for lang in langs:
			if lang == "en":
				continue

			regional_name = chardicts[lang][char]["name"]
			newchar["name"][lang] = regional_name

		charlist.append(newchar)

	return charlist

def make_and_save_charlist():
	charlist = make_charlist()
	print("Loaded {} characters".format(len(charlist)))
	save_json(charlist, "charlist.json")

def download_avatars():
	# We've downloaded up to the 149th btw
	charlist = load_json("charlist.json")
	count = 0
	for char in charlist:
		count += 1

		if count > 100:
			numberid = char["numberid"] 
			nameid = char["nameid"]
			print(f"{numberid}_{nameid}")

			grabfiles.grab_avatar(char)

		if count > 150:
			break

def grab_welcome():
	table = {}
	for lang in langs:
		table[lang] = load_wordtable(lang)
		print(f"Word table for {lang} loaded")
		
	print("Word tables loaded.")

	key = "char_002_amiya_CN_042"
	result = {}
	for lang in langs:
		voice_data = table[lang]["charWords"][key]
		result[lang] = voice_data["voiceText"]

	print("Texts in key found. Now saving...")
	save_json(result, "welcome.json")

grab_welcome()
