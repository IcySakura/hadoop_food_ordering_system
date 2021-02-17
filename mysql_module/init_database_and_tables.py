from mysql_config import *

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

mycursor.execute("SHOW DATABASES")

# print("Existing databases:")
# for x in mycursor:
#   print(x)

mycursor.execute("USE " + MYSQL_DATABASE_NAME)

mycursor.execute("CREATE TABLE order (order_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")

# print("Existing tables:")
for x in mycursor:
  print(x)

