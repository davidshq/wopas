
import requests
import os.path
import html
import sys
import time
# Python 3 has the json library, if we are running Python 2 we need to use simplejson,
# which emulates the Python 3 library.
if sys.version < '3':
    import simplejson as json
else:
    import json

# Calls WP API to get page of Plugin Results, also returns last_page so we can
# terminate our loop when we have all our data
def get_plugin_info_page(page_number):
    # Added the per_page param to the endpoint so we can get more results per request
    # Each request will also take longer, so we're slowing down our rate a bit
    # TODO: Take user input for requests per page, type of browse, page range (including all)
    url = 'https://api.wordpress.org/plugins/info/1.1/?action=query_plugins& \
           request[per_page]=250&request[browse]=popular&request[page]={}'.format(page_number)
    response = requests.get(url)
    json_data = response.json()

    num_pages = json_data['info']['pages']
    wp_plugins = json_data['plugins']

    return wp_plugins, num_pages

# Make plugins folder if it doesn't exist
# TODO: Allow user input to determine path
if not os.path.exists('plugins'):
    os.mkdir('plugins')

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
    for plug in plugins:
        plugin_name = plug['name']

        # Save to a Folder so we don't clutter current directory
        file = "plug{}.json".format(plug['slug'])  # Slug is the plugin name without spaces, usually used to create URLs

        # I hate encoding/decoding crap and this took me forever to get working. Windows is the worst.
        # TODO: Remember to make 'plugins' a variable once user input accepted.
        with open(os.path.join('plugins', file), 'w+', encoding='utf-8', errors="replace") as outfile:
            json_data = json.dumps(plug, sort_keys=False, indent=4) # TODO: Add user input parameters for options.

            # html.unescape will remove all those weird characters, they're like PHP line breaks or something
            php_crap_removed = html.unescape(json_data)
            outfile.write(php_crap_removed)
            print("Plugin {} added".format(plugin_name))

    print("Page {} of {} total pages complete".format(page_number, last_page))
    page_number += 1
    # TODO: Maybe include time.sleep as user input parameter?
    time.sleep(2)