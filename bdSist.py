import sqlite3

conn = sqlite3.connect('UserData')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NULL
);
""")
print("CONECTADO COM O BANDO DE DADOS")