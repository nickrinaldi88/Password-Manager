import sqlite3

# creation connection object

conn = sqlite3.connect("pw_manager.db")

c = conn.cursor()

# c.execute("""CREATE TABLE accounts (
#     service TEXT,
#     username TEXT,
#     password TEXT) """)

# commits current transaction


def db_add(service, username, password):

    info = (service, username, password)

    c.execute('INSERT INTO accounts VALUES(?, ?, ?)', info)

    conn.commit()

    conn.close()


def display_db():

    global conn

    c = conn.cursor()

    for row in c.execute('SELECT * FROM accounts'):
        print(row)


def db_grab(service):

    for row in c.execute('SELECT service, password FROM accounts where service == ?', service,):
        print(row)


def close_db():

    conn.commit()

    conn.close()

# -Decide on SQL library to use
# -Create table:
# -Columns: Service
#			Username
#			Password
#			Email?
