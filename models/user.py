#!/usr/bin/python3
""" This class is to manage users and authentication """

from models.base_model import BaseModel


class User(BaseModel):
    """ This class inherits from BaseModel and is used to manage users authentication """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
