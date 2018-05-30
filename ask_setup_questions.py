import requests
import html
import sys
import time
import json
import os.path

def ask_setup_questions(avail_num_results):
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
    select_path = input('Where do you want to store the plugin data?')
    if not os.path.exists(select_path):
        os.mkdir(select_path)
    multiple_files = input('Should each plugin be saved to a separate JSON file? [Default: N]')
    if not multiple_files:
        multiple_files = 'N'

    return plugins_per_page, plugins_order, starting_page, ending_page, select_path, multiple_files