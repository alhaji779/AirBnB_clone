#!/usr/bin/python3
""" This class manages states of the AirBNB backend """

from models.base_model import BaseModel

class State(BaseModel):
    """ This class stores the various states where accommodation exist """

    name = ""
