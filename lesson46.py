import sqlite3

db = sqlite3.connect('test_db.sqlite')
cursor = db.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY, 
#     name TEXT NOT NULL, 
#     email TEXT NOT NULL UNIQUE
# )
# ''')
# cursor.execute("INSERT INTO users (name, email) VALUES ('Henry Bob', 'henry@gmail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Kokos Kokos', 'kokos@gmail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Bob Anry', 'bob@gmail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Duna Katy', 'duna@gmail.com')")
# cursor.executescript('''
# # INSERT INTO users (name, email) VALUES ('John Doe', 'doe@gmail.com');
# # INSERT INTO users (name, email) VALUES ('Nisk Sand', 'sand@gmail.com');
# # ''')
users = [
    ('User1', 'user1@gmail.com'),
    ('User2', 'user2@gmail.com'),
    ('User3', 'user3@gmail.com')
]
cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)
db.commit()

db.close()
