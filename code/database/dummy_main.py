import db_handler
from datetime import datetime
import random
import time

def main():
  print(db_handler.get_table())
  for i in range(25):
    now = datetime.now()
    db_handler.insert_new_food(random_food(), random.randint(40, 100), 
                                now.strftime("%Y-%m-%d"), 
                                now.strftime("%H:%M:%S"), 
                                round(random.uniform(.25, 5.5), 3))
    time.sleep(2)
  db_handler.display_table()

def random_food():
  foods = ["hot dog", "pizza", "burger", "french fries", "lettuce",
           "corn", "pasta", "macaroni and cheese", "chicken",
           "breaded chicken", "yogurt", "omelette", "sandwich",
            "cereal", "drink", "pork chop", "fruit"]
  return random.choice(foods)

if __name__ == "__main__":
  main()