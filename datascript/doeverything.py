import grabfiles
import transformer
from extravoices import create_and_fill_in_extra_voices
import mover
from utils import load_json

if __name__ == "__main__":
    grabfiles.grab_all_charword_tables()
    grabfiles.grab_all_chartable()

    charlist, wordtables = transformer.run_transformer()
    charlist = load_json("charlist.json")
    wordtables = transformer.load_wordtables()
    create_and_fill_in_extra_voices(charlist, wordtables)

    # grabfiles.grab_factions()
    grabfiles.grab_avatars()

    mover.move_charlist()
    mover.move_chardata()
    mover.move_avatars()