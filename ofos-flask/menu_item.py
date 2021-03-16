from constants import MENU_ITEM_NAME_KEY, MENU_ITEM_ID_KEY, MENU_ITEM_QUANTITY_KEY

#TODO: add type checking, conversion to correct type

class menu_item:
    def __init__(self,menu_dict=dict()):
        self.name = ""
        self.id = ""
        self.quantity = 0

        if len(menu_dict) != 0:
            self.load_menu_item_from_dict(menu_dict)

    def has_id(self):
        return isinstance(self.id,str) and len(self.id) > 0 or self.id >= 0

    def load_menu_item_from_dict(self,menu_dict):
        if MENU_ITEM_NAME_KEY in menu_dict:
            self.name = menu_dict[MENU_ITEM_NAME_KEY]

        if MENU_ITEM_ID_KEY in menu_dict:
            self.id = menu_dict[MENU_ITEM_ID_KEY]

        if MENU_ITEM_QUANTITY_KEY in menu_dict:
            self.quantity = int(menu_dict[MENU_ITEM_QUANTITY_KEY])

    def convert_to_dict(self):
        to_return = dict()
        to_return[MENU_ITEM_NAME_KEY] = self.name
        to_return[MENU_ITEM_ID_KEY] = self.id
        to_return[MENU_ITEM_QUANTITY_KEY] = str(self.quantity)
        return to_return