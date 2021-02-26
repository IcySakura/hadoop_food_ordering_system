import uuid
import random

#constants (can edit):
FIRST_NAMES = ["Alice","Bob", "Charlie"]
LAST_NAMES = ["Adams", "Smith"]

UCI_COORDS = (33.640633,-117.844505)
DEFAULT_RADIUS_IN_KM = 10.0

#conversion (Don't edit unless you are sure the code will still work with changes):
KM_TO_COORD_DELTA = 0.01 #rouch conversion: see example: http://boulter.com/gps/distance/?from=%2833.640633%2C-117.844505%29&to=%2833.650633%2C-117.844505%29&units=m


#functions:
def generate_unique_id():
    return str(uuid.uuid4()) #https://stackoverflow.com/a/1210468/13544635

def generate_customer_name():
    return "{} {}".format(random.choice(FIRST_NAMES), random.choice(LAST_NAMES))

def generate_location(center=UCI_COORDS,radius=DEFAULT_RADIUS_IN_KM):
    '''generate a coord in radius from center'''
    delta = KM_TO_COORD_DELTA  * radius
    (centerLat,centerLon) = center
    
    return (random.uniform(centerLat-delta,centerLat+delta),random.uniform(centerLon-delta,centerLon+delta))
    
def generate_phone_number():
    #for now, just return a constant
    return "(123) 456-7890"
