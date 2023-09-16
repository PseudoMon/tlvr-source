import requests
from os import path

base_chardicturl = "https://raw.githubusercontent.com/050644zf/ArknightsStoryJson/main/{}/chardict.json"
chardictsurls = {
    "en": base_chardicturl.format("en_US"),
    "jp": base_chardicturl.format("ja_JP"),
    "cn": base_chardicturl.format("zh_CN"),
    "kr": base_chardicturl.format("ko_KR"),
}
base_avatar = "https://raw.githubusercontent.com/Aceship/Arknight-Images/main/avatars/char_{}.png"

base_charwordurl = "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/{}/gamedata/excel/charword_table.json"
charwordsurls = {
    "en": base_charwordurl.format("en_US"),
    "jp": base_charwordurl.format("ja_JP"),
    "cn": base_charwordurl.format("zh_CN"),
    "kr": base_charwordurl.format("ko_KR"),
}


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

def grab_avatar(char):
    fullid = f"{char['numberid']}_{char['nameid']}"
    url = base_avatar.format(fullid)
    target = path.join("images", "avatars", f"{fullid}.png") 
    download_image(url, target)

if __name__ == "__main__":  
    grab_all_charword_tables()