from constants import ORDER_ID_KEY, CUSTOMER_ID_KEY, CUSTOMER_INFO_KEY, MAX_DISTANCE_KEY, ORDER_KEY
from info import info
from menu_item import menu_item

#TODO: add type checking, conversion to correct type

class order:
    def __init__(self,order_dict=dict()):
        self.order_id = ""
        self.customer_id = ""
        self.info = info()
        self.max_distance = 0.0
        self.order_items = []

        if len(order_dict) != 0:
            self.load_order_from_dict(order_dict)

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

