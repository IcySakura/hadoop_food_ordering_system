import sys
from json_parser import *
from restaurant import restaurant, generate_random_restraunt
from aggregator import create_all_restraunts_from_json_files_in_folder, create_map_of_menu_items

data_dir = ""

def run_sample_rest_generation(path_to_store):
    #Step 1) Load all restraunt and order details
    PATH_TO_FOLDER = "../data/restaurant_json" #update this path to be path to restraunt json folder
    list_of_restraunts = create_all_restraunts_from_json_files_in_folder(PATH_TO_FOLDER)
    (menu_item_id_to_restraunt_id, restraunt_id_to_menu_item_id, menu_item_dict,restraunt_id_dict) = create_map_of_menu_items(list_of_restraunts)

    #Step 2) Specify max number of dishes to serve at generated rest. and capacity
    MAX_NUMBER_OF_DISHES = 5
    MIN_CAPACITY = 1
    MAX_CAPACITY = 10

    #Step 3) Generate rest.
    generate_rest = generate_random_restraunt(menu_item_dict,max_number_of_dishes=MAX_NUMBER_OF_DISHES,min_capacity=MIN_CAPACITY,max_capacity=MAX_CAPACITY)

    #Step 4) *optional* print rest.
    write_dict_to_json_file(generate_rest.convert_to_dict(), path_to_store)
    # json_pretty_print(generate_rest.convert_to_dict())

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("required parameter: [location_for_storing_generated_restaurants] [num_of_restaurants_to_generate]")
        exit()
    
    data_dir = sys.argv[1]
    for i in range(int(sys.argv[2])):
        path_of_new_restaurant_json = data_dir + "/" + str(i) + ".json"
        run_sample_rest_generation(path_of_new_restaurant_json)
    print(sys.argv[2], "restaurants have been generated under directory:", sys.argv[1])
