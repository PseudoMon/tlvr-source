# TLVR's Data Processor
Everything here uses Python 3, so make sure you got that to get anything done. Moving images require FFMPEG accessible through the command line, so set that up first if you haven't.

There are three files of importance here: `grabfiles.py` download data from Kengxxiao's and ASTR's repo or images from Aceship's repo, `transformer.py` transforms data from Kengxxiao's repo into JSON that we can use (you can find the results in the folder `chardata`), and `mover.py` move the files here to the site folder next door (with some additional processing e.g. minifying). The `utils.py` just got your simple load/save json functions, etc.

Whenever you want to do something, you should go to this folder, edit the `if __name__ ==__main__` part of the file, and the run the file. Or you can just run Python on the command line and then import the file to run the functions. A proper command line tooling is still coming (if I ever get the desire for it).

## grabfiles.py
Source JSON files are downloaded to the cn/en/jp/kr folders, while images are dropped in the images folder. None of those folders are included in this repo! You should do a clean download when setting up in a new machine.

There are two JSON files currently in use for each language: `chardict.json` from ASTR, and `charword_table.json` from Kengxxiao. 

(I can technically just create a character list from the data from Kengxxiao's, but I'm lazy and just use the chardict.json that is used by ASTR (🙏).) 

`grab_all_chardicts()` and `grab_all_charword_tables()` will download all the relevant data.

Run `grab_avatars()` to grab avatar images from Aceship for each character in the EN version's chardict. The chardict should already be downloaded.

## transformer.py
Generally file created from this script is included in this repo with nice indentation, so you can read it easily.

`make_and_save_charlist()` will process all chardicts into a `charlist.json`, a single file that contains names in all the languages, along with other data relevant for the list page of the site.

`get_welcome()` grabs the data used for the multilingual quote in the front page, which will result in `welcome.json`. At the moment this is hardcoded to Amiya's greeting, but I might add more later. 

`get_and_write_chardata()` is the one to run to create a single json file for each character. Its first argument use Arknights's usual internal name (e.g. *char_002_amiya*). Four other functions are also ran with it:
1. `get_voices()` to get the voice text.
2. `get_actors()` to get voice actor names. This is taken from the EN and JP data (the latter have names in the native script, the former have pen name used in the global server).
3. `get_voice_availability()` to check for which audio files should be available. This is done by checking voice actor in the CN server, so it's possible that you can play the voice files in the site, but the actor's name isn't displayed.

If a `wordtables` is part of a function argument, then you need to load it first with `load_wordtabes()` (mind the plural). This function will create a dict with the key being the language code (e.g. `cn`). 

## mover.py
Three functions you can use here: `move_chardata()`, `move_charlist()`, `move_avatars()`. Sorry about the name; *copy* is probably a better name, since we leave the source as is.

The resulting JSON are always minified (no more nice indent). Resulting images are converted to WEBP to save bandwith (TLVR is not the site to go for lossless images, aha).