import ijson
import json
import pandas as pd
import requests


filename = 'output.json'


def get_and_save(target_filename, file_url):
    with open(target_filename, 'wb') as handle:
        response = requests.get(file_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)



j = 0

with open(filename) as f:
    for line in f:
        try:
            card_json = json.loads(line)
            card_id = card_json['id']
            target_filename = './Pictures/' + card_id + '.jpg'
            large_url = card_json['image_uris']['large']

            get_and_save(target_filename, large_url)
            
        except:
            print("No image dict found...")
            j = j+1


print("Finished with ", j, " errors.")
