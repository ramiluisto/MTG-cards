import ijson
import json
import pandas as pd


# This script will read the preprocessed 'output.json' file
# line by line and convert it first to a pandas DataFrame
# and then write the result into a 'Formatted_list.json' -file.
# This script should be run after 'Parserer.py' and is in a separate
# file due to memory limitations on some (my) machines.


filename = 'output.json'

card_array = []

with open(filename) as f:
    for line in f:
        card_json = json.loads(line)
        card_array.append(card_json)


card_df = pd.DataFrame(card_array)


card_df.to_json('Formatted_list.json')

# The end.
