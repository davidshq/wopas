# A very basic query without additional parameters, will return 24 plugins details as well
# as some meta information - e.g., page of results, total pages available, and total plugins available.
import requests
import json

url = 'https://api.wordpress.org/plugins/info/1.1/?action=query_plugins'
response = requests.get(url)
json_data = response.json()
raw_plugins = json_data['plugins']
plugins = raw_plugins
# Sometimes the API returns a dictionary, sometimes a list
# If it returns a list we want to convert the list to a dictionary
# to make it easier to handle
if type(plugins) != dict:
        plugins = {}
        for i, plugin in enumerate(raw_plugins):
            plugins[i] = plugin
# Output the dictionary to the screen
for plugin in plugins.items():
    print(json.dumps(plugin))
