import os
from restaurant import restaurant
from json_parser import *
from collections import defaultdict

def create_all_restraunts_from_json_files_in_folder(path_to_folder):
    list_of_restraunts = []
    json_files = [os.path.join(path_to_folder, pos_json) for pos_json in os.listdir(path_to_folder) if pos_json.endswith('.json')]

    for each_json_file in json_files:
        each_restraunt = restaurant(load_json_file_as_dict(each_json_file))
        if each_restraunt.has_menu_items:
            list_of_restraunts.append(each_restraunt)

    return list_of_restraunts

def create_map_of_menu_items(list_of_restraunts):
    menu_item_id_to_restraunt_id = defaultdict(list)
    restraunt_id_to_menu_item_id = defaultdict(list)
    menu_item_dict = dict()
    restraunt_id_dict = dict()

    for each_restraunt in list_of_restraunts:
        if each_restraunt.has_id():
            if each_restraunt.id not in restraunt_id_dict:
                restraunt_id_dict[each_restraunt.id] = each_restraunt
            else:
                print("Error: duplicate restraunt_id encountered: id # = {}, name = {}".format(each_restraunt.id,each_restraunt.info.name))

            for each_item in each_restraunt.menu_items:
                if each_item.id not in menu_item_dict:
                    menu_item_dict[each_item.id] = each_item
                elif each_item.name != menu_item_dict[each_item.id].name:
                    print("Error: duplicate menu_id encountered: id # = {}, name = {}".format(each_item.id,each_item.name)) #here

                if each_item.id not in menu_item_id_to_restraunt_id or each_restraunt.id not in menu_item_id_to_restraunt_id[each_item.id]:
                    menu_item_id_to_restraunt_id[each_item.id].append(each_restraunt.id)
                if each_restraunt.id not in restraunt_id_to_menu_item_id or each_item.id not in restraunt_id_to_menu_item_id[each_restraunt.id]:
                    restraunt_id_to_menu_item_id[each_restraunt.id].append(each_item.id)

    return (menu_item_id_to_restraunt_id, restraunt_id_to_menu_item_id, menu_item_dict,restraunt_id_dict)



if __name__ == "__main__":
    PATH_TO_FOLDER = "C:\\Users\\wills\\Desktop\\hadoop_food_ordering_system\\restaurant_json"
    list_of_restraunts = create_all_restraunts_from_json_files_in_folder(PATH_TO_FOLDER)
    (menu_item_id_to_restraunt_id, restraunt_id_to_menu_item_id, menu_item_dict,restraunt_id_dict) = create_map_of_menu_items(list_of_restraunts)
