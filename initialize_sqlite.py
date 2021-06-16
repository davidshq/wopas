import sqlite3
from sqlite3 import Error
from use_sqlite import use_sqlite

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
    db_file = r'wopas/wopas.db'
    
    sql_create_authors_table = """CREATE TABLE IF NOT EXISTS authors (
                                    id integer PRIMARY KEY,
                                    author text NOT NULL,
                                    author_profile NOT NULL
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
                                    num_ratings integer,
                                    threads integer,
                                    threads_resolved integer,
                                    downloads integer,
                                    added date,
                                    homepage text,
                                    short_description text,
                                    description text,
                                    download_link text,
                                    tags text,
                                    versions text,
                                    donate text,
                                    current integer,
                                    FOREIGN KEY (author_id) REFERENCES authors (id)
    );"""

    sql_create_ratings_table = """CREATE TABLE IF NOT EXISTS ratings (
                                    id INTEGER PRIMARY KEY,
                                    computed_rating text,
                                    ratings_1 text,
                                    ratings_2 text,
                                    ratings_3 text,
                                    ratings_4 text,
                                    ratings_5 text,
                                    timestamp date,
                                    plugin_id integer,
                                    FOREIGN KEY (plugin_id) REFERENCES plugins (id)
    );"""

    sql_create_images_table = """CREATE TABLE IF NOT EXISTS images (
                                    id INTEGER PRIMARY KEY,
                                    url text,
                                    plugin_id integer,
                                    FOREIGN KEY (plugin_id) REFERENCES plugins (id)
    );"""


    # Instantiate our db connection
    conn = use_sqlite(db_file)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_authors_table)

        create_table(conn, sql_create_plugins_table)

        create_table(conn, sql_create_ratings_table)

        create_table(conn, sql_create_images_table)

        conn.close()

    else:
        print("Error! cannot create the database connection.")
    

if __name__ == '__main__':
    main()