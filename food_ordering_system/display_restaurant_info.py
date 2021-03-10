def get_google_map_link_to_coords(lat,lon):
    return "http://maps.google.com/maps?q={},{}".format(lat,lon) #based off of: https://stackoverflow.com/a/5807150/13544635


def get_google_map_link_from_restraunt_with_id(the_id, restraunt_dict):
    if the_id in restraunt_dict:
        the_location = restraunt_dict[the_id].info.location
        return get_google_map_link_to_coords(the_location.lat,the_location.lon)
    else:
        return ""

def get_restaurant_info_from_id(the_id, restraunt_dict):
    the_name = ""
    the_phone_number = ""
    the_google_maps_link = ""

    if the_id in restraunt_dict:
        the_name = restraunt_dict[the_id].info.name
        the_phone_number = restraunt_dict[the_id].info.phone
        the_google_maps_link = get_google_map_link_from_restraunt_with_id(the_id, restraunt_dict)

    return (the_name, the_phone_number, the_google_maps_link)
    
