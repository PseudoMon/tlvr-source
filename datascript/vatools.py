from os import path
from utils import save_json, load_json
import glob

langs = ["en", "cn", "jp", "kr"]

def get_all_vadata():
	all_datafiles = glob.glob("chardata/*.json")
	vadata = {}
	vadata["en"] = {}
	vadata["jp"] = {}
	vadata["kr"] = {}
	vadata["cn"] = {}

	for charafile in all_datafiles:
		charadata = load_json(charafile)
		for lang in langs:
			try:
				actor_name = charadata["actors"][lang]["global"]
			except KeyError:
				# Probably no voice actor in that language
				continue

			if actor_name in vadata[lang]:
				vadata[lang][actor_name].append(charadata["nameid"])
			else:
				vadata[lang][actor_name] = [charadata["nameid"]]

	return vadata

def get_all_vadata_perchar():
	all_datafiles = glob.glob("chardata/*.json")
	allchars = []

	for charafile in all_datafiles:
		charadata = load_json(charafile)
		combo = {
			"nameid": charadata["nameid"], 
			"names": charadata["names"],
			"actors": charadata["actors"],
		}
		print(combo)
		allchars.append(combo)

	return allchars

def weed_out_nonmulti(vadata):
	# Take out everyone who's only voiced one character
	final_vadata = {}

	for lang in langs:
		dataholder = {}

		for actor_name in vadata[lang]:
			charas = vadata[lang][actor_name]
			if len(charas) > 1:
				dataholder[actor_name] = charas 

		final_vadata[lang] = dataholder 

	return final_vadata

def get_and_save_vadata(nomulti = False):
	if nomulti:
		vadata = weed_out_nonmulti(get_all_vadata())
	else:
		vadata = get_all_vadata()
	save_json(vadata, "vadata.json")
	print("Saved data to vadata.json")

def get_shared_va(vadata, nameid):
	shared_va = {}

	for lang in langs:
		for actor_name in vadata[lang]:
			charas = vadata[lang][actor_name]
			if nameid in charas:
				shared_va[lang] = [chara for chara in charas if chara != nameid]
				break

	return shared_va

if __name__ == "__main__":  
	#get_and_save_vadata()
	save_json(get_all_vadata_perchar(), "vadata-alt.json")
