import requests
from os import path
from utils import load_json

def getregurls(baseurl):
    return {
        "en": baseurl.format("en_US"),
        "jp": baseurl.format("ja_JP"),
        "cn": baseurl.replace("ArknightsGameData_YoStar", "ArknightsGameData")
              .format("zh_CN"),
        "kr": baseurl.format("ko_KR"),
    }

base_chardicturl = "https://raw.githubusercontent.com/050644zf/ArknightsStoryJson/main/{}/chardict.json"
chardictsurls = getregurls(base_chardicturl)

base_avatar = "https://raw.githubusercontent.com/Aceship/Arknight-Images/main/avatars/char_{}.png"

base_charwordurl = "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/master/{}/gamedata/excel/charword_table.json"
charwordsurls = getregurls(base_charwordurl)

base_chartable = "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/master/{}/gamedata/excel/character_table.json"
chartableurls = getregurls(base_chartable)

base_faction_url = "https://raw.githubusercontent.com/Aceship/Arknight-Images/main/factions/logo_{}.png"

def download_text(url, target):
    response = requests.get(url)
    response.raise_for_status()

    with open(target, "w", encoding="utf-8") as targetfile:
        targetfile.write(response.text) 

    print("Succesfully written {} to {}".format(url, target))

def download_image(url, target):
    # Image uses streaming 
    response = requests.get(url, stream=True)
    if not response.ok:
        print(response)
        return

    with open(target, 'wb') as targetfile:   
        for block in response.iter_content(1024):
            if not block:
                break
            targetfile.write(block)

    print("Sucesfully downloaded image {} to {}".format(url, target))

def grab_chardict(region):
    # This is not longer used since we don't take from ASTR anymore
    download_text(
        chardictsurls[region], 
        path.join(region, "chardict.json")
    )

def grab_all_chardicts():
    for region in chardictsurls:
        grab_chardict(region)


def grab_charword_table(region):
    download_text(
        charwordsurls[region],
        path.join(region, "charword_table.json")
    )

def grab_all_charword_tables():
    for region in charwordsurls:
        grab_charword_table(region)

def grab_all_chartable():
    for region in chartableurls:
        download_text(
            chartableurls[region],
            path.join(region, "character_table.json")
        )

def grab_avatar(char):
    fullid = f"{char['numberid']}_{char['nameid']}"
    url = base_avatar.format(fullid)
    target = path.join("images", "avatars", f"{fullid}.png") 

    if path.isfile(target):
        print("Image already exists. Skipping...")
    else:
        download_image(url, target)

def grab_avatars():
    charlist = load_json("charlist.json")
    for char in charlist:
        numberid = char["numberid"] 
        nameid = char["nameid"]
        print(f"{numberid}_{nameid}")

        grab_avatar(char)

def grab_factions():
    # This will require charlist.json that also contains nation data
    # Since those are the faction images we'll be taking
    charlist = load_json("charlist.json")

    factions_to_grab = []
    for char in charlist:
        nation = char["nation"]
        if nation is not None and nation not in factions_to_grab:
            factions_to_grab.append(nation) 

    for faction in factions_to_grab:   
        url = base_faction_url.format(faction) 
        download_image(url, f"images/factions/{faction}.png")

if __name__ == "__main__":
    grab_all_charword_tables()
    grab_all_chartable()

    # grab_factions()
    grab_avatars()