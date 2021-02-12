from constants import ORDER_ID_KEY, CUSTOMER_ID_KEY, RESTAUARNT_ID_KEY, ESTIMATED_FINISH_KEY
from info import info
from menu_item import menu_item

#TODO: add type checking, conversion to correct type

class confirmation:
    def __init__(self,confirmation_dict=dict()):
        self.order_id = ""
        self.customer_id = ""
        self.restaurant_id = ""
        self.estimated_time = ""

        if len(confirmation_dict) != 0:
            self.load_confirmation_from_dict(confirmation_dict)

    def load_confirmation_from_dict(self, confirmation_dict):
        if ORDER_ID_KEY in confirmation_dict:
            self.order_id = confirmation_dict[ORDER_ID_KEY]

        if CUSTOMER_ID_KEY in confirmation_dict:
            self.customer_id = confirmation_dict[CUSTOMER_ID_KEY]
            
        if RESTAUARNT_ID_KEY in confirmation_dict:
            self.restaurant_id = confirmation_dict[RESTAUARNT_ID_KEY]

        if ESTIMATED_FINISH_KEY in confirmation_dict:
            self.estimated_time = confirmation_dict[ESTIMATED_FINISH_KEY]


    def convert_to_dict(self):
        to_return = dict()
        to_return[ORDER_ID_KEY] = self.order_id
        to_return[CUSTOMER_ID_KEY] = self.customer_id
        to_return[RESTAUARNT_ID_KEY] = self.restaurant_id
        to_return[ESTIMATED_FINISH_KEY] = self.estimated_time
        return to_return

    
        
