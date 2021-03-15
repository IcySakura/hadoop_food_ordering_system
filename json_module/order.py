from constants import ORDER_ID_KEY, CUSTOMER_ID_KEY, CUSTOMER_INFO_KEY, MAX_DISTANCE_KEY, ORDER_KEY
from constants import INFO_NAME_KEY, INFO_PHONE_KEY, INFO_LOCATION_KEY
from constants import LOCATION_LAT_KEY, LOCATION_LON_KEY

from info import info
from menu_item import menu_item
from generator import generate_unique_id, generate_customer_name, generate_location, generate_phone_number

from random import choice, sample, randrange

#TODO: add type checking, conversion to correct type

def is_blank(to_check):
    return isinstance(to_check,type(None)) or len(to_check) == 0

class order:
    def __init__(self,order_dict=dict()):
        self.order_id = ""
        self.customer_id = ""
        self.info = info()
        self.max_distance = 0.0
        self.order_items = []

        if len(order_dict) != 0:
            self.load_order_from_dict(order_dict)

    def count_number_of_order_items(self):
        return len(self.order_items)

    def load_order_from_dict(self, order_dict):
        if ORDER_ID_KEY in order_dict:
            self.order_id = order_dict[ORDER_ID_KEY]

        if CUSTOMER_ID_KEY in order_dict:
            self.customer_id = order_dict[CUSTOMER_ID_KEY]

        if CUSTOMER_INFO_KEY in order_dict:
            self.info.load_info_from_dict(order_dict[CUSTOMER_INFO_KEY])

        if MAX_DISTANCE_KEY in order_dict:
            self.max_distance = float(order_dict[MAX_DISTANCE_KEY])

        if ORDER_KEY in order_dict:
            for each_item in order_dict[ORDER_KEY]:
                self.order_items.append(menu_item(each_item))

    def convert_to_dict(self):
        to_return = dict()
        to_return[ORDER_ID_KEY] = self.order_id
        to_return[CUSTOMER_ID_KEY] = self.customer_id
        to_return[CUSTOMER_INFO_KEY] = self.info.convert_to_dict()
        to_return[MAX_DISTANCE_KEY] = str(self.max_distance)

        order_item_dict_list = []
        for each_item in self.order_items:
            order_item_dict_list.append(each_item.convert_to_dict())
        to_return[ORDER_KEY] = order_item_dict_list
        return to_return

def construct_order_object(items_to_order, customer_max_distance=10.0, order_id=None,customer_id=None,customer_name=None,customer_phone=None,customer_coord=None):
    location_dict = {}
    info_dict = {}
    dictionary_to_construct_order = {}

    if is_blank(order_id):
        order_id = generate_unique_id()
        
    if is_blank(customer_id):
        customer_id = generate_unique_id()

    if is_blank(customer_name):
        customer_name = generate_customer_name()

    if is_blank(customer_phone):
        customer_phone = generate_phone_number()

    if is_blank(customer_coord):
        customer_coord = generate_location()
        
    location_dict[LOCATION_LAT_KEY] = customer_coord[0]; location_dict[LOCATION_LON_KEY]= customer_coord[1];
    info_dict[INFO_NAME_KEY] = customer_name; info_dict[INFO_PHONE_KEY] = customer_phone; info_dict[INFO_LOCATION_KEY] = location_dict
    dictionary_to_construct_order[CUSTOMER_INFO_KEY] = info_dict

    dictionary_to_construct_order[ORDER_ID_KEY] = order_id; dictionary_to_construct_order[CUSTOMER_ID_KEY] = customer_id
    dictionary_to_construct_order[MAX_DISTANCE_KEY] = customer_max_distance
    dictionary_to_construct_order[ORDER_KEY] = items_to_order
    
    the_order = order(dictionary_to_construct_order)
    return the_order


def create_random_order(menu_item_id_to_restraunt_id, restraunt_id_to_menu_item_id, menu_item_dict,restraunt_id_dict,max_number_of_unique_dishes_to_order=3, max_quantity_per_dish=3):
    select_random_dish = choice(list(menu_item_dict.keys()))
    select_random_restraunt_that_serves_random_dish = choice(list(menu_item_id_to_restraunt_id[select_random_dish]))

    additional_dish_ids = restraunt_id_to_menu_item_id[select_random_restraunt_that_serves_random_dish]
    additional_dish_ids.remove(select_random_dish)

    number_of_additional_dishes = randrange(0, min(max_number_of_unique_dishes_to_order, len(additional_dish_ids)))
    select_additional_random_dish_list = sample(additional_dish_ids, number_of_additional_dishes)

    dishes_to_order = [select_random_dish] + select_additional_random_dish_list

    order_items = []
    for each_dish_id in dishes_to_order:
        the_item = menu_item_dict[each_dish_id]
        the_item.quantity = randrange(1,max_quantity_per_dish)
        order_items.append(the_item.convert_to_dict())

    return construct_order_object(order_items)
    
