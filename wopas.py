import requests
import os.path
import html
import sys
import time
import json
import get_page_of_results
from get_page_of_results import get_page_of_results
import get_num_of_plugins
from get_num_of_plugins import get_num_of_plugins
import ask_setup_questions
from ask_setup_questions import ask_setup_questions

# Get the total number of plugins available from the WordPress.org Plugin API.
avail_num_results = get_num_of_plugins()

# Ask questions to determine what query is used against the API.
plugins_per_page, plugins_order, starting_page, ending_page, select_path, multiple_files = ask_setup_questions(avail_num_results)

page_number = int(starting_page) # The Page of API results we are going to start returning results from.
last_page = int(ending_page) # The Last Page of API results we are going to return results from.
plugin_number = 1

# Loops until page number = last_page (+1 because we still want the last page)
while page_number is not last_page + 1:

    plugins = get_page_of_results(page_number, plugins_per_page, plugins_order, multiple_files)

    # Loop through wp_plugin data
    for pid, plugin in plugins.items():
        plugin_name = plugin['name']

        # Put everything in one file.
        if multiple_files == 'N':
            file = "wp-plugins.json"

        # Give each plugin its own file.
        if multiple_files == 'Y':
            file = "plugin-{}.json".format(plugin['slug'])  # Slug is the plugin name without spaces, usually used to create URLs

        with open(os.path.join(select_path, file), 'a+', encoding='utf-8', errors="replace") as outfile:
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
    with open(os.path.join(select_path, file), 'a+', encoding='utf-8', errors="replace") as outfile:
        outfile.write(']')
