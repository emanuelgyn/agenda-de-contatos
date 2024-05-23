import sqlite3

connecton = sqlite3.connect('agenda.db')

cursor = connecton.cursor()

cursor.execute('''
    CREATE TABLE contatos(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    number INTEGER NOT  NULL,
    email TEXT NOT NULL
    );
            ''')

connecton.close()
