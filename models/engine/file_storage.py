#!/usr/bin/python3
"""
Module for FileStorage class 4 serializing and deserializing data
"""
import json
import os
from models.base_model import BaseModel
import datetime


class FileStorage:
    """
    Class for serializtion and deserialization of base classes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key 
        <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        all_objs = FileStorage.__objects
        obj_dictionary = {}

        for obj in all_objs.keys():
            obj_dictionary[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dictionary, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dictionary = json.load(file)
                    for key, value in obj_dictionary.items():
                        class_name, obj_id = key.split('.')
                        CC = eval(class_name)
                        inst_ance = CC(**value)

                        FileStorage.__objects[key] = inst_ance
                except Exception:
                    pass