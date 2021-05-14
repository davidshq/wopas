import sqlite3
from sqlite3 import Error

# Connect to SQLite DB
def connect_sqlite(db_file):
    """ create a database connection to the SQLite db
        specified by db_file
    :param db_file: db file
    :return: Connection object or None
    """
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()