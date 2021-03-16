from constants import RESTAUARNT_ID_KEY, RESTAURANT_INFO_KEY, RESTAURANT_MAX_CAPACITY_KEY, RESTAURANT_MENU_KEY
from constants import INFO_NAME_KEY, INFO_PHONE_KEY, INFO_LOCATION_KEY
from constants import LOCATION_LAT_KEY, LOCATION_LON_KEY

from info import info
from menu_item import menu_item

from generator import generate_unique_id, generate_customer_name, generate_location, generate_phone_number, generate_rest_name

from random import choice, sample, randrange

#TODO: add type checking, conversion to correct type

class restaurant:
    def __init__(self,restaurant_dict=dict()):
        self.id = ""
        self.info = info()
        self.max_capacity = 0
        self.menu_items = []

        if len(restaurant_dict) != 0:
            self.load_restaurant_from_dict(restaurant_dict)

    def has_menu_items(self):
        return len(self.menu_items) > 0

    def has_id(self):
        return isinstance(self.id,str) and len(self.id) > 0 or self.id >= 0

    def load_restaurant_from_dict(self, restaurant_dict):
        if RESTAUARNT_ID_KEY in restaurant_dict:
            self.id = restaurant_dict[RESTAUARNT_ID_KEY]

        if RESTAURANT_INFO_KEY in restaurant_dict:
            self.info.load_info_from_dict(restaurant_dict[RESTAURANT_INFO_KEY])

        if RESTAURANT_MAX_CAPACITY_KEY in restaurant_dict:
            self.max_capacity = int(restaurant_dict[RESTAURANT_MAX_CAPACITY_KEY])

        if RESTAURANT_MENU_KEY in restaurant_dict:
            for each_item in restaurant_dict[RESTAURANT_MENU_KEY]:
                self.menu_items.append(menu_item(each_item))

    def convert_to_dict(self):
        to_return = dict()
        to_return[RESTAUARNT_ID_KEY] = self.id
        to_return[RESTAURANT_INFO_KEY] = self.info.convert_to_dict()
        to_return[RESTAURANT_MAX_CAPACITY_KEY] = str(self.max_capacity)

        menu_item_dict_list = []
        for each_item in self.menu_items:
            menu_item_dict_list.append(each_item.convert_to_dict())
        to_return[RESTAURANT_MENU_KEY] = menu_item_dict_list
        return to_return

    
def generate_random_restraunt(menu_item_dict,max_number_of_dishes=10,min_capacity=1,max_capacity=10):
    location_dict = {}
    info_dict = {}
    dictionary_to_construct_rest = {}
    menu_items = []

   
    rest_id = generate_unique_id()
    rest_name = generate_rest_name()
    rest_phone = generate_phone_number()
    rest_coord = generate_location()


    dish_list = list(menu_item_dict.keys())
    number_of_dishes = randrange(1, min(max_number_of_dishes, len(dish_list)))
    select_dishes = sample(dish_list, number_of_dishes)

    for each_id in select_dishes:
        menu_items.append(menu_item_dict[each_id])
        
        
    location_dict[LOCATION_LAT_KEY] = rest_coord[0]; location_dict[LOCATION_LON_KEY]= rest_coord[1];
    info_dict[INFO_NAME_KEY] = rest_name; info_dict[INFO_PHONE_KEY] = rest_phone; info_dict[INFO_LOCATION_KEY] = location_dict
    dictionary_to_construct_rest[RESTAURANT_INFO_KEY] = info_dict
    dictionary_to_construct_rest[RESTAURANT_MAX_CAPACITY_KEY] = randrange(min_capacity,max_capacity)

    the_rest = restaurant(dictionary_to_construct_rest)
    the_rest.menu_items = menu_items

    return the_rest
