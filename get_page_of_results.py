import requests
import os.path
import html
import sys
import time
import pdb
import json

# Calls WP API to get page of Plugin Results, also returns last_page so we can
# terminate our loop when we have all our data
def get_page_of_results(page_number, plugins_per_page, plugins_order, multiple_files):
    # Added the per_page param to the endpoint so we can get more results per request
    # Each request will also take longer, so we're slowing down our rate a bit
    url = 'https://api.wordpress.org/plugins/info/1.1/?action=query_plugins& \
           request[per_page]={}&request[browse]={}&request[page]={}&request[fields][description]=0&request[fields][sections]=0'.format(plugins_per_page, plugins_order, page_number)
    response = requests.get(url)
    json_data = response.json()

    num_pages = json_data['info']['pages']
    raw_plugins = json_data['plugins']
    plugins = raw_plugins

    if type(plugins) == dict:
        return plugins
    else:
        plugins = {}
        for i, plugin in enumerate(raw_plugins):
            plugins[i] = plugin
        return plugins
