import sqlite3
from wopas import connect_sqlite

# Use SQLite for data storage
def use_sqlite():
    connect_sqlite('results\wopas.sqlite')

    print("Goodbye")