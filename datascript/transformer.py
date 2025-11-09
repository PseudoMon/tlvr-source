import json
from os import path
from utils import save_json, load_json

langs = ["en", "jp", "kr", "cn"] 
mute_chars = ["rguard", "rdfend", "rsnipe", "rmedic", "rcast", "aprot", 
	"ccast", "csnipe", "cpione", "cguard", "cspec", "cmedic", "cdfend", "csuppo",
	"acnipe", "acpion", "accast", "acsupo", "acspec", "acmedc", "acfend", "acguad"]

def rarity_str_to_int(raritystr):
	# Transform rarity data from e.g. TIER_6 to 6 as an integer
	return int(raritystr.split("_")[-1])

def load_wordtable(region):
	sourcepath = path.join(region, "charword_table.json")
	return load_json(sourcepath)

def load_chartable(region):
	sourcepath = path.join(region, "character_table.json")
	return load_json(sourcepath)

def load_chartables(regions):
	dicts = {}
	for region in regions:
		dicts[region] = load_chartable(region)
	return dicts

def make_charlist_v2():
	chartable = load_chartable("en")
	characters = []
	
	for charid in chartable:
		if charid.split("_")[0] != "char":
			continue
		print(chartable[charid]["name"])
		
	for charid in chartable:
		if charid.split("_")[0] != "char":
			continue

		splitname = charid.split("_")
		characters.append({
			"name": chartable[charid]["name"],
			"nameid": splitname[-1],
			"numberid": splitname[1],
		})

	save_json(characters, "text.json")


def make_charlist():
	chartables = load_chartables(langs)
	
	charlist = []

	# Use EN as base
	for charid in chartables["en"]:
		splitid = charid.split("_")

		if splitid[0] != "char":
			continue

		charname = splitid[-1]

		if charname in mute_chars:
			print("Found mute char", charname)
			continue

		newchar = {
			"fullid": charid,
			"nameid": charname,
			"numberid": splitid[1],
			"name": { }
		}

		for lang in langs:
			regional_name = chartables[lang][charid]["name"]
			newchar["name"][lang] = regional_name

		# Set additional data
		fulldata = chartables["en"][charid] # just use en as base
		newchar["nation"] = fulldata["nationId"]
		rarity = rarity_str_to_int(fulldata["rarity"])
		newchar["rating"] = rarity

		charlist.append(newchar)

		if charid == "char_002_amiya":
			amiya_alter1, amiya_alter2 = make_amiya_alters_data(newchar)
			charlist.append(amiya_alter1)
			charlist.append(amiya_alter2)

	return charlist

def make_amiya_alters_data(base_amiya):
	amiya_alter1 = base_amiya.copy()
	amiya_alter2 = base_amiya.copy()

	amiya_alter1["name"] = base_amiya["name"].copy()
	for lang in amiya_alter1["name"]:
		amiya_alter1["name"][lang] = base_amiya["name"][lang] + " 2"

	amiya_alter2["name"] = base_amiya["name"].copy()
	for lang in amiya_alter2["name"]:
		amiya_alter2["name"][lang] = base_amiya["name"][lang] + " 3"

	amiya_alter1["fullid"] = "char_1001_amiya2"
	amiya_alter2["fullid"] = "char_1037_amiya3"

	amiya_alter1["nameid"] = "amiya2"
	amiya_alter2["nameid"] = "amiya3"

	amiya_alter1["numberid"] = "1001"
	amiya_alter2["numberid"] = "1037"

	return (amiya_alter1, amiya_alter2)

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

			try:
				langbasedata = wordtables[lang]["charWords"][wordid]
			except KeyError:
				print(f"Error getting voice in {lang} for {wordid}")
			else:
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
		"cn_topolect": "CN_TOPOLECT",
		"ger": "GER",
		"rus": "RUS",
		"fre": "FRE",
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
	try:
		voidedict = basetable["voiceLangDict"][charid]["dict"]
	except KeyError:
		# When there are no voice data associated yet
		return {}
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
	try:
		voicedict = table["voiceLangDict"][charid]["dict"]
	except KeyError:
		# When there are no voice data associated yet
		voicedict = {}
	cn_names = get_actors_from_voicedict(voicedict)
	# technically the name itself is not needed
	# but im too lazy to make another function

	availability = []
	for lang in cn_names:
		availability.append(lang)

	print("Availability found with langs:", availability)
	return availability

def get_chardata(charid, wordtables, names={}):
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

	add_old_voices(chardata)

	return chardata

def add_old_voices(chardata):
	manualdata = load_json("manual.json")

	try:
		old_voice_data = manualdata["oldvoices"][chardata["nameid"]]
	except KeyError:
		return
	
	print(f"Adding old voice to {chardata['nameid']}")
	newkey = "old_" + old_voice_data["lang"]
	chardata["actors"][newkey] = old_voice_data["actor"]
	chardata["availability"].append(newkey)

	try:
		chardata["audio_path_override"][newkey] = old_voice_data["baseurl"]
	except KeyError:
		chardata["audio_path_override"] = {}
		chardata["audio_path_override"][newkey] = old_voice_data["baseurl"]

	return

def get_and_write_chardata(charid, wordtables, names={}):
	chardata = get_chardata(charid, wordtables, names)

	save_json(chardata, f"chardata/{charid}.json")
	print(f"Written chardata for {charid}")

def process_all_characters(charlist, wordtables):
	for char in charlist:
		charid = f"char_{char['numberid']}_{char['nameid']}"
		get_and_write_chardata(charid, wordtables, char["name"])

	return wordtables

def get_and_save_misc_data(charlist):
	nations = []
	for char in charlist:
		if char["nation"] not in nations:
			nations.append(char["nation"])

	miscdata = { "nations": nations }

	save_json(miscdata, "miscdata.json")
	print("Created misc data file")

def shit():
	print("Hello")

def run_transformer():
	make_and_save_charlist()

	charlist = load_json("charlist.json")
	wordtables = load_wordtables()

	get_and_save_misc_data(charlist)
	process_all_characters(charlist, wordtables)

	return charlist, wordtables

if __name__ == "__main__":
	chardata = load_json("chardata/char_103_angel.json")
	add_old_voices(chardata)
	print(chardata["availability"])