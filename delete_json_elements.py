import os.path
import path
import json

with open('E:\wopas\wp-plugins.json', 'r') as data_file:
    data = json.load(data_file)

for element in data:
   # element.pop('description', None)
    element.pop('versions', None)


with open('E:\wopas\wp-plugins-after.json', 'w') as data_file:
    json_data = json.dumps(data, sort_keys=False, indent=4)
    data_file.write(json_data)