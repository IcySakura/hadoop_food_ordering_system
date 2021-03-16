from constants import INFO_NAME_KEY, INFO_PHONE_KEY, INFO_LOCATION_KEY
from location import location

#TODO: add type checking, conversion to correct type

class info:
    def __init__(self,info_dict=dict()):
        self.name = ""
        self.phone = ""
        self.location = location()

        if len(info_dict) != 0:
            self.load_info_from_dict(info_dict)

    def load_info_from_dict(self, info_dict):
        if INFO_NAME_KEY in info_dict:
            self.name = info_dict[INFO_NAME_KEY]

        if INFO_PHONE_KEY in info_dict:
            self.phone = info_dict[INFO_PHONE_KEY]

        if INFO_LOCATION_KEY in info_dict:
            self.location.load_location_from_dict(info_dict[INFO_LOCATION_KEY])

    def convert_to_dict(self):
        to_return = dict()
        to_return[INFO_NAME_KEY] = self.name
        to_return[INFO_PHONE_KEY] = self.phone
        to_return[INFO_LOCATION_KEY] = self.location.convert_to_dict()
        return to_return