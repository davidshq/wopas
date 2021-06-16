import sqlite3
from sqlite3 import Error

def use_sqlite(db_file, plugins = ''):
    """ 
    create connection to the SQLite database
    :param db_file: database file
    :return: Connection object or None
    """

    conn = None

    try:
        conn = sqlite3.connect(db_file)
        if plugins != '':
            add_data(conn, plugins)
        return conn
    except Error as e:
        print(e)
        return conn
    


def add_data(conn, plugins):
    for index, plugin in plugins.items():
        cur = conn.cursor()
        print(plugin["name"])
        print(plugin["author_profile"])
        cur.execute("INSERT INTO authors VALUES (?, ?, ?)", (None, plugin["name"], plugin["author_profile"]))
