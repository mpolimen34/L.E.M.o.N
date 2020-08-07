import mysql.connector
import atexit
#import data_display

mydb = mysql.connector.connect(
  host="155.246.80.48",
  user="lemon-team",
  password="lemon-team",
  database="lemon"
)

# print(mydb)

c = mydb.cursor()

def exit_handler(): # closes database upon termination
    conn.close()
atexit.register(exit_handler)

# c.execute("""CREATE TABLE food (
#           id INTEGER PRIMARY KEY,
#           name TEXT,
#           date DATE,
#           time TIME
#           );""")

def insert_new_food(name, heat, date, time, weight):
  with conn: # Commits the change to the database
    c.execute("""INSERT INTO food (name, heat, date, 
              time, weight) VALUES (?, ?, ?, ?, ?);""",
              (name, heat, date, time, weight))

def get_food_info(name):
  c.execute("SELECT * FROM food WHERE name=:name", {'name': name})
  return c.fetchall()

def get_table():
  c.execute("SELECT * FROM food;")
  return c.fetchall()

#def display_table():
# data_display.display()

# insert_new_food("pizza", 65, '2018-06-23', '09:10:00', 12)
# with conn:
#   c.execute("DELETE from test WHERE id=2;")
