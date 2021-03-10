import simplejson
import urllib.request

PATH_TO_GOOGLE_MAPS_KEY = "google_maps_key.txt" #make sure this is the path to the txt file with the key

#helper function:
def read_google_maps_key(path_to_key):
    try:
        f = open(path_to_key,'r')
        key = f.read().strip()
        f.close()

        return key
    except:
        raise Exception("Error opening/ finding Google Maps API Key file, double check that variable 'PATH_TO_GOOGLE_MAPS_KEY' is correct and you have the key file")

def convert_time_string_to_number_of_mins(google_driving_time_string):
    '''convert time_string returned from google map api into int number of mins'''
    #formats:
    #   1) "1 hour 45 mins"
    #   2) "6 mins"
    number_of_mins = 0
    number_of_hours = 0

    to_parse = google_driving_time_string.strip().split()

    if "hour" in google_driving_time_string:
        try:
            number_of_hours = int(to_parse[0])
        except:
            pass

    if "mins" in google_driving_time_string:
        try:
            number_of_mins = int(to_parse[-2])
        except:
            pass

    number_of_mins = max(number_of_mins,0)
    number_of_hours = max(number_of_hours,0)

    return 60 * number_of_hours + number_of_mins

#function:
def get_time_between_two_points(lat_1,lon_1,lat_2, lon_2):
    KEY = read_google_maps_key(PATH_TO_GOOGLE_MAPS_KEY)

    time_in_mins = 0

    try:
        orig_coord  = "{},{}".format(lat_1,lon_1)  # (latitude, longitude) don't confuse
        dest_coord = "{},{}".format(lat_2, lon_2)

        url = "https://maps.googleapis.com/maps/api/distancematrix/json?key={0}&origins={1}&destinations={2}&mode=driving&language=en-EN&sensor=false".format(KEY,str(orig_coord),str(dest_coord))


        result= simplejson.load(urllib.request.urlopen(url))

        driving_time = result['rows'][0]['elements'][0]['duration']['text']

        time_in_mins = convert_time_string_to_number_of_mins(driving_time)
    except Exception as e:
        print("error encountered in google_map_handler: {}".format(e))

    return time_in_mins


if __name__ == "__main__":
    time_in_mins = get_time_between_two_points(33.650212,-117.840672,33.650876,-117.827445)
    print(time_in_mins)