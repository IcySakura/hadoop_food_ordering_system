from json_parser import *
from restaurant import restaurant
from order import order
from confirmation import confirmation

data_dir = "../data/"

def run_eample_one():
    #example 1: simulate json passed as string:
    
    #Step 1) Load json file as dict:
    example_restaurant_json_path = data_dir + "restaurant_json/resaurant_id_1_in_n_out.json"
    data_as_dict = load_json_file_as_dict(example_restaurant_json_path)

    #Step 2) *Optional* Check dict is correct structure/ has all necessary keys:

    #Step 3) Convert Dict to string:
    data_as_str = dict_to_string(data_as_dict)

    #Step 4) *Optional* pass data as string (for example, on std.out)

    #Step 5) Create dict from string:
    data_recieved_as_dict = string_to_dict(data_as_str)

    #Step 6) *Optional* Check dict recieved is correct structure/ has all necessary keys:

    #Step 7) *Optional* Use this dict for processing

    #Step 8) Write dict of json to json file:
    example_restraunt_json_output_path = data_dir + "restaurant_json/sample_output.json"
    write_dict_to_json_file(data_recieved_as_dict, example_restraunt_json_output_path)

def run_eample_two():
    #example 2: load json file of restraunt as restraunt class object, edit data, and write back to json file

    #Step 1) Load json file as dict:
    example_restaurant_json_path = data_dir + "restaurant_json/resaurant_id_1_in_n_out.json"
    data_as_dict = load_json_file_as_dict(example_restaurant_json_path)

    #Step 2) Create restraunt object and read in dict:
    sample_restaurant = restaurant(data_as_dict)

    #Step 3) *optional* update restraunt data:

    #Step 4) Write restraunt to json file:
    sample_restaurant_dict = sample_restaurant.convert_to_dict()

    example_restraunt_json_output_path = data_dir + "restaurant_json/sample_restaurant_output.json"
    write_dict_to_json_file(sample_restaurant_dict, example_restraunt_json_output_path)

def run_eample_three():
    #example 3: load json file of order as order class object, edit data, and write back to json file

    #Step 1) Load json file as dict:
    example_order_json_path = data_dir + "order_json/order_id_1.json"
    data_as_dict = load_json_file_as_dict(example_order_json_path)

    #Step 2) Create restraunt object and read in dict:
    sample_order = order(data_as_dict)

    #Step 3) *optional* update restraunt data:

    #Step 4) Write restraunt to json file:
    sample_order_dict = sample_order.convert_to_dict()
    ##json_pretty_print(sample_order_dict)

    example_order_json_output_path = data_dir + "order_json/sample_order_output.json"
    write_dict_to_json_file(sample_order_dict, example_order_json_output_path)

def run_eample_four():
    #example 4: load json file of confirmation as confirmation class object, edit data, and write back to json file

    #Step 1) Load json file as dict:
    example_confirmation_path = data_dir + "confirmation_json/order_id_1_confirmation.json"
    data_as_dict = load_json_file_as_dict(example_confirmation_path)

    #Step 2) Create restraunt object and read in dict:
    sample_confirmation = confirmation(data_as_dict)

    #Step 3) *optional* update restraunt data:

    #Step 4) Write restraunt to json file:
    sample_confirmation_dict = sample_confirmation.convert_to_dict()
    json_pretty_print(sample_confirmation_dict)

    example_confirmation_json_output_path = data_dir + "confirmation_json/sample_confirmation_output.json"
    write_dict_to_json_file(sample_confirmation_dict, example_confirmation_json_output_path)

def run_test_location():
    #Step 1) Load restaurant:
    example_restaurant_json_path = data_dir + "restaurant_json/resaurant_id_1_in_n_out.json"
    data_as_dict = load_json_file_as_dict(example_restaurant_json_path)
    sample_restaurant = restaurant(data_as_dict)

    #Step 2) Load order:
    example_order_json_path = data_dir + "order_json/order_id_1.json"
    data_as_dict = load_json_file_as_dict(example_order_json_path)
    sample_order = order(data_as_dict)

    #Step 3) Calculate distance:
    sample_restaurant_location = sample_restaurant.info.location
    sample_order_location = sample_order.info.location
    distance = sample_order_location.caluclate_distance_to_location(sample_restaurant_location)
    print("Distance = {}".format(distance))
    
if __name__ == "__main__":
    #run_eample_one()
    #run_eample_two()
    #run_eample_three()
    #run_eample_four()
    run_test_location()
