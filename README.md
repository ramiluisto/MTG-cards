# MTG-cards
A sandbox where I apply ML stuff to a database of cards from the game 'Magic: the Gathering'.

*Heavily under construction.*

The files "Parserer.py", "Panderer.py" and "Picturer.py" are scripts used off-cloud to process very large json files and to download related images. To use them, you need to have the bulk json file e.g. from https://scryfall.com/docs/api/bulk-data which you then run Parserer.py to get 'output.json' which in turn is processed by Panderer.py into 'Formatted_list.json'. The Picturer.py script downloads related card imagery from scryfall.

In the future we'll also have a script that converts those downloaded .jpg images into Numpry arrays.

