import sqlite3

with sqlite3.connect("computers.db") as connect:
    cur = connect.cursor()
    SQL = """INSERT INTO users(name, phone, email, credit_card)
    VALUES (?,?,?,?);
    """

    values = [
        ["Greg", "11-111-1111", "greg@email.com", 12345673223]
        ["Abdoul", "222-222-2222", "abdoul@email.com", 7654321343]
        ["Greg", "11-111-1111", "greg@email.com", 32324344343]

    ]

    for value in values:
        cur.execute(SQL, value)