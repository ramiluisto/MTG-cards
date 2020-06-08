import ijson
import json
import pandas as pd

# This script will handle the first parsing round of the main card file.
# It will look at the file specified in the 'filename' variable
# and parse it line by line, reading each line into a json object
# and storing any data with english flag and headings in the 'column_name_list' below.
# (The fact that this prunes non-english data is currently hard-coded to the function 'line_handler', sry.)
# Each json object is then written to the file specified in the 'output_file'.



# Input file name:
filename = 'all-cards-20200602052133.json'
# Output file name:
output_file = 'output.json'


# This lists the column names that we wish to save.
column_name_list = [
    "object",
    "id",
    "name",
    "lang",
    "mana_cost",
    "cmc",
    "type_line",
    "oracle_text",
    "power",
    "toughness",
    "colors",
    "color_identity",
    "set",
    "set_name",
    "set_type",
    "rarity",
    "flavor_text",
    "image_uris"
]



# This is the main beast, which will handle each line based on the column list.
def line_handler(line, column_list):

    # We initialize a dictionary which will store the returned line data.
    dict = {}

    # We copy the line we are starting to work on
    # and remove line changes and commas if they exist at the end of the file.
    loop_string = line
    if loop_string[-1] == '\n':
        loop_string = loop_string[:-1]
    if loop_string[-1] == ',':
        loop_string = loop_string[:-1]

    # We check that we are not working with the first or last line of the json file.
    if (loop_string[0] != '[') & (loop_string[0] != ']'):

        # Now we try to load the line as a json object. If we fail
        # we do get an error message.
        try:
            loop_json = json.loads(loop_string)

        except:
            print('Error in line_handler json.loads; it doesn\'t :(')
            print('\n\n')
            print(loop_string)
            print('\n\n')


        # Next we start to work on importing the wanted columns from
        # the json object 'loop_json' into our dictionary object 'dict'.
        for column_name in column_list:
            # This try-except pair will trigger numerous times as
            # many cards, like lands, miss e.g. power and toughness or
            # some other properties.
            try:
                dict[column_name] = loop_json[column_name]
            except:
                continue 
                #print("Failed with ", column_name)


        # Not all cards have a language option, so we do
        # another try-catch here.
        try:
            language = dict['lang']
            if language == 'en':
                # When language flag exists and is 'en', we return the dict, otherwise
                # we will return an empty string.
                return(json.dumps(dict))
        except:
            print("no language?")

    # This return triggers unless we found an english language flag.
    return ''



######################################
## Here we read and write the files ##
######################################

# We open the destination file for writing,
# remember to close it in the end!
out = open(output_file, "w")

# Why is there an i here?
i=0

# Here we process the input file line by line and apply the function.
with open(filename) as f:
    for line in f:
        processed = line_handler(line, column_name_list)
        # We check if we get a non-empty string, and only write when we do.
        if len(processed) > 1:
            out.write(processed+'\n')
        
out.close()

# The end.
