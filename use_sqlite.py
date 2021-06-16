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
    except Error as e:
        print(e)
        return conn
    
    add_data(conn, plugins)

def add_data(conn, plugins):
    for plugin in plugins:
        sql_add_plugin = f"""INSERT INTO authors VALUES {plugin.name}, {plugin.author_profile};
        """
        cur = conn.cursor()
        cur.execute(sql_add_plugin)
