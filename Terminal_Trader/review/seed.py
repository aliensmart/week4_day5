import sqlite3


with sqlite3.connect('computers.db') as connection:
    cursor = connection.cursor()

    SQL = """INSERT INTO users (
        name, phone, email, credit_card) 
        VALUES (?,?,?,?);"""

    values = [
        ["Greg", "111-111-1111", "email@greg.com", 12309829389],
        ["Justin", '222-222-2222', "justin@email.com", 90000000000],
        ["Abdoul", '233-332-3332', "abdoul@gmail.com", 88760000000]
    ]

    for value in values:
        cursor.execute(SQL, value)

