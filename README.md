# WordPress.Org Plugin API Scraper (WOPAS)
WOPAS is a Python script that allows one to utilize the WordPress.org 
Plugin API (not the WordPress Plugin API) to download the plugin directory's
plugin contents.

Please use responsibly (aka, don't hammer the WordPress.org servers!)

# Things You Should Know
- WOPAS uses [pipenv](https://pipenv.pypa.io/en/latest/) for package/dependency management, this is preferred over requirements.txt
  - You can install pipenv using `pip install --user pipenv`
    - To setup an environment and install packages: `pipenv install`
- WOPAS uses the popular [requests](https://requests.readthedocs.io/en/latest/) library for querying the WP.org API but then uses the native Python JSON library for manipulation of the returned results because the requests JSON functionality is fairly basic.

# Release History
The notes were starting to get lengthy, see RELEASE_NOTES.md for details.