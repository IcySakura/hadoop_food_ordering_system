from google_map_handler import get_time_between_two_points

#constants:
DEFAULT_RATE = 10 #unit of min per dish

#functions:
def calculate_static_prep_time(capacity, number_of_dishes_ordered, rate_in_mins_per_dish=DEFAULT_RATE):
    '''calculate prep_time needed to prepare food'''

    #explanation:
    #capacity = # of cooks that can prepare food (they work in parallel to complete order)
    #   NOTE: min capcity is 1, if capcity is less than 1, it adds a buffer ammount of time to order completion
    #rate_in_mins_per_dish = time it takes 1 cook to prepare 1 dish
    #number_of_dishes_ordered ordered = how many dishes were ordered

    # Now lets define: number_of_cook_iterations_to_complete to be the max number of dishes one cook has to prepare
    #   Since it takes this cook rate_in_mins_per_dish t prepare the dish:

    #prep_time = number_of_cook_iterations_to_complete * rate_in_mins_per_dish + buffer
    #   (the buffer was to handle the case if the inital capacity was less than 1, and we have to wait for a chef to finish their prior dish)

    #Finally: number_of_cooks_occupied_by_task is just the max number of cooks used at once

    capacity = max(capacity,1) #use minimum capcity of 1
    buffer = rate_in_mins_per_dish if capacity < 1 else 0

    rem = number_of_dishes_ordered % capacity
    div = number_of_dishes_ordered // capacity

    number_of_cook_iterations_to_complete = div + (1 if rem > 0 else 0)

    prep_time = number_of_cook_iterations_to_complete * rate_in_mins_per_dish + buffer
    number_of_cooks_occupied_by_task = capacity if div > 0 else rem

    return (prep_time, number_of_cooks_occupied_by_task)


def calculate_driving_time(location_object_1, location_object_2):
    '''calculate current drive time (using google's map api) between two points'''
    lat1 = location_object_1.lat; lon1 = location_object_1.lon
    lat2 = location_object_2.lat; lon2 = location_object_2.lon

    return get_time_between_two_points(lat1,lon1,lat2, lon2)

def calculate_wait_time(prep_time, drive_time):
    return max(prep_time, drive_time)

def calculate_approximate_wait_time_and_number_of_cooks_occupied(order_object, restraunt_object, current_capacity=0, use_current_capacity=False):
    order_location = order_object.info.location
    restraunt_location = restraunt_object.info.location

    restraunt_capacity = restraunt_object.max_capacity if not use_current_capacity else current_capacity
    number_of_dishes_ordered = order_object.count_number_of_order_items()

    (prep_time, estimated_number_of_cooks_occupied_by_task) = calculate_static_prep_time(restraunt_capacity, number_of_dishes_ordered)
    drive_time = calculate_driving_time(order_location, restraunt_location)

    wait_time = calculate_wait_time(prep_time, drive_time)

    return (wait_time, estimated_number_of_cooks_occupied_by_task)