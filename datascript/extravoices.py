from os import path
from utils import load_json
from transformer import load_wordtables, get_voices

def grab_uhh():
    unique_voices = []

    charlist = load_json("charlist.json")
    wordtables = load_wordtables()
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

            voices = get_voices(basedata["wordKey"], wordtables)

            if not (basedata["wordKey"] in unique_voices):
                unique_voices.append(basedata["wordKey"])

    print(unique_voices)
    return unique_voices

unique = grab_uhh()
unique[1]
voices = get_voices(unique[1], load_wordtables())
print(voices)