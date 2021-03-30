import sqlite3

def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d

db = sqlite3.connect('test_db.sqlite')
db.row_factory = dict_factory
cursor = db.cursor()

email = 'doe@gmail.com'
# cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
# cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?", (email, 'John Doe'))
# cursor.execute("SELECT * FROM users WHERE email = :email OR name = :name", {'email': email, 'name': 'Nisk Sand'})
# res = cursor.fetchone()

cursor.execute("SELECT * FROM users")
res = cursor.fetchall()

print(res)

# for user in res:
#     print(user[1], user[2])

for user in res:
    print(user['name'], user['email'])


db.close()