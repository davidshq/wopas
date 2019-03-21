# WordPress.Org Plugin API Scraper (WOPAS)
WOPAS is a Python script that allows one to utilize the WordPress.org 
Plugin API (not the WordPress Plugin API) to download the plugin directory's
plugin contents.

Please use responsibly (aka, don't hammer the WordPress.org servers!)

# Things You Should Know
- WOPAS uses pipenv for package/dependency management, this is preferred over requirements.txt
- WOPAS uses the popular requests library for querying the WP.org API but then uses the native Python JSON library for manipulation of the returned results because the requests JSON functionality is fairly basic.
- The application has moved from interactive to config file driven. Desired settings are configured in wopas.ini.

# What's Next
- Adding the ability to choose what query you want to run against the API.

# Release History
- 0.9 - 3/21/19:
  - This is what happens when you don't touch a codebase for a long time and then come back to it...Simplifying code to make it easier to build out again
  - Code no longer offers option to save plugins to individual files and get_page_of_results.py has been deprecated; may be recreated later.
  - wopas.py now includes preset values that allow bypassing interactivity; you'll need to comment out preset values and uncomment lines as instructed in wopas.py to reenable interactive mode.
- 0.8 - 3/9/19:
  - Updated example code and renamed folder/file to learn/basic_api_call.py
- 0.7 - 5/29/18:
  - One can now limit the number of pages of results returned.
  - Refactoring to make the code more OOP.
- 0.6 - 5/22/18:
  - API now asks user to provide parameters for starting and ending pages.
  - Breaking out minimal functionality into separate files for testing in small-bits folder.
  - Added delete_json_elements.py which provides basic method for removing elements from a saved json file.
  - Bug fixes, code cleanup, comments, and introduction of new bugs. :)
- 0.5 - 5/13/18:
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
