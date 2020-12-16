from sqlite3 import Connection, connect

def open_db() -> Connection:
    return connect(':memory:')
