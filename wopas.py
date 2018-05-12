import requests
import os.path
import html
import sys
import time
import pdb
import json
# Python 3 has the json library, if we are running Python 2 we need to use simplejson,
# which emulates the Python 3 library.

# Calls WP API to get page of Plugin Results, also returns last_page so we can
# terminate our loop when we have all our data
def get_plugin_info_page(page_number):
    # Added the per_page param to the endpoint so we can get more results per request
    # Each request will also take longer, so we're slowing down our rate a bit
    url = 'https://api.wordpress.org/plugins/info/1.1/?action=query_plugins& \
           request[per_page]={}&request[browse]={}&request[page]={}'.format(plugins_per_page, plugins_order, page_number)
    response = requests.get(url)
    json_data = response.json()

    num_pages = json_data['info']['pages']
    plugins = json_data['plugins']

    return plugins, num_pages

# Allow user to enter path they want to store plugin data in.
selectpath = input('Where do you want to store the plugin data?')
if not os.path.exists(selectpath):
    os.mkdir(selectpath)

# TODO: Take user input for requests per page, type of browse, page range (including all)
plugins_per_page = input('How many plugins do you want to be returned in each API response? [Default: 250]')
plugins_order = input('In what order do you want the results returned? [Default: popular]')
if not plugins_per_page:
    plugins_per_page = 250
# Bahh! WP.org API is returning a dict when querying popular but a list when querying featured
# For right now, just use featured, until I work out logic to respond with processing by dict/list as needed.
if not plugins_order:
    plugins_order = 'popular'

# Set initial values for last_page and page_number
# TODO: This will need to change once user input is accepted
last_page = 1
page_number = 1

# Loops until page number = last_page (+1 because we still want the last page)
while page_number is not last_page + 1:

    # last_page is updated after the first loop
    # everytime really, but this shouldn't add any overhead
    # TODO: This too, maybe using a variable that detects whether last_page is user input or all
    plugins, last_page = get_plugin_info_page(page_number)

    # Loop through wp_plugin data
    for pid, plugin in plugins.items():
        plugin_name = plugin['name']

        # Save to a Folder so we don't clutter current directory
        file = "plugin-{}.json".format(plugin['slug'])  # Slug is the plugin name without spaces, usually used to create URLs

        with open(os.path.join(selectpath, file), 'w+', encoding='utf-8', errors="replace") as outfile:
            json_data = json.dumps(plugin, sort_keys=False, indent=4) # TODO: Add user input parameters for options.
            outfile.write(json_data)
            print("Plugin {} added".format(plugin_name))

    print("Page {} of {} total pages complete".format(page_number, last_page))
    page_number += 1
    # TODO: Maybe include time.sleep as user input parameter?
    time.sleep(2)