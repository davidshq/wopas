import os.path

# Set parameters below to determine what query is run against API.
# Note: You can specify an integer for the ending_page or you can calculate the last page of available
# results by changing end_page to:
# int(round(avail_num_results/plugins_per_page))

def use_preset_values(avail_num_results):
    plugins_per_page = 250 # 10
    plugins_order = 'popular'
    starting_page = 1
    ending_page = 3
    select_path = 'wopas'

    if not os.path.exists(select_path):
        os.mkdir(select_path)

    return plugins_per_page, plugins_order, starting_page, ending_page, select_path