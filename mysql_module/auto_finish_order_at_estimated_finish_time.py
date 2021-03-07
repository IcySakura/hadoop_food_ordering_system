import sys
from mysql_module_lib import *
from datetime import datetime
import time

if __name__ == "__main__":
    while True:
        mycursor.execute("SELECT * FROM orders")
        myresult = mycursor.fetchall()
        for order_info in myresult:
            if order_info[7] == 1 and datetime.strptime(order_info[5], '%d/%m/%Y %H:%M:%S') < datetime.now():
                update_order_with_finish(order_info[0])
                update_restaurant_current_capacity(order_info[2], get_restaurant_info(order_info[2])[2] + order_info[3])
                print("order", order_info[0], "has been marked as finish and its assigned restaurant", order_info[2], "now has increased current capacity...")
        time.sleep(1)

