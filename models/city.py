#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
# from sqlalchemy import Column, String, ForeignKey
# from os import getenv


class City(BaseModel):
    """ The city class, contains state ID and name """
    # theREEEALenv = getenv('HBNB_TYPE_STORAGE')
    # if theREEEALenv == "db":
    #     __tablename__ = "cities"
    #     name = Column(String(128), nullable=False)
    #     state_id = Column(String(128), ForeignKey=('states.id')
    # , nullable=False)
    state_id = ""
    name = ""
