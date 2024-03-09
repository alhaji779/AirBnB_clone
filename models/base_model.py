#!/usr/bin/python3
import uuid
from datetime import datetime
import models
""" This is the Base Module where other classes will feed from """


class BaseModel:
    """ Functions and attributes that custs across other classes """
    def __init__(self, *args, **kwargs):
        """ This is the constructor of the Base Module
            Modified to accept dict arg as parameter if provided
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    pass
                elif k == 'created_at' or k == 'updated_at':
                    setattr(
                        self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    )
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """ This is the default print content of the base module """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """ This method is called when a new or existing instance is saved.
            It updates the Updated_date to current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ This converts an object instance to a dictionary structur """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict
