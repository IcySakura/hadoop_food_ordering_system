from mysql_module_lib import *

if __name__ == "__main__":
    new_order(1, 1, 10)
    update_order_with_restaurant_assignment(1, 1, 600)
    update_order_with_finish(1)
    print(get_order_info(1))
    # show_table("orders")
    new_restaurant(1, 60)
    update_restaurant_current_capacity(1, 30)
    print(get_restaurant_info(1))
    # show_table("restaurants")