from constants import LOCATION_LAT_KEY, LOCATION_LON_KEY
from geopy.distance import geodesic

#TODO: add type checking, conversion to correct type

#functions:
def calculate_distance_in_km_between_coords(lat_1,lon_1,lat_2, lon_2):
    '''return distance in km between two points, return -1 if error'''
    #source: https://stackoverflow.com/a/57445729/13544635
    try:
        origin = (float(lat_1), float(lon_1))  # (latitude, longitude) don't confuse
        dist = (float(lat_2), float(lon_2))
    
        return geodesic(origin, dist)
    except:
        return -1

#class:
class location:
    def __init__(self,location_dict=dict()):
        self.lat = ""
        self.lon = ""

        if len(location_dict) != 0:
            self.load_location_from_dict(location_dict)

    def caluclate_distance_to_location(self, a_location):
        if isinstance(a_location,location):
            return calculate_distance_in_km_between_coords(self.lat, self.lon, a_location.lat, a_location.lon)
        else:
            return -1

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