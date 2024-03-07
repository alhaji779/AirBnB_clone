#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """ This class manages the cities where accommodations are available """

    state_id = ""
    name = ""
