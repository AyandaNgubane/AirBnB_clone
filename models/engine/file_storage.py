#!/usr/bin/python3
"""
File that will be responsible for sereialization
and deserialization
"""

import json
from models.base_model import BaseModel
from os import path
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A class that serializes instances to a JSON file
    and deserializes JSON file to instances:

    models/engine/file_storage.py
    Private class attributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by
    <class name>.id (ex: to store a BaseModel object with id=12121212,
    the key will be BaseModel.12121212)
    Public instance methods:
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file (path: __file_path)
    reload(self): deserializes the JSON file to __objects (only if the JSON
    file (__file_path) exists ; otherwise, do nothing. If the file doesn’t
    exist, no exception should be raised)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """

        return (self.__objects)

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """

        key = "{}.{}".format(obj.__class__.__name__, str(obj.id))

        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dict_json = {key: value.to_dict() for
                         key, value in FileStorage.__objects.items()}
            json.dump(dict_json, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """

        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.load(f)
            json_dict = {key: eval(value["__class__"])(**value) for
                         key, value in json_dict.items()}
            FileStorage.__objects = json_dict
