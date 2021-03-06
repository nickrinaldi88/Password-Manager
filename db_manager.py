import sqlite3
import pass_manager
import pyperclip
import time


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


def db_update(service, new_pwd):

    c.execute('UPDATE accounts SET password = ? WHERE service= ?',
              (new_pwd, service))


def db_remove(service):

    c.execute('DELETE from accounts WHERE service = ?', (service,))


def db_chek(service):

    if c.execute('SELECT service from accounts WHERE service = ?', (service,)).fetchone():
        print("------------------------------------------")
        print("Found " + service)
    else:
        ("------------------------------------------")
        print("The the service does not exist in the database!")
        return False


def db_grab(service):

    print("Service " + "|" + " Username " + "|" + " Password")
    print("------------------------------------------")

    for row in c.execute('SELECT * FROM accounts where service == ?', (service,)):
        print(row)

    pyperclip.copy(row[2])
    print("------------------------------------------")
    print("Password has been copied to the clipboard!")
    print("------------------------------------------")


def display_db():
    print("----------Display Menu----------")

    print("Service " + "|" + " Username " + "|" + " Password")
    print("------------------------------------------")

    for row in c.execute('SELECT * FROM accounts'):
        time.sleep(0.5)
        print(row)


def close_db():

    conn.commit()
    conn.close()
