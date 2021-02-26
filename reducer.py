#!/usr/bin/env python3
"""reducer.py"""

import sys

sys.path.append('./json_module')
sys.path.append('./mysql_module')

from json_parser import *
from restaurant import restaurant
from order import order

current_order = None
current_restaurant = None
parent_dir = "./"
current_json_path = ""
confirmation_json_path = ""

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
        else:
            current_restaurant = restaurant(data_as_dict)

# TO-DO: add logic to generate and print the path of confirmation json

if not confirmation_json_path:
    print("error", end='')
else:
    print(confirmation_json_path, end='')