#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            theSpecificClassDict = {}
            for key in FileStorage.__objects:
                splitNgetTheName = key.split('.')[0]
                if splitNgetTheName == cls.__name__:
                    theSpecificClassDict[key] = self.__objects[key]
            # print (theSpecificClassDict)
            return theSpecificClassDict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        # self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

        # json_objects = {}
        # for key in self.__objects:
        #     if key == "password":
        #         json_objects[key].decode()
        #     json_objects[key] = self.__objects[key].to_dict(save_fs=1)
        # with open(self.__file_path, 'w') as f:
        #     json.dump(json_objects, f)


    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it is inside"""
        if obj is not None:
            # key = type(obj).__class__.name + '.' + obj.id
            # if key in self.__objects:
            #     del self.__objects[key]
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call the reload method to deserialize the JSON file to objects."""
        self.reload()
