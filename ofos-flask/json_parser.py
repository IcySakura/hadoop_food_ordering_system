import json

#read/ write json functions:
def load_json_file_as_dict(file_path):
    '''load json file as dict'''
    with open(file_path) as f:
        return json.load(f)

def write_dict_to_json_file(the_dict,file_path):
    '''writes dict (of json object) to json file'''
    with open(file_path, 'w') as json_file:
        json.dump(the_dict, json_file)

    
#encode/ decode dict functions:
def dict_to_string(a_dict):
    '''takes dict of json object and converts to json string'''
    return json.dumps(a_dict)

def string_to_dict(a_string):
    '''decodes string (representation of dict) to a dict'''
    return json.loads(a_string)

#print json functions:
def json_pretty_print(to_print):
    '''pretty print function for json string or dict of json string'''
    if not isinstance(to_print, dict):
        to_print = json.loads(to_print)
    print(json.dumps(to_print, indent = 4))