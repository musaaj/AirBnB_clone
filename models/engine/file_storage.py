#!/usr/bin/python3
"""Objects storage engine"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage engine"""
    __file_paths = 'file.json'
    __objects = {}

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
                          key: BaseModel(**value)
                          for key, value in objects.items()
                        }
        except FileNotFoundError:
            pass

    def get(self, id):
        """get an object based on id"""
        obj = self.__objects.get(id)
        if obj:
            return json.dumps(str(obj))
        return False
