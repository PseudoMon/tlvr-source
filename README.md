# Rhodes Island Tetralingual Voice Record Archive
Or just TLVR for short.

An Arknights fansite where you can listen/read operator's voice records and switch easily between languages.

I'm learning Chinese and Japanese and I am hopelessly in love with web design and development so I'm willing to waste whole weekends for this apparently.

The two folders of this repo are for the two parts of this project: the part where I organize the data into something the site can read (that's `datascript`), and the site itself (that's `site`). Look at the README in the respective folders for more details on how they're run. 

## The README in the respective folders
- For the [data](datascript/README.md)
- For the [site](site/README.md)

## Special Thanks
Voice files are from [Aceship's repo](https://github.com/Aceship/Arknight-voices) (they're not provided in this repo) and text data are processed from [Kengxxiao's repo](https://github.com/Kengxxiao/ArknightsGameData).  

Also checkout the [Arknights Story Text Reader](https://github.com/050644zf/ArknightsStoryTextReader) if you're looking for the story text instead of voices.

## Bugs to squash
- Nine-colored Deer (and other crossover characters) puts CV data in different place, so they're not shown here. Fix that.
- Xiaohei only have the cat noise, not the human form voice. Low-priority, but might be worth a look

## Upcoming features
- Rarity and faction filters in the list page
- Regional voice
- Lazy loading in list page so users don't have to load all uhh 3MB of images
- Command line tooling (or maybe even Github actions?) for updating the data