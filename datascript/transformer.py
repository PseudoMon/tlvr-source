import json
from os import path
from utils import save_json, load_json

langs = ["en", "jp", "kr", "cn"] 
mute_chars = ["rguard", "rdfend", "rsnipe", "rmedic", "rcast", "aprot"]

def rarity_str_to_int(raritystr):
	# Transform rarity data from e.g. TIER_6 to 6 as an integer
	return int(raritystr.split("_")[-1])

def loadchardict(region):
	sourcepath = path.join(region, "chardict.json")
	return load_json(sourcepath)

def load_wordtable(region):
	sourcepath = path.join(region, "charword_table.json")
	return load_json(sourcepath)

def load_chartable(region):
	sourcepath = path.join(region, "character_table.json")
	return load_json(sourcepath)

def loadchardicts(regions):
	dicts = {}
	for region in regions:
		dicts[region] = loadchardict(region)
	return dicts

def load_chartables(regions):
	dicts = {}
	for region in regions:
		dicts[region] = load_chartable(region)
	return dicts

def make_charlist(check_nation=True):
	chardicts = loadchardicts(langs)
	chartable = load_chartable("en")
	
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

		fulldata = chartable[f"char_{newchar['numberid']}_{char}"]
		newchar["nation"] = fulldata["nationId"]
		rarity = rarity_str_to_int(fulldata["rarity"])
		newchar["rating"] = rarity

		charlist.append(newchar)

	return charlist

def make_and_save_charlist():
	charlist = make_charlist()
	print("Loaded {} characters".format(len(charlist)))
	save_json(charlist, "charlist.json")

def load_wordtables():
	tables = {}
	for lang in langs:
		tables[lang] = load_wordtable(lang)
		print(f"Word table for {lang} loaded")
		
	print("Word tables loaded.")

	return tables

def get_welcome():
	tables = load_wordtables()

	key = "char_002_amiya_CN_042"
	result = {}
	for lang in langs:
		voice_data = table[lang]["charWords"][key]
		result[lang] = voice_data["voiceText"]

	print("Texts in key found. Now saving...")
	save_json(result, "welcome.json")

def get_voices(wordkey, wordtables):
	# Use EN as base
	basetable = wordtables["en"]

	voices = []

	for wordid in basetable["charWords"]:
		basedata = basetable["charWords"][wordid]
		if basedata["wordKey"] != wordkey:
			continue

		voiceText = basedata["voiceText"].replace(" ", " ")
		voicedata = {
			"id": wordid,
			"title": {"en": basedata["voiceTitle"]},
			"text": {"en": basedata["voiceText"].replace(" ", " ")},
			"asset": basedata["voiceAsset"],
		}

		for lang in langs:
			if lang == "en":
				# Skip en
				continue

			langbasedata = wordtables[lang]["charWords"][wordid]
			voicedata["title"][lang] = langbasedata["voiceTitle"]
			voicedata["text"][lang] = langbasedata["voiceText"]

		voices.append(voicedata)

	return voices

def get_actors_from_voicedict(voicedict):
	# Might add other voice languages later
	lang_mapping = {
		"en": "EN",
		"cn" :"CN_MANDARIN",
		"jp": "JP",
		"kr": "KR",
		"linkage": "LINKAGE",
		"ita": "ITA",
		"cn_topolect": "CN_TOPOLECT"
	}

	actors = {}
	for lang in lang_mapping:
		try:
			actordata = voicedict[lang_mapping[lang]]
			actors[lang] = actordata["cvName"][0]
		except KeyError:
			# No actor data for this language
			print(f"No actor found for language {lang}")
			pass

	return actors

def get_actors(charid, wordtables):
	print("Checking voice actor name for", charid)
	# JP use the native spelling of the name
	# EN use English preferred name or transliteration
	# CN use CN names even for Korean and Japanese names with kana
	# So we use JP as base
	basetable = wordtables["jp"]
	voidedict = basetable["voiceLangDict"][charid]["dict"]
	native_names = get_actors_from_voicedict(voidedict)

	# Add EN names as they're often the global preferred name
	entable = wordtables["en"]
	envoicedict = entable["voiceLangDict"][charid]["dict"]
	global_names = get_actors_from_voicedict(envoicedict)

	actors = {}
	for lang in native_names:
		actors[lang] = {}
		actors[lang]["native"] = native_names[lang]
		actors[lang]["global"] = global_names[lang]

	return actors

def get_voice_availability(charid, wordtables):
	print ("Checking voice availability for", charid)
	# Check which languages this character has voice of
	# Use EN since that's what our data is based on

	table = wordtables["en"]
	voicedict = table["voiceLangDict"][charid]["dict"]
	cn_names = get_actors_from_voicedict(voicedict)
	# technically the name itself is not needed
	# but im too lazy to make another function

	availability = []
	for lang in cn_names:
		availability.append(lang)

	print("Availability found with langs:", availability)
	return availability

def get_and_write_chardata(charid, wordtables, names={}):
	voices = get_voices(charid, wordtables)
	actors = get_actors(charid, wordtables)
	availability = get_voice_availability(charid, wordtables)

	chardata = {
		"charid": charid,
		"nameid": charid.split("_")[-1],
		"names": names,
		"voices": voices,
		"actors": actors,
		"availability": availability,
	}

	save_json(chardata, f"chardata/{charid}.json")
	print(f"Written chardata for {charid}")

def process_all_characters():
	charlist = load_json("charlist.json")
	wordtables = load_wordtables()
	for char in charlist:
		charid = f"char_{char['numberid']}_{char['nameid']}"
		get_and_write_chardata(charid, wordtables, char["name"])

def get_and_save_misc_data(charlist):
	nations = []
	for char in charlist:
		if char["nation"] not in nations:
			nations.append(char["nation"])

	miscdata = { "nations": nations }

	save_json(miscdata, "miscdata.json")
	print("Created misc data file")

if __name__ == "__main__":  
	# charlist = load_json("charlist.json")
	# test_chars = ["indigo", "texas", "lmlee", "jnight", 
	# 	"lolxh", "ncdeer", "aprot2"]
	# chars = [char for char in charlist if char["nameid"] in test_chars]

	# chartable = load_chartable("en")
	# factions = []
	# for charid in chartable:
	# 	chardata = chartable[charid]
	# 	faction = chardata["nationId"]
	# 	if faction not in factions:
	# 		factions.append(faction)

	# nonationfactions = ["rainbow", "babel", "followers"]
	# nations = ['rhodes', 'kazimierz', 'columbia', None, 
	# 	'laterano', 'victoria', 'sami', 'bolivar', 'iberia', 
	# 	'siracusa', 'higashi', 'sargon', 'kjerag', 'minos', 'yan', 
	# 	'lungmen', 'ursus', 'egir', 'leithanien', 'rim']

	# print(factions)

	make_and_save_charlist()

	charlist = load_json("charlist.json")
	get_and_save_misc_data(charlist)

	process_all_characters()