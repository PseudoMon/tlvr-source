# TLVR's Data Processor
Everything here uses Python 3, so make sure you got that to get anything done. Moving images require FFMPEG accessible through the command line, so set that up first if you haven't.

There are three files of importance here: `grabfiles.py` download data from Kengxxiao's and/or images from Aceship's repo, `transformer.py` transforms data from Kengxxiao's repo into JSON that we can use (you can find the results in the folder `chardata`), and `mover.py` move the files here to the site folder next door (with some additional processing e.g. minifying). The `utils.py` just got your simple load/save json functions, etc.

Whenever you want to do something, you should go to this folder, go to the script you want to use and edit the `if __name__ ==__main__` part of it to just the function you need, and then run the file. Or you can just run Python on the command line and then import the file to run the functions. I might make a proper command line tooling eventually.

## grabfiles.py
Source JSON files are downloaded to the cn/en/jp/kr folders, while images are dropped in the images folder. None of those folders are included in this repo! You should do a clean download when setting up in a new machine.

There are two JSON files currently in use for each language: `charword_table.json` and `character_table.json`, both from Kengxxiao. The former contains the voice text lines while the latter has general operator data.

Running `grab_all_charword_tables()` and `grab_all_chartable()` will download all the data you need for all languages.

There used to be a `chardict.json` from ASTR, but I don't use that anymore. 

To download avatar images, you'll have to first generate a `charlist.json` with the next script. If you have the list, run `grab_avatars()` to grab avatar images from Aceship. If Aceship is down/is no longer updated, well, I'll finally have to do some datamining on my own.

Voices aren't downloaded here. They're loaded directly from [the audio repo](https://github.com/PseudoMon/arknights-audio). I update that by datamining the game. 

## transformer.py
Generally, file created by this script is included in this repo with nice indentation, so you can read it easily.

`make_and_save_charlist()` will process all character data from `character_table.json` into a `charlist.json`, a single file that contains names in all the languages, along with other data relevant for the list page of the site.

`get_welcome()` grabs the data used for the multilingual quote in the front page, which will result in `welcome.json`. At the moment this is hardcoded to Amiya's greeting, but I might add more later. 

`get_and_save_misc_data()` create `miscdata.json`, which contains data like factions. This requires `charlist.json` to already be available.

`process_all_characters()` process data for every character. The resulting files are made in the `chardata` folder.

Under the hood, it runs `get_and_write_chardata()` to create single JSON file for a character. Its first argument use Arknights's usual internal name (e.g. *char_002_amiya*). Four other functions are ran within it:
1. `get_voices()` to get the voice text.
2. `get_actors()` to get voice actor names. This is taken from the EN and JP data (the latter have names in the native script, the former have pen name used in the global server).
3. `get_voice_availability()` to check for which audio files should be available. I used to check the CN server data for this, but since audio files are based on the EN version now, this check the EN version.

## mover.py
Three functions you can use here: `move_chardata()`, `move_charlist()`, `move_avatars()`. Sorry about the name; *copy* is probably a better name, since we leave the source as is.

The resulting JSON are always minified (no more nice indent). Resulting images are converted to WEBP to save bandwith. Right now this webp is lossy and it's serviceable but kinda suck. I'll see if lossless webp is small enough. 