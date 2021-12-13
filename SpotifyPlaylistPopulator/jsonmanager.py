import json
import os

def read_json(file_name):
    current_directory = os.path.dirname(__file__)
    path = os.path.join(current_directory, file_name)
    with open(path, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object