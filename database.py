import sqlite3

def get_connection():
    connection = sqlite3.connect("health_pal.db")
    return connection