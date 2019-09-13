import sqlite3


with sqlite3.connect('computers.db') as connection:
    cursor = connection.cursor()
    
    SQL = "DROP TABLE IF EXISTS computers;"

    cursor.execute(SQL)

    SQL = """CREATE TABLE computers(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        brand VARCHAR,
        model VARCHAR,
        year INTEGER,
        ram INTEGER,
        disk INTEGER,
        user_pk INTEGER,
        FOREIGN KEY(user_pk) REFERENCES users(pk)
        );"""

    cursor.execute(SQL)

    SQL = "DROP TABLE IF EXISTS users;"

    cursor.execute(SQL)

    SQL = """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        phone VARCHAR,
        email VARCHAR,
        credit_card INTEGER
    );"""

    cursor.execute(SQL)
