# WordPress.Org Plugin API Scraper (WOPAS)
WOPAS is a Python script that allows one to utilize the WordPress.org 
Plugin API (not the WordPress Plugin API) to download the plugin directory's
plugin contents.

Please use responsibly (aka, don't hammer the WordPress.org servers!)

# What's Next
- Adding the ability to choose what query you want to run against the API.
- Allowing one to limit the number of results returned (right now it grabs all of them).

# Release History
- 0.2 - 10/7/17 - Removed calls to html.unescape which was causing JSON to be invalid.
- 0.1 - 7/22/17 - Initial GitHub release. Pre-History can be found on [Reddit](https://www.reddit.com/r/learnpython/comments/6o4tls/help_parsing_json/) and elsewhere on [Reddit](https://www.reddit.com/r/Python/comments/6nk5yl/help_needed_using_python_to_pull_in_and_transform/).
