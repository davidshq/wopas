import requests
import os.path
import html
import sys
import time
import json
import get_num_of_plugins
from get_num_of_plugins import get_num_of_plugins
# !!Uncomment below to use interactively!!
# import ask_setup_questions
# from ask_setup_questions import ask_setup_questions

# Ask questions to determine what query is used against the API.
# plugins_per_page, plugins_order, starting_page, ending_page, select_path = ask_setup_questions(avail_num_results)
# !!Uncomment above to use interactively!!

# Get the total number of plugins available from the WordPress.org Plugin API.
avail_num_results = get_num_of_plugins()

# !!Comment below out to use interactively!!
# Set parameters below to determine what query is run against API.
plugins_per_page = 250 # 10
plugins_order = 'popular'
starting_page = 1
ending_page = 3 # int(round(avail_num_results/plugins_per_page))
select_path = "E:\wopas"
# !!Comment above out to use interactively!!

# Set variables for first page and last page of API results to be retrieved.
# page_number will be incremented as we loop through pages of API results.
page_number = int(starting_page)
last_page = int(ending_page)

# Initialize a variable to track the plugin number we are currently on.
plugin_number = 1

# Initialize a dictionary we'll store all of the plugin data in.
plugins = {}

# Loop that executes until page_number is equal to last_page + 1.
while page_number is not last_page + 1:
    # The API call we will be making.
    url = 'https://api.wordpress.org/plugins/info/1.1/?action=query_plugins& \
    request[per_page]={}&request[browse]={}&request[page]={}&request[fields][description]=0 \
    &request[fields][sections]=0'.format(plugins_per_page, plugins_order, page_number)

    # Make the call, store reply in response.
    response = requests.get(url)

    # Store only the JSON portion of the response in json_data
    json_data = response.json()

    # Get the total number of pages of results available using configured variables above.
    num_pages = json_data['info']['pages']

    # Store only the plugins portion of the JSON data
    json_plugins = json_data['plugins']

    # For each JSON object in json_plugins, add an object to dictionary plugin
    for id, plugin in enumerate(json_plugins):
            plugins[id] = plugin
    page_number += 1

file = "wp-plugins.json"
with open(os.path.join(select_path, file), 'a+', encoding='utf-8', errors="replace") as outfile:
    json.dump(json_plugins, outfile, sort_keys=False, indent=4)

