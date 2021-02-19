import sqlite3
import pass_manager

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


def db_update(service, new_pwd):

    c.execute('UPDATE account SET password= ? WHERE service= ?')


def db_remove(service):

    c.execute('DELETE from accounts WHERE servce = ?', (service,))


def db_grab(service):

    # service is being read as 3 characters, rather than one

    for row in c.execute('SELECT service, password FROM accounts where service == ?', (service,)):

        # Invalid Token means the token is literally not valid


def print_keys():
    print("Key in db_manager")
    print(pass_manager.key)
    print("\n")
    print("Pass Manager key")
    pass_manager.print_key()


def delete_row(service):
    # for row in c.execute(#drop)
    pass


def close_db():

    conn.commit()

    conn.close()

# -Decide on SQL library to use
# -Create table:
# -Columns: Service
#			Username
#			Password
#			Email?
