from json_parser import *
from restaurant import restaurant

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

if __name__ == "__main__":
    #run_eample_one()
    run_eample_two()
