from json_parser import *
from restaurant import restaurant
from order import order, construct_order_object
from confirmation import confirmation
from wait_time import calculate_approximate_wait_time_and_number_of_cooks_occupied, calculate_static_prep_time, calculate_driving_time

from constants import MENU_ITEM_NAME_KEY, MENU_ITEM_ID_KEY, MENU_ITEM_QUANTITY_KEY


def run_eample_one():
    #example 1: simulate json passed as string:
    
    #Step 1) Load json file as dict:
    example_restaurant_json_path = "../restaurant_json/resaurant_id_1_in_n_out.json"
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
    example_restraunt_json_output_path = "../restaurant_json/sample_output.json"
    write_dict_to_json_file(data_recieved_as_dict, example_restraunt_json_output_path)

def run_eample_two():
    #example 2: load json file of restraunt as restraunt class object, edit data, and write back to json file

    #Step 1) Load json file as dict:
    example_restaurant_json_path = "../restaurant_json/resaurant_id_1_in_n_out.json"
    data_as_dict = load_json_file_as_dict(example_restaurant_json_path)

    #Step 2) Create restraunt object and read in dict:
    sample_restaurant = restaurant(data_as_dict)

    #Step 3) *optional* update restraunt data:

    #Step 4) Write restraunt to json file:
    sample_restaurant_dict = sample_restaurant.convert_to_dict()

    example_restraunt_json_output_path = "../restaurant_json/sample_restaurant_output.json"
    write_dict_to_json_file(sample_restaurant_dict, example_restraunt_json_output_path)

def run_eample_three():
    #example 3: load json file of order as order class object, edit data, and write back to json file

    #Step 1) Load json file as dict:
    example_order_json_path = "../order_json/order_id_1.json"
    data_as_dict = load_json_file_as_dict(example_order_json_path)

    #Step 2) Create restraunt object and read in dict:
    sample_order = order(data_as_dict)

    #Step 3) *optional* update restraunt data:

    #Step 4) Write restraunt to json file:
    sample_order_dict = sample_order.convert_to_dict()
    ##json_pretty_print(sample_order_dict)

    example_order_json_output_path = "../order_json/sample_order_output.json"
    write_dict_to_json_file(sample_order_dict, example_order_json_output_path)

def run_eample_four():
    #example 4: load json file of confirmation as confirmation class object, edit data, and write back to json file

    #Step 1) Load json file as dict:
    example_confirmation_path = "../confirmation_json/order_id_1_confirmation.json"
    data_as_dict = load_json_file_as_dict(example_confirmation_path)

    #Step 2) Create restraunt object and read in dict:
    sample_confirmation = confirmation(data_as_dict)

    #Step 3) *optional* update restraunt data:

    #Step 4) Write restraunt to json file:
    sample_confirmation_dict = sample_confirmation.convert_to_dict()
    json_pretty_print(sample_confirmation_dict)

    example_confirmation_json_output_path = "../confirmation_json/sample_confirmation_output.json"
    write_dict_to_json_file(sample_confirmation_dict, example_confirmation_json_output_path)

def run_test_location():
    #Step 1) Load restaurant:
    example_restaurant_json_path = "../restaurant_json/resaurant_id_1_in_n_out.json"
    data_as_dict = load_json_file_as_dict(example_restaurant_json_path)
    sample_restaurant = restaurant(data_as_dict)

    #Step 2) Load order:
    example_order_json_path = "../order_json/order_id_1.json"
    data_as_dict = load_json_file_as_dict(example_order_json_path)
    sample_order = order(data_as_dict)

    #Step 3) Calculate distance:
    sample_restaurant_location = sample_restaurant.info.location
    sample_order_location = sample_order.info.location
    distance = sample_order_location.caluclate_distance_to_location(sample_restaurant_location)
    print("Distance = {}".format(distance))

def run_example_order_generation():
    #Step 1) Construct a dict (like this) for each item you want to order:
    sample_order_item_1 = {MENU_ITEM_NAME_KEY: "hamburger",
                          MENU_ITEM_ID_KEY: "1",
                          MENU_ITEM_QUANTITY_KEY: "1"}
    sample_order_item_2 = {MENU_ITEM_NAME_KEY: "fries",
                          MENU_ITEM_ID_KEY: "2",
                          MENU_ITEM_QUANTITY_KEY: "1"}

    #Step 2) Place in a list:
    sample_order_items = [sample_order_item_1, sample_order_item_2]

    #Step 3) Construct order using this function:
    ##NOTE: there are additional params, but by default it will randomly generate them
    order_object = construct_order_object(sample_order_items)

    #Step 4) *optional* print json object:
    json_pretty_print(order_object.convert_to_dict())


def run_example_wait_time():
    print("Make sure you have downloaded the google maps key file and 'PATH_TO_GOOGLE_MAPS_KEY' is correct")
    #Step 1) Load order:
    example_order_json_path = "../order_json/order_id_1.json"
    data_as_dict = load_json_file_as_dict(example_order_json_path)
    sample_order = order(data_as_dict)

    #Step 2)Load (corresponding) restraunt:
    example_restaurant_json_path = "../restaurant_json/resaurant_id_1_in_n_out.json"
    data_as_dict = load_json_file_as_dict(example_restaurant_json_path)
    sample_restaurant = restaurant(data_as_dict)

    #Step 3) *Optional* Print out info about order and restraunt:
    (prep_time,_) = calculate_static_prep_time(sample_restaurant.max_capacity, sample_order.count_number_of_order_items())
    drive_time = calculate_driving_time(sample_order.info.location,sample_restaurant.info.location)
    print("Prep time (using max_capacity) = {} mins\nCurrent Drive Time = {} mins\n".format(prep_time,drive_time))

    #Step 4)Calaculate wait time using max_capacity:
    (wait_time, estimated_number_of_cooks_occupied_by_task) = calculate_approximate_wait_time_and_number_of_cooks_occupied(sample_order, sample_restaurant, current_capacity=0, use_current_capacity=False)
    print("At max capacity, the wait time will be {} mins [max(prep_time,drive_time)]. The number of cooks needed is ~{}\n".format(wait_time, estimated_number_of_cooks_occupied_by_task))

    #Step 5) *optional* use current capcity to calculate wait time:
    current_capcity = 1
    (wait_time, estimated_number_of_cooks_occupied_by_task) = calculate_approximate_wait_time_and_number_of_cooks_occupied(sample_order, sample_restaurant, current_capacity=current_capcity, use_current_capacity=True)
    print("At current capacity of {}, the wait time will be ~{} mins. The number of cooks needed is ~{}\n".format(current_capcity,wait_time, estimated_number_of_cooks_occupied_by_task))

    
if __name__ == "__main__":
    #run_eample_one()
    #run_eample_two()
    #run_eample_three()
    #run_eample_four()
    #run_test_location()
    #run_example_order_generation()
    run_example_wait_time()
