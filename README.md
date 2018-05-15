# WordPress.Org Plugin API Scraper (WOPAS)
WOPAS is a Python script that allows one to utilize the WordPress.org 
Plugin API (not the WordPress Plugin API) to download the plugin directory's
plugin contents.

Please use responsibly (aka, don't hammer the WordPress.org servers!)

# What's Next
- Adding the ability to choose what query you want to run against the API.
- Allowing one to limit the number of results returned (right now it grabs all of them).

# Release History
- 0.5. - 5/13/18:
    - API request now asks that description and sections not be included in file, significantly decreases amount of data received.
    - WP.org API inconsistently returns dicts or lists, added code that detects what is being returned and converts to dict if necessary.
    - Added logic to add [ at the beginning and ] at the end of single file JSON output to enclose all JSON objects in an array.
    - Added logic to place commas between JSON objects in a single file.
    - Added separate script that reads in the JSON file and outputs it without the versions info. This can be easily modified to remove any info. desired.
    - HT to AlexCoventry, Rascal_Two, and Zigity_Zagity on the LearnPython subreddit for helping me work through these enhancements.
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
