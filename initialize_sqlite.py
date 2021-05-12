import sqlite3
from sqlite3 import Error

def connect_sqlite(db_file):
    """ create a db connection to the SQLite database
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

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: CREATE TABLE statement
    :return:
    """

    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    db_file = 'wopas.sqlite'
    
    sql_create_authors_table = """CREATE TABLE IF NOT EXISTS authors (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL
    );"""

    sql_create_plugins_table = """CREATE TABLE IF NOT EXISTS plugins (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    slug text NOT NULL,
                                    version text NOT NULL,
                                    author_id integer,
                                    requires text,
                                    tested text,
                                    requires_php text,
                                    compatibility text,
                                    rating integer,
                                    ratings_1 integer,
                                    ratings_2 integer,
                                    ratings_3 integer,
                                    ratings_4 integer,
                                    ratings_5 integer,
                                    num_ratings integer,
                                    threads integer,
                                    threads_resolved integer,
                                    downloaded integer,
                                    added date,
                                    homepage text,
                                    short_description text,
                                    description text,
                                    download_link text,
                                    screenshots text,
                                    tags text,
                                    versions text,
                                    donate text,
                                    FOREIGN KEY (author_id) REFERENCES authors (id)
    );"""

    conn = connect_sqlite(db_file)

    if conn is not None:
        create_table(conn, sql_create_authors_table)

        create_table(conn, sql_create_plugins_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()