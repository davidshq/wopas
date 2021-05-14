import os.path
import json

# Write the dictionary to a file as JSON.
def create_json(select_path, json_plugins):
    
    file = "wp-plugins.json"
    with open(os.path.join(select_path, file), 'a+', encoding='utf-8', errors="replace") as outfile:
        json.dump(json_plugins, outfile, sort_keys=False, indent=4)