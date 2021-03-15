from mysql_config import *
from datetime import datetime
from datetime import timedelta

mydb = mysql.connector.connect(
  host="localhost",
  user=MYSQL_USERNAME,
  password=MYSQL_PASSWORD,
  database="cs230_food_ordering_system"
)
mycursor = mydb.cursor()

def show_table(table_name: str):
  mycursor.execute("SELECT * FROM " + table_name)
  myresult = mycursor.fetchall()
  print("===========================================Start printing table: " + table_name + " ===========================================")
  for x in myresult:
    print(x)
  print("===========================================End printing table: " + table_name + " ===========================================")

def new_order(order_id: str, customer_id: str, needed_capacity: int):
  current_timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  sql = "INSERT INTO orders (order_id, customer_id, needed_capacity, start_timestamp, order_status) VALUES (%s, %s, %s, %s, %s)"
  val = (order_id, customer_id, needed_capacity, current_timestamp, 0)
  mycursor.execute(sql, val)
  mydb.commit()

def update_order_with_restaurant_assignment(order_id: str, restaurant_id: int, estimated_prepare_time_in_sec: int):
  estimated_finish_timestamp = (datetime.now() + timedelta(seconds=estimated_prepare_time_in_sec)).strftime("%d/%m/%Y %H:%M:%S")
  sql = "UPDATE orders SET restaurant_id = %s, estimated_finish_timestamp = %s, order_status = 1 WHERE order_id = %s"
  val = (restaurant_id, estimated_finish_timestamp, order_id)
  mycursor.execute(sql, val)
  mydb.commit()

def update_order_with_finish(order_id: str):
  current_timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  sql = "UPDATE orders SET actual_finish_timestamp = %s, order_status = 2 WHERE order_id = %s"
  val = (current_timestamp, order_id)
  mycursor.execute(sql, val)
  mydb.commit()

def get_order_info(order_id: str):
  # print("get_order_info: order_id is:", order_id)
  # mycursor.execute("SELECT * FROM orders WHERE order_id = " + order_id)
  sql = "SELECT * FROM orders WHERE order_id = %s"
  val = (order_id, )
  mycursor.execute(sql, val)
  myresult = mycursor.fetchall()
  return myresult[0]

def new_restaurant(restaurant_id: int, max_capacity: int):
  sql = "INSERT INTO restaurants (restaurant_id, max_capacity, current_capacity) VALUES (%s, %s, %s)"
  val = (restaurant_id, max_capacity, max_capacity)
  mycursor.execute(sql, val)
  mydb.commit()

def update_restaurant_current_capacity(restaurant_id: int, new_current_capacity: int):
  sql = "UPDATE restaurants SET current_capacity = %s WHERE restaurant_id = %s"
  val = (new_current_capacity, restaurant_id)
  mycursor.execute(sql, val)
  mydb.commit()

def get_restaurant_info(restaurant_id: int):
  mycursor.execute("SELECT * FROM restaurants WHERE restaurant_id = " + str(restaurant_id))
  myresult = mycursor.fetchall()
  return myresult[0]
