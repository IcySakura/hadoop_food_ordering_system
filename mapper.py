#!/usr/bin/env python3
"""mapper.py"""

import sys

sys.path.append('./json_module')
sys.path.append('./mysql_module')

from json_parser import *
from restaurant import restaurant
from order import order
from location import *
from mysql_module_lib import *

current_order = None
current_order_items = []
current_restaurant = None
parent_dir = "./"
current_json_path = ""

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace

    line = line.strip()
    json_file_paths = line.split()

    for json_file_path in json_file_paths:
        current_json_path = parent_dir + json_file_path
        data_as_dict = load_json_file_as_dict(current_json_path)

        if current_order is None:
            current_order = order(data_as_dict)
            current_order_needed_capacity = 0
            for m_item in current_order.order_items:
                current_order_items.append(m_item.name)
                current_order_needed_capacity += m_item.quantity    # each item should have different prep capacity
            new_order(current_order.order_id, current_order.customer_id, current_order_needed_capacity)
            print(current_json_path)
        else:
            current_restaurant = restaurant(data_as_dict)

            # Check if restaurant is within range
            distance_between_each_other = \
                calculate_distance_in_km_between_coords(\
                    current_order.info.location.lat, current_order.info.location.lon, \
                    current_restaurant.info.location.lat, current_restaurant.info.location.lon)
            # print("distance_between is:", distance_between_each_other.km)
            if distance_between_each_other > current_order.max_distance:
                continue

            # Check if restaurant can fulfill the order
            current_restaurant_items = [m_item.name for m_item in current_restaurant.menu_items]
            if not all(m_item in current_restaurant_items for m_item in current_order_items):
                continue
            print(current_json_path, end=' ')