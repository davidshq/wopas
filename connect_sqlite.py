import sqlite3
from sqlite3 import Error

def connect_sqlite(db_file):
    """ 
    create connection to the SQLite database
    :param db_file: database file
    :return: Connection object or None
    """

    conn = None

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn