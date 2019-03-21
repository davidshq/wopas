import requests
import html
import sys
import time
import json

# Get the total number of WordPress plugins available from the WordPress.org Plugin API

def get_num_of_plugins():
    # API call we are making.
    url = 'https://api.wordpress.org/plugins/info/1.1/?action=query_plugins& \
    request[browse]=popular'

    # Make call, store reply in response.
    response = requests.get(url)

    # Store only JSON portion of response in json_data
    json_data = response.json()

    # Get total number of pages of results available
    num_results = json_data['info']['results']

    # Return total number of pages
    return num_results