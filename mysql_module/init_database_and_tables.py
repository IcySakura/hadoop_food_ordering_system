from mysql_config import *

if __name__ == "__main__":
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
    mycursor.execute("CREATE TABLE orders (order_id INT NOT NULL PRIMARY KEY, customer_id INT, restaurant_id INT, needed_capacity INT, start_timestamp VARCHAR(255), estimated_finish_timestamp VARCHAR(255), actual_finish_timestamp VARCHAR(255), order_status INT)")
  except mysql.connector.errors.ProgrammingError as e:
    print("[Warning] Table: orders probably already exist")  
  '''
  order_status: 0 means created but no restaurant assigned yet, 1 means restaurant assigned and order is being prepared, 2 means restaurant has finished preparing
  '''

  try:
    mycursor.execute("CREATE TABLE restaurants (restaurant_id INT NOT NULL PRIMARY KEY, max_capacity INT, current_capacity INT)")
  except mysql.connector.errors.ProgrammingError as e:
    print("[Warning] Table: restaurants probably already exist")


  # Delete everything from tables
  mycursor.execute("TRUNCATE orders")
  mycursor.execute("TRUNCATE restaurants")

  mycursor.execute("SHOW TABLES")

  # print("Existing tables:")
  for x in mycursor:
    print(x)

