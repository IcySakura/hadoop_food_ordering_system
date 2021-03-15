from mysql_config import *
from mysql_module_lib import *
import sys

sys.path.append('../json_module')
from json_parser import *
from restaurant import restaurant

from os import walk

if __name__ == "__main__":

  if len(sys.argv) < 2:
    print("required parameter: [path_of_restaurant_json_files]")
    exit()

  mydb = mysql.connector.connect(
    host="localhost",
    user=MYSQL_USERNAME,
    password=MYSQL_PASSWORD
  )

  mycursor = mydb.cursor()

  try:
    mycursor.execute("CREATE DATABASE " + MYSQL_DATABASE_NAME)
  except mysql.connector.errors.DatabaseError as e:
    print("[Warning] Database: " + MYSQL_DATABASE_NAME + " probably already exist")

  # mycursor.execute("SHOW DATABASES")

  # print("Existing databases:")
  # for x in mycursor:
  #   print(x)

  mycursor.execute("USE " + MYSQL_DATABASE_NAME)

  try:
    mycursor.execute("CREATE TABLE orders (order_id VARCHAR(255) NOT NULL PRIMARY KEY, customer_id VARCHAR(255), restaurant_id INT, needed_capacity INT, start_timestamp VARCHAR(255), estimated_finish_timestamp VARCHAR(255), actual_finish_timestamp VARCHAR(255), order_status INT)")
  except mysql.connector.errors.ProgrammingError as e:
    print("[Warning] Table: orders probably already exist")  
  '''
  order_status: 0 means created but no restaurant assigned yet, 1 means restaurant assigned and order is being prepared, 2 means restaurant has finished preparing
  '''

  try:
    mycursor.execute("CREATE TABLE restaurants (restaurant_id VARCHAR(255) NOT NULL PRIMARY KEY, max_capacity INT, current_capacity INT)")
  except mysql.connector.errors.ProgrammingError as e:
    print("[Warning] Table: restaurants probably already exist")


  # Delete everything from tables
  mycursor.execute("TRUNCATE orders")
  mycursor.execute("TRUNCATE restaurants")

  # Load all restaurants
  for (dirpath, dirnames, filenames) in walk(sys.argv[1]):
    for filename in filenames:
      data_as_dict = load_json_file_as_dict(dirpath + filename)
      current_restaurant = restaurant(data_as_dict)
      sql = "INSERT INTO restaurants (restaurant_id, max_capacity, current_capacity) VALUES (%s, %s, %s)"
      val = (current_restaurant.id, current_restaurant.max_capacity, current_restaurant.max_capacity)
      mycursor.execute(sql, val)
      print("[INFO] Table: inserting restaurant with id:", current_restaurant.id)

  mydb.commit()


  mycursor.execute("SHOW TABLES")

  # print("Existing tables:")
  for x in mycursor:
    print(x)
  
  show_table("restaurants")

