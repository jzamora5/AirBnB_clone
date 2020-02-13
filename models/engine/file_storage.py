#!/usr/bin/python3

""" Module for serializing and deserializing instances to JSON """

import json


class FileStorage:

    """ Class that stores and loads instances to/from files in JSON format """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj key <obj class name>.id """
        obj_id = obj.__class__.__name__ + '.' + obj.id
        self.__objects[obj_id] = obj.to_dict()

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        jst = json.dumps(self.__objects)
        with open(self.__file_path, "w", encoding="utf-8") as myfile:
            myfile.write(jst)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, encoding="utf-8") as myfile:
                rd = myfile.read()
                if not rd or len(rd) == 0:
                    return None
                self.__objects = json.loads(rd)
        except IOError:
            pass
