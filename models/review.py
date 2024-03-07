#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """ This class manages the reviews of customers """

    place_id = ""
    user_id = ""
    text = ""

