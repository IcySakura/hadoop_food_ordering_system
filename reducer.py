#!/usr/bin/env python3
"""reducer.py"""

import sys

sys.path.append('./json_module')
sys.path.append('./mysql_module')

from json_parser import *
from restaurant import restaurant
from order import order
from mysql_module_lib import *
from wait_time import calculate_approximate_wait_time_and_number_of_cooks_occupied, calculate_static_prep_time, calculate_driving_time
import time

current_order = None
current_order_info = None
current_restaurant = None
current_lowest_waiting_time = 999999999999
current_lowest_waiting_time_restaurant = None
parent_dir = "./"
current_json_path = ""
confirmation_json_path = parent_dir + "data/confirmation_json/"

eval_log_path = "eval_use/reducer.log"

eval_file = open(eval_log_path, "a")

def write_current_time_to_eval_file():
    eval_file.write(str(time.perf_counter()))
    eval_file.write("\n")

def get_estimated_waiting_time(order_info, restaurant_id):
    result = 5 * 60  # Base time of 5 mins
    restaurant_info = get_restaurant_info(restaurant_id)
    if restaurant_info[2] >= order_info[3]:
        result += 2 * 60    # Asuming each item will cost 2 mins; here all capacity can be used...
        return result
    estimated_remaining_capacity = restaurant_info[2]
    estimated_remaining_items = order_info[3]
    if restaurant_info[2] > 0:
        result += 2 * 60    # Asuming each item will cost 2 mins; here all remaining capacity can be used...
        estimated_remaining_items -= estimated_remaining_capacity
        estimated_remaining_capacity = 0
    estimated_remaining_capacity -= estimated_remaining_items
    if estimated_remaining_capacity < 0:
        result -= estimated_remaining_capacity * 2 * 60 # Assuming restaurant can restore 1 capacity per 2 mins
        result += estimated_remaining_items * 2 * 60    # Asumming each item will cost 2 mins
    return result

def confirm_order_with_current_lowest_waiting_time_restaurant():
    update_restaurant_current_capacity(current_lowest_waiting_time_restaurant.id, get_restaurant_info(current_lowest_waiting_time_restaurant.id)[2] - current_order_info[3])
    update_order_with_restaurant_assignment(current_order_info[0], current_lowest_waiting_time_restaurant.id, current_lowest_waiting_time)

    new_confirmation_dict = {"order_id": current_order_info[0], "customer_id": current_order_info[1], "restaurant_id": current_lowest_waiting_time_restaurant.id, "estimated_finish_time": current_lowest_waiting_time}
    new_confirmation_json_path = confirmation_json_path + "order_id_" + str(current_order_info[0]) + "_confirmation.json"
    write_dict_to_json_file(new_confirmation_dict, new_confirmation_json_path)
    print(new_confirmation_json_path, end=' ')
    write_current_time_to_eval_file()

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace

    line = line.strip()
    json_file_paths = line.split()

    for json_file_path in json_file_paths:
        current_json_path = parent_dir + json_file_path
        data_as_dict = load_json_file_as_dict(current_json_path)

        if "order_id" in data_as_dict.keys():
            if current_order is not None:
                if current_restaurant is None:
                    print("[Error]: No restaurant can fulfill the order:", current_order.order_id)
                    exit()
                confirm_order_with_current_lowest_waiting_time_restaurant()
                current_restaurant = None
                current_lowest_waiting_time = 999999999999

            current_order = order(data_as_dict)
            current_order_info = get_order_info(current_order.order_id)
            # print("New Order coming in:", current_order.order_id)
        else:
            current_restaurant = restaurant(data_as_dict)
            # print("New Restaurant coming in:", current_restaurant.id)
            current_restaurant_estimated_waiting_time = get_estimated_waiting_time(current_order_info, current_restaurant.id)
            current_restaurant_estimated_drive_time = calculate_driving_time(current_order.info.location, current_restaurant.info.location) * 60
            # print("current_restaurant_estimated_waiting_time:", current_restaurant_estimated_waiting_time, ", current_restaurant_estimated_drive_time:", current_restaurant_estimated_drive_time)
            current_restaurant_estimated_waiting_time = max(current_restaurant_estimated_waiting_time, current_restaurant_estimated_drive_time)
            if current_lowest_waiting_time > current_restaurant_estimated_waiting_time:
                current_lowest_waiting_time = current_restaurant_estimated_waiting_time
                current_lowest_waiting_time_restaurant = current_restaurant

# TO-DO: Make some backup restaurants options...

confirm_order_with_current_lowest_waiting_time_restaurant()

# if not confirmation_json_path:
#     print("error", end='')
# else:
#     print(confirmation_json_path, end='')