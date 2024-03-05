#!/usr/bin/python3
import uuid
from datetime import datetime
""" This is the Base Module where other classes will feed from """

class BaseModel:
    """ Base module is the Base Class of the AirBNB app, it will be the base for other classes.
        Functions and attributes that custs across other classes will be defined here
    """
    def __init__(self):
        """ This is the constructor of the Base Module """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ This is the default print content of the base module """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ This method is called when a new or existing instance is saved.
            It updates the Updated_date to current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ This converts an object instance to a dictionary structure for serialization """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        
        return new_dict
