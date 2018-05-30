import requests
import html
import sys
import time
import json

def get_num_of_plugins():
    url = 'https://api.wordpress.org/plugins/info/1.1/?action=query_plugins& \
    request[browse]=popular'

    response = requests.get(url)
    json_data = response.json()

    num_results = json_data['info']['results']

    return num_results