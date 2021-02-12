# nr-pw-manager

1. How do password managers work? -https://www.youtube.com/watch?v=w68BBPDAWr8
   -big list of passwords, encrypted using a key
   -associate encryption with needed an encryption key
   -master password to access database
   -creating a local password manager
2. Research hashing algorithims to use (sha 256?)
   -hashlib library -https://www.youtube.com/watch?v=rJANKZ682ks&list=PL1H1sBF1VAKUcc5BrTB0rEvJLtIIQVKe1
3. Create a SQL database of some kind (mysql)
   -tables: password, username, user_email, app_name, url
   -use SQLlite; for encryption of DB file and password protection of opening of the DB - https://stackoverflow.com/questions/5669905/sqlite-with-encryption-password-protection/5877130#5877130
4. Refresh memory on how to create, store and retrieve things from an SQL database
5. Create a terminal menu
6. Create master password
   -Google how to create a master password; the key

1a. How many files will I need? And for what?

-4 files?
-database_manager
-does DB stuff
-connect to database
FUNCTIONS:
-insert into db function, username, password, website, and email
-retrieve password function, given username and website
-hash_maker
-takes input, and generates hash key
-makes secret key
-do more research on this
-menu
-gui and menu display
-print organized display to the screen, asking for master password?
-create password
-store password
-password manager
-import menu
-works behind the scenes of menu
-runs functions based on input on the menu script

# basic functionality

# When user loads program, ask for master password

# when master password is entered, provide other options:

#THE BELOW IS IN THE pass_manager.py script

# add a password,

# (if clicked):

    		-Ask for service, username, password
    		-Take password, encode, run through hashing algorithm, and store in database
    		-Access function in database script to add to DB

# update a password,

# (if clicked):

    		-ask for service to update
    		-query DB for the service row
    		-ask whether you're updating username or password
    		-if username, ask for new username, update username row
    		-if password, ask for new password, encode, run through hash algorithm, update password row

# remove a password

    		-ask for service to remove
    		-query DB for the service row
    		-ask to enter the password
    		-then ask to confirm to remove

# see list of password
