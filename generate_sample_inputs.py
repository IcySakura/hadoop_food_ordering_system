import sys, os

sample_inputs_path = "./sample_inputs.txt"

restaurants_json_dir = ""
orders_json_dir = ""

list_of_restaurants_json_paths = []
list_of_orders_json_paths = []

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("required parameter: [location_for_restaurants] [location_for_orders] [num_of_orders_want_use]")
        exit()

    restaurants_json_dir = sys.argv[1] + "/"
    orders_json_dir = sys.argv[2] + "/"

    list_of_restaurants_json_paths.extend([restaurants_json_dir + file_name for file_name in os.listdir(restaurants_json_dir)])
    # list_of_restaurants_json_paths.sort()
    # print(" ".join(list_of_restaurants_json_paths))

    list_of_orders_json_paths.extend(os.listdir(orders_json_dir))
    list_of_orders_json_paths = [orders_json_dir + file_name for file_name in sorted(list_of_orders_json_paths)]
    # print(list_of_orders_json_paths)

    sample_inputs_file = open(sample_inputs_path, "w")

    for i in range(int(sys.argv[3])):
        sample_inputs_file.write(list_of_orders_json_paths[i])
        sample_inputs_file.write("\n")
        sample_inputs_file.write(" ".join(list_of_restaurants_json_paths))
        sample_inputs_file.write("\n")
    
    sample_inputs_file.close()

    
    