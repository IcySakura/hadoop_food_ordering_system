import sys
from json_parser import *
from order import order, construct_order_object, create_random_order
from aggregator import create_all_restraunts_from_json_files_in_folder, create_map_of_menu_items

data_dir = ""

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

def run_generate_random_order(path_to_store):
    '''generate a random order (that can be fufilled by atleast one restraunt)'''
    #Step 1) Load all restraunt and order details
    PATH_TO_FOLDER = "../data/restaurant_json" #update this path to be path to restraunt json folder
    list_of_restraunts = create_all_restraunts_from_json_files_in_folder(PATH_TO_FOLDER)
    (menu_item_id_to_restraunt_id, restraunt_id_to_menu_item_id, menu_item_dict,restraunt_id_dict) = create_map_of_menu_items(list_of_restraunts)
    ##  Note: this will only be needed to be done once, even if creating multiple random orders

    #Step 2) Pick max number of dishes and max quantity:
    max_number_of_unique_dishes_to_order = 3
    max_quantity_per_dish = 3

    #Step 3) Generate random order:
    order = create_random_order(menu_item_id_to_restraunt_id, restraunt_id_to_menu_item_id, menu_item_dict,restraunt_id_dict,max_number_of_unique_dishes_to_order=max_number_of_unique_dishes_to_order, max_quantity_per_dish=max_quantity_per_dish)

    #Step 4) *optional* print order
    write_dict_to_json_file(order.convert_to_dict(), path_to_store)
    # print("random order:")
    # print(json_pretty_print(order.convert_to_dict()))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("required parameter: [location_for_storing_generated_orders] [num_of_orders_to_generate]")
        exit()
    
    data_dir = sys.argv[1]
    for i in range(int(sys.argv[2])):
        path_of_new_order_json = data_dir + "/" + str(i) + ".json"
        run_generate_random_order(path_of_new_order_json)
    print(sys.argv[2], "orders have been generated under directory:", sys.argv[1])
