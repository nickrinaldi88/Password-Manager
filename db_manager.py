import sqlite3
import pass_manager

# creation connection object

conn = sqlite3.connect("pw_manager.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS accounts (
    service TEXT,
    username TEXT,
    password TEXT) """)


def db_add(service, username, password):

    info = (service, username, password)
    c.execute('INSERT INTO accounts VALUES(?, ?, ?)', info)


def display_db():

    for row in c.execute('SELECT * FROM accounts'):
        print(row)


def db_update(service, new_pwd):

    c.execute('UPDATE accounts SET password = ? WHERE service= ?',
              (new_pwd, service))


def db_remove(service):

    c.execute('DELETE from accounts WHERE service = ?', (service,))


def db_chek(service):

    for row in c.execute('SELECT service from accounts WHERE service = ?', (service,)):
        print("Found " + str(row))


def db_grab(service):

    # service is being read as 3 characters, rather than one

    for row in c.execute('SELECT * FROM accounts where service == ?', (service,)):
        print(row)


def close_db():

    conn.commit()
    conn.close()
