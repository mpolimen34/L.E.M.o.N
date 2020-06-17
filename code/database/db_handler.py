import sqlite3

conn = sqlite3.connect('test-base.db')

c = conn.cursor()

# c.execute("""CREATE TABLE test (
#           name text,
#           heat integer
#           )""")

def insert_new_food(name, temp):
  with conn: # Commits the change to the database
    c.execute("INSERT INTO test VALUES (:name, :heat)", {'name': name, 'heat': temp})

def get_food_info(name):
  c.execute("SELECT * FROM test WHERE name=:name", {'name': name})
  return c.fetchall()

conn.close()