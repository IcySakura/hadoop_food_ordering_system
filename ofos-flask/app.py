from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, FormField
from wtforms.fields.core import FieldList, FloatField, StringField
from wtforms.validators import DataRequired

import os
import subprocess
from random import randint
import json
import glob
import ast
from collections import defaultdict

from restaurant import restaurant
from json_parser import *
from collections import defaultdict

app = Flask(__name__)

# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'OAdregJF9823Rofjwoef3209489H4T'

# Flask-Bootstrap requires this line
Bootstrap(app)

class FoodQuantityForm(FlaskForm):
    menu_item_name = StringField()
    menu_item_quantity = IntegerField('Quantity', default=0)
    menu_item_id = IntegerField()
    
class OrderForm(FlaskForm):
    customer_name = StringField('Name', validators=[DataRequired()])
    latitude = FloatField("Latitude", validators=[DataRequired()])
    longitude = FloatField("Longitude", validators=[DataRequired()])
    preferred_max_distance = IntegerField("Preferred maximum distance (in kilometers)", validators=[DataRequired()])
    menu = FieldList(FormField(FoodQuantityForm), min_entries=1)
    submit = SubmitField('Submit')

def create_all_restraunts_from_json_files_in_folder(path_to_folder):
    list_of_restraunts = []
    json_files = [os.path.join(path_to_folder, pos_json) for pos_json in os.listdir(path_to_folder) if pos_json.endswith('.json')]

    for each_json_file in json_files:
        each_restraunt = restaurant(load_json_file_as_dict(each_json_file))
        if each_restraunt.has_menu_items:
            list_of_restraunts.append(each_restraunt)

    return list_of_restraunts

def create_map_of_menu_items(list_of_restraunts):
    menu_item_id_to_restraunt_id = defaultdict(list)
    restraunt_id_to_menu_item_id = defaultdict(list)
    menu_item_dict = dict()
    restraunt_id_dict = dict()

    for each_restraunt in list_of_restraunts:
        if each_restraunt.has_id():
            if each_restraunt.id not in restraunt_id_dict:
                restraunt_id_dict[each_restraunt.id] = each_restraunt
            else:
                print("Error: duplicate restraunt_id encountered: id # = {}, name = {}".format(each_restraunt.id,each_restraunt.info.name))

            for each_item in each_restraunt.menu_items:
                if each_item.id not in menu_item_dict:
                    menu_item_dict[each_item.id] = each_item
                elif each_item.name != menu_item_dict[each_item.id].name:
                    print("Error: duplicate menu_id encountered: id # = {}, name = {}".format(each_item.id,each_item.name)) #here

                if each_item.id not in menu_item_id_to_restraunt_id or each_restraunt.id not in menu_item_id_to_restraunt_id[each_item.id]:
                    menu_item_id_to_restraunt_id[each_item.id].append(each_restraunt.id)
                if each_restraunt.id not in restraunt_id_to_menu_item_id or each_item.id not in restraunt_id_to_menu_item_id[each_restraunt.id]:
                    restraunt_id_to_menu_item_id[each_restraunt.id].append(each_item.id)

    return (menu_item_id_to_restraunt_id, restraunt_id_to_menu_item_id, menu_item_dict,restraunt_id_dict)

def find_best_restaurant(order_dict):
    with open(f"./data/order_json/order_id_{order_dict['order_id']}.json", 'w') as fp:
        json.dump(order_dict, fp)

    restaurant_filepaths = ' '.join(glob.glob('./data/restaurant_json/*.json'))
    with open("input.txt", 'w') as f:
        f.write(f"./data/order_json/order_id_{order_dict['order_id']}.json" + "\n" + restaurant_filepaths)
    
    subprocess.run(['mapred', 'streaming', '-input', 'input.txt', '-output', 'output', '-mapper', 'mapper.py', '-reducer', 'reducer.py'])
    subprocess.run(['rm', '-rf', 'output'])

    with open(f"./data/confirmation_json/order_id_{order_dict['order_id']}_confirmation.json") as f:
        return_string = json.load(f)

    return return_string

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

@app.route('/', methods=['GET', 'POST'])
def index():
    PATH_TO_FOLDER = "./data/restaurant_json"
    list_of_restraunts = create_all_restraunts_from_json_files_in_folder(PATH_TO_FOLDER)
    (_, _, menu_item_dict, restaurant_dict) = create_map_of_menu_items(list_of_restraunts)
    
    id_to_menu_item_name = dict()
    for each_id in menu_item_dict:
        id_to_menu_item_name[each_id] = menu_item_dict[each_id].name
    
    menu_list = []
    for key, value in id_to_menu_item_name.items():
        menu_list.append({"menu_item_id": key, "menu_item_name":value, "menu_item_quantity": 0})

    # menu_list = [{"menu_item_name":"ribs", "menu_item_id": 4, "menu_item_quantity": 0}, {"menu_item_name":"fries", "menu_item_id": 2, "menu_item_quantity": 0}]
    form = OrderForm(menu=menu_list)
    err_message = ''

    if form.validate_on_submit():
        order_data = form.menu.data
        order_data = [i for i in order_data if i['menu_item_quantity'] > 0]
        for item in order_data:
            item.pop("csrf_token")
        total_quantity = 0
        for item in order_data:
            total_quantity += item['menu_item_quantity']
        if total_quantity == 0:
            return render_template('index.html', form=form, err_message='Please order at least one type of food.')

        order_dictionary = {}
        order_dictionary['order_id'] = randint(1, 2147483645)
        order_dictionary['customer_id'] = randint(1, 2147483645)
        order_dictionary['customer_info'] = {"name":form.customer_name.data, "phone":"1 (661) 123-4567", 'location':{'lat':form.latitude.data, 'lon':form.longitude.data}}
        order_dictionary['preferred_max_distance_km'] = form.preferred_max_distance.data
        order_dictionary['order'] = order_data

        confirmation_dict = find_best_restaurant(order_dictionary)
        message_to_flash = get_restaurant_info_from_id(confirmation_dict['restaurant_id'], restaurant_dict)
        flash(message_to_flash[0])
        flash(message_to_flash[1])
        flash(message_to_flash[2])
        flash(confirmation_dict['estimated_finish_time'])
        return redirect( url_for('results') )
    else:
        err_message = 'Please fill every field.'

    return render_template('index.html', form=form, err_message=err_message)

@app.route('/results')
def results():
    # pass all the data for the selected actor to the template
    return render_template('results.html')

# 2 routes to handle errors - they have templates too

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
