import sqlite3


conn = sqlite3.connect('example.db' , check_same_thread=False)
curs = conn.cursor()


