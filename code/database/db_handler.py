import sqlite3
import atexit

conn = sqlite3.connect('proto-base.db')

c = conn.cursor()

def exit_handler(): # closes database upon termination
    conn.close()
atexit.register(exit_handler)

# c.execute("""CREATE TABLE test (
#           id INTEGER PRIMARY KEY,
#           name TEXT,
#           heat INTEGER,
#           date DATE,
#           time TIME,
#           weight FLOAT
#           );""")

def insert_new_food(name, heat, date, time, weight):
  with conn: # Commits the change to the database
    c.execute("""INSERT INTO test (name, heat, date, 
              time, weight) VALUES (?, ?, ?, ?, ?);""",
              (name, heat, date, time, weight))

def get_food_info(name):
  c.execute("SELECT * FROM test WHERE name=:name", {'name': name})
  return c.fetchall()

def get_table():
  c.execute("SELECT * FROM test;")
  return c.fetchall()

# insert_new_food("pizza", 65, '2018-06-23', '09:10:00', 12)