#!/usr/bin/python3
"""  """


from os.path import exists
import json


class FileStorage:
    """  """

    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the dictionary objects"""
        return self.__objects
        
    def new(self, obj):
        """sets in objects the obj with key <obj class name>.id"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        self.save()

    def save(self):
        """ serializes objects to the JSON file """
        dicts = {}
        for key, value in self.__objects.items():
            dicts[key] = value.to_dict() 
        with open(self.__file_path, 'w') as f:
            json.dump(dicts, f)

    def reload(self):
        """ deserializes the JSON file to objects """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                dicts = json.load(f)
                for key, value in dicts.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
                    self.__objects[key].id = key
                    self.save()
        else:
            return
