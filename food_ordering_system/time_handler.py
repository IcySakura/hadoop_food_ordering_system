import datetime

def get_current_datetime():
    return datetime.datetime.now()

def get_timestamp_from_datetime(the_datetime):
    return the_datetime.timestamp()

def get_datetime_from_timestamp(the_timestamp):
    return datetime.datetime.fromtimestamp(the_timestamp)

def get_delta_datetime(the_datetime, delta_minutes):
    delta = datetime.timedelta(minutes = delta_minutes)
    return the_datetime + delta

def how_much_time_is_left(future_datetime):
    now_datetime = get_current_datetime()
    return (future_datetime - now_datetime).seconds


if __name__ == "__main__":
    #example communicate time, and calculate time order will take:
    ##Step 1) Get current datetime:
    current_datetime_when_order_placed = get_current_datetime()
    print("Order was placed at: {}".format(current_datetime_when_order_placed))

    ##Step 2) Convert to timesstemap:
    current_timestamp_when_order_placed = get_timestamp_from_datetime(current_datetime_when_order_placed)

    ##Step 3) *optional transit timestamp in order json*

    ##Step 4) Convert back to datetime:
    reconstructed_datetime_when_order_was_place = get_datetime_from_timestamp(current_timestamp_when_order_placed)

    ##Step 5) Look at how long it will take to make the order, and add that to the datetime:
    minutes_neeeded_to_cook = 5
    datetime_when_order_will_be_ready = get_delta_datetime(reconstructed_datetime_when_order_was_place, minutes_neeeded_to_cook)
    print("Order will be ready at: {}".format(datetime_when_order_will_be_ready))

    ##Step 6) Check how much time is left:
    time_left = how_much_time_is_left(datetime_when_order_will_be_ready)
    print("Time left: {} seconds".format(time_left))
