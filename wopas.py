import requests
import os.path
import html
import sys
import time
import json
import get_plugin_info_page
from get_plugin_info_page import get_plugin_info_page
import get_basic_plugin_info
from get_basic_plugin_info import get_basic_plugin_info

# Get the total number of plugins available from the API.
avail_num_results = get_basic_plugin_info()

# Interactive Questions That Determine How the API is Queried.
print(f'There are {avail_num_results} plugins available from the WordPress.org Plugin API.')
plugins_per_page = input('How many plugins do you want to be returned for each API call? [Default: 250]')
if not plugins_per_page:
    plugins_per_page = 250
else:
    plugins_per_page = int(plugins_per_page)
print('The WordPress.org API supports returning results ordered by popularity, search, tag, and author. Currently WOPAS only supports ordering by popularity.')
plugins_order = input('In what order do you want the results returned? [Default: popular]')
if not plugins_order:
    plugins_order = 'popular'
starting_page = input('What is the first page of results you want to return results from? [Default: 1]')
if not starting_page:
    starting_page = 1
max_ending_page = int(round(avail_num_results/plugins_per_page))
ending_page = input(f'What is the last page of results you want to return results from? [Default: {max_ending_page}]')
if not ending_page:
    ending_page = max_ending_page
selectpath = input('Where do you want to store the plugin data?')
if not os.path.exists(selectpath):
    os.mkdir(selectpath)
multiple_files = input('Should each plugin be saved to a separate JSON file? [Default: N]')
if not multiple_files:
    multiple_files = 'N'

page_number = int(starting_page) # The Page of API results we are going to start returning results from.
last_page = int(ending_page) # The Last Page of API results we are going to return results from.
plugin_number = 1

# Loops until page number = last_page (+1 because we still want the last page)
while page_number is not last_page + 1:

    plugins = get_plugin_info_page(page_number, plugins_per_page, plugins_order, multiple_files)

    # Loop through wp_plugin data
    for pid, plugin in plugins.items():
        plugin_name = plugin['name']

        # Put everything in one file.
        if multiple_files == 'N':
            file = "wp-plugins.json"

        # Give each plugin its own file.
        if multiple_files == 'Y':
            file = "plugin-{}.json".format(plugin['slug'])  # Slug is the plugin name without spaces, usually used to create URLs

        with open(os.path.join(selectpath, file), 'a+', encoding='utf-8', errors="replace") as outfile:
            if plugin_number == 1 and multiple_files == 'N': # We need to place each plugin object within a containing array.
                outfile.write('[')

            json_data = json.dumps(plugin, sort_keys=False, indent=4) # TODO: Add user input parameters for options.
            outfile.write(json_data)
            if multiple_files == 'N': # We need to separate each plugin object within the container array if using a single file.
                outfile.write(',')
            print("Plugin Number {} Named: {} added".format(plugin_number, plugin_name))
        plugin_number +=1

    print("Page {} of {} total pages complete".format(page_number, last_page))
    page_number += 1
    time.sleep(2)

# When we've finished processing all the individual plugins
if multiple_files == 'N':
    # Remove the last comma
    # with open(os.path.join(selectpath, file), '+r', errors="replace") as outfile:
    # outfile.seek(-1, os.SEEK_END)
    # outfile.truncate()
    # Close the container array
    with open(os.path.join(selectpath, file), 'a+', encoding='utf-8', errors="replace") as outfile:
        outfile.write(']')
