from constants import LOCATION_LAT_KEY, LOCATION_LON_KEY

#TODO: add type checking, conversion to correct type

class location:
    def __init__(self,location_dict=dict()):
        self.lat = ""
        self.lon = ""

        if len(location_dict) != 0:
            self.load_location_from_dict(location_dict)

    def load_location_from_dict(self, location_dict):
        if LOCATION_LAT_KEY in location_dict:
            self.lat = location_dict[LOCATION_LAT_KEY]

        if LOCATION_LON_KEY in location_dict:
            self.lon = location_dict[LOCATION_LON_KEY]

    def convert_to_dict(self):
        to_return = dict()
        to_return[LOCATION_LAT_KEY] = self.lat
        to_return[LOCATION_LON_KEY] = self.lon
        return to_return
