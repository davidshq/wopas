import requests
import ask_setup_questions
from ask_setup_questions import ask_setup_questions
import use_preset_values
from use_preset_values import use_preset_values
from count_plugins import count_plugins
from create_json import create_json
from use_sqlite import use_sqlite

# Get the total number of plugins available from the WordPress.org Plugin API.
avail_num_results = count_plugins()

# Will we be running interactively or using presets?
interactive_query = input('Do you want to configure how WOPAS queries the API? (Y or N)')
if interactive_query == 'Y':
    # Ask questions to determine what query is used against the API.
    plugins_per_page, plugins_order, starting_page, ending_page, select_path = ask_setup_questions(avail_num_results)
else:
    # Use preset values to query against API.
    plugins_per_page, plugins_order, starting_page, ending_page, select_path = use_preset_values(avail_num_results)


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

    # Make the call, store reply from API in response.
    response = requests.get(url)

    # Store only the JSON portion of the response in response
    response_json = response.json()

    # Get the total number of pages of results available.
    avail_num_pages = response_json['info']['pages']

    # Store only the plugins portion of the JSON data
    json_plugins = response_json['plugins']

    # For each JSON object in json_plugins, add an object to our plugins dictionary
    for id, plugin in enumerate(json_plugins):
            plugins[id] = plugin
    page_number += 1

# Will we be using JSON or SQLite for data storage?
data_storage_query = input('Do you want to use JSON or SQLite as your data storage? (json or sqlite)')

if data_storage_query == 'json':
    create_json(select_path, json_plugins)
elif data_storage_query == 'sqlite':
    use_sqlite()
