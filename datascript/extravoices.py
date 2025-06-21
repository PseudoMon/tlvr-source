from os import path
from utils import load_json, save_json
from transformer import load_wordtables, get_voices, get_chardata

def grab_unique_voices_ids(charlist, wordtables):
    unique_voices = []
    unique_voices_data = []

    basetable = wordtables["en"]

    for char in charlist:
        charid = f'char_{char["numberid"]}_{char["nameid"]}'

        for wordid in basetable["charWords"]:
            basedata = basetable["charWords"][wordid]

            if basedata["charId"] != charid:
                # Not the character we're looking for
                continue

            if not "#" in basedata["wordKey"]:
                # Most likely normal voiceline handled elsewhere
                continue

            #voices = get_voices(basedata["wordKey"], wordtables)

            extrachardata = {
                "oldid": charid,
                "names": char["name"],
                "newid": basedata["wordKey"]
            }

            if not (basedata["wordKey"] in unique_voices):
                unique_voices.append(basedata["wordKey"])
                unique_voices_data.append(extrachardata)

    return unique_voices_data

def get_new_names(oldnames, newid):
    newname_split = newid.split("_")
    extraid = newid.split("#")[-1]

    newnames = {}

    if extraid == "1" and oldnames["en"] != "Chongyue":
        nameaddon = "E2"
        # it's xiaohei or mudrock

    elif len(newname_split) < 4:
        print("Found unique voice that's not common addon but no identifier!")

    else:
        nameaddon = newname_split[-1].split("#")[0].upper()

    for lang in oldnames:
        newnames[lang] = oldnames[lang] + " " + nameaddon

    return (newnames, nameaddon.lower())


def get_char_index(charlist, charnameid):
    for idx, char in enumerate(charlist):
        if char["nameid"] == charnameid:
            return idx

    return -1

def create_and_fill_in_extra_voices(charlist, wordtables):
    uniques = grab_unique_voices_ids(charlist, wordtables)

    for newchar in uniques:
        newnames, nameaddon =  get_new_names(newchar["names"], newchar["newid"])
        chardata = get_chardata(newchar["newid"], wordtables, newnames)

        oldid = newchar["oldid"].split("_")[-1]
        newid = oldid + "-" + nameaddon

        chardata["nameid"] = newid
        save_json(chardata, f"chardata/{newchar['newid']}.json")
        print(f"Written chardata for {newchar['newid']}")

        oldindex = get_char_index(charlist, oldid)
        newindex = get_char_index(charlist, newid)

        if oldindex >= 0 and newindex < 0:
            # Old index is found, new index is not found
            # Add this new index
            newchardata = charlist[oldindex].copy()
            newchardata["nameid"] = newid
            newchardata["name"] = newnames
            newchardata["fullid"] = newchar["newid"]

            if nameaddon == "ADDON":
                newchardata["base"] = charlist[oldindex]["nameid"] 

            charlist.insert(oldindex + 1, newchardata)

    save_json(charlist, "charlist.json", prettify=True)