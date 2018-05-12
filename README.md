# WordPress.Org Plugin API Scraper (WOPAS)
WOPAS is a Python script that allows one to utilize the WordPress.org 
Plugin API (not the WordPress Plugin API) to download the plugin directory's
plugin contents.

Please use responsibly (aka, don't hammer the WordPress.org servers!)

# What's Next
- Adding the ability to choose what query you want to run against the API.
- Allowing one to limit the number of results returned (right now it grabs all of them).

# Release History
- 0.4 - 5/12/18:
    - Added ability to choose between each plugin getting its own file and all plugins being compiled in one file.
    - Moved get_plugin_info_page into its own file.
- 0.3.1 - 12/4/17:
	- Corrected error introduced in 0.3 which caused prompting for user input repeatedly.
- 0.3 - 12/4/17:
	- Added initial logic for choosing the sort used when returning plugins.
	- Added ability to choose how many results to return.
	- Added requirements.txt
	- Updated .gitignore
	- Response from WP API seems to have changed from list to dictionary causing an error, fixed.
	- Added the ability to specify directory you want to save results to.
- 0.2 - 10/7/17 - Removed calls to html.unescape which was causing JSON to be invalid.
- 0.1 - 7/22/17 - Initial GitHub release. Pre-History can be found on [Reddit](https://www.reddit.com/r/learnpython/comments/6o4tls/help_parsing_json/) and elsewhere on [Reddit](https://www.reddit.com/r/Python/comments/6nk5yl/help_needed_using_python_to_pull_in_and_transform/).
