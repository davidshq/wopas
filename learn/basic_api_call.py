# Basic query without additional parameters.
import requests # http://docs.python-requests.org
import json

# The API URL we are querying.
url = 'https://api.wordpress.org/plugins/info/1.1/?action=query_plugins'

# Storing the returned data in response
response = requests.get(url)

# Pulling out the JSON data from the response
response_json = response.json()

# The JSON response includes meta information such as page of results being returned;
# how many are available total; etc. We only want to see the actual plugin data; so
# pull only json within plugins
plugins_json = response_json['plugins']

# Sometimes the API returns a dictionary, sometimes a list
# (shorter queries are returned as list, longer as dictionary)
# Rather than deal with both, we'll convert any lists to dictionaries
if type(plugins_json) != dict:
    plugins = {}
    # For each plugin entry in plugins_json
    for i, plugin in enumerate(plugins_json):
        # Create an entry in the dictionary
        plugins[i] = plugin

# Print contents of the dictionary to screen
for plugin in plugin.items():
    print(json.dumps(plugin, indent=4))
