import requests
import os.path
import html
import sys
import time
import pdb
import json
import get_plugin_info_page
from get_plugin_info_page import get_plugin_info_page
# Python 3 has the json library, if we are running Python 2 we need to use simplejson,
# which emulates the Python 3 library.


# Allow user to enter path they want to store plugin data in.
selectpath = input('Where do you want to store the plugin data?')
if not os.path.exists(selectpath):
    os.mkdir(selectpath)

# TODO: Take user input for requests per page, type of browse, page range (including all)
plugins_per_page = input('How many plugins do you want to be returned in each API response? [Default: 250]')
plugins_order = input('In what order do you want the results returned? [Default: popular]')
multiple_files = input('Should each plugin be saved to a separate JSON file? [Default: N]')
if not plugins_per_page:
    plugins_per_page = 250
else:
    plugins_per_page = int(plugins_per_page)
# Bahh! WP.org API is returning a dict when querying popular but a list when querying featured
# For right now, just use popular, until I work out logic to respond with processing by dict/list as needed.
if not plugins_order:
    plugins_order = 'popular'
if not multiple_files:
    multiple_files = 'N'

# Set initial values for last_page and page_number
# TODO: This will need to change once user input is accepted
last_page = 1
page_number = 1
plugin_number = 1

# Loops until page number = last_page (+1 because we still want the last page)
while page_number is not last_page + 1:

    # last_page is updated after the first loop
    # everytime really, but this shouldn't add any overhead
    # TODO: This too, maybe using a variable that detects whether last_page is user input or all
    plugins, last_page = get_plugin_info_page(page_number, plugins_per_page, plugins_order, multiple_files)

    # Loop through wp_plugin data
    for pid, plugin in plugins.items():
        plugin_name = plugin['name']

        if multiple_files == 'N':
            file = "wp-plugins.json"

        if multiple_files == 'Y':
            file = "plugin-{}.json".format(plugin['slug'])  # Slug is the plugin name without spaces, usually used to create URLs

        with open(os.path.join(selectpath, file), 'a+', encoding='utf-8', errors="replace") as outfile:
            if plugin_number == 1 and multiple_files == 'N':
                outfile.write('[')

            json_data = json.dumps(plugin, sort_keys=False, indent=4) # TODO: Add user input parameters for options.
            outfile.write(json_data)
            if multiple_files == 'N':
                outfile.write(',')
            print("Plugin Number {} Named: {} added".format(plugin_number, plugin_name))
        plugin_number +=1

    print("Page {} of {} total pages complete".format(page_number, last_page))
    page_number += 1
    # TODO: Maybe include time.sleep as user input parameter?
    time.sleep(2)

if multiple_files == 'N':
    with open(os.path.join(selectpath, file), 'a+', encoding='utf-8', errors="replace") as outfile:
        outfile.write(']')
