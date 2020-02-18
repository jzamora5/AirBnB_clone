#!/usr/bin/env python3

""" Module for serializing and deserializing instances to JSON and keeping
storage of instances
"""

import json


class FileStorage:

    """ Class that stores and loads instances to/from files in JSON format """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj key <obj class name>.id """
        obj_id = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[obj_id] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        jdic = {}

        for key, value in FileStorage.__objects.items():
            jdic[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as myfile:
            json.dump(jdic, myfile)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as myfile:
                from models.base_model import BaseModel
                from models.user import User
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                from models.state import State

                pobj = json.load(myfile)
                for key, value in pobj.items():
                    clas = value["__class__"]
                    obj = eval(clas + "(**value)")
                    FileStorage.__objects[key] = obj
        except IOError:
            pass
