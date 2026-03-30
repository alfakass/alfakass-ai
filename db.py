import sqlite3
import sqlite_vec

def get_db_connection():
    connection = sqlite3.connect("vec-store.db")
    connection.enable_load_extension(True)
    sqlite_vec.load(conn=connection)

    return connection