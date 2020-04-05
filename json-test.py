import json

with open('jsonfile.json') as json_file:
    data = json.load(json_file)
    for data_piece in data['records']:
        print(data_piece)
