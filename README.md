# WordPress.Org Plugin API Scraper (WOPAS)
WOPAS is a Python script that allows one to utilize the WordPress.org 
Plugin API (not the WordPress Plugin API) to download the plugin directory's
plugin contents.

Please use responsibly (aka, don't hammer the WordPress.org servers!)

# Things You Should Know
- WOPAS uses pipenv for package/dependency management, this is preferred over requirements.txt
- WOPAS uses the popular requests library for querying the WP.org API but then uses the native Python JSON library for manipulation of the returned results because the requests JSON functionality is fairly basic.

# Release History
The notes were starting to get lengthy, see RELEASE_NOTES.md for details.