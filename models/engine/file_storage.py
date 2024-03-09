#!/usr/bin/python3
""" The class serves to store data temporality to file """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ This class will handle data persistency by serializing
        the object.
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """ This methos returns all saved objects """
        return FileStorage.__objects

    def new(self, obj):
        """ This method creates a new instance of BaseModule
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ This method saves any instance of base module
            This is the serialized data in json format
        """
        new_obj = dict()
        for k, v in FileStorage.__objects.items():
            new_obj[k] = v.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_obj, f)

    def reload(self):
        """ This method retrieves object data from file.
            With this the data is persistant
        """
        new_obj = dict()
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                new_obj = json.load(f)
                for k, v in new_obj.items():
                    cl_name, cl_id = k.split('.')
                    new_class = eval(cl_name)
                    new_instance = new_class(**v)
                    FileStorage.__objects[k] = new_instance
        except Exception:
            pass
