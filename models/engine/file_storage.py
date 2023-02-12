#!/usr/bin/python3
"""Objects storage engine"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""Authors henok934 & musaaj"""


class FileStorage:
    """FileStorage engine"""
    __file_paths = 'file.json'
    __objects = {}
    __classes = {
              'User': User,
              'BaseModel': BaseModel,
              'State': State,
              'City': City,
              'Amenity': Amenity,
              'Place': Place,
              'Review': Review
            }

    def all(self):
        """get all the objects in this engine"""
        return self.__objects

    def new(self, obj):
        """add a new object to this engine"""
        id = '{}.{}'.format(
                  obj.__class__.__name__,
                  obj.id
                )
        self.__objects[id] = obj

    def save(self):
        """write objects to file"""
        objects = {}
        for key in self.__objects:
            objects[key] = self.__objects[key].to_dict()
        try:
            with open(self.__file_paths, 'w') as fp:
                json.dump(objects, fp)
                fp.close()
        except PermissionError:
            pass

    def reload(self):
        """reload objects from file"""
        try:
            with open(self.__file_paths, 'r') as fp:
                objects = json.load(fp)
                fp.close()
                self.__objects = {
                          key: self.__classes.get(key.split('.')[0])(**value)
                          for key, value in objects.items()
                        }
        except FileNotFoundError:
            pass

    def get(self, id):
        """get an object based on id"""
        obj = self.__objects.get(id)
        if obj:
            return obj
        return False

    def destroy(self, id):
        """delete a given object from the storage"""
        if id:
            try:
                return self.__objects.pop(id)
            except KeyError:
                return False
        return False
