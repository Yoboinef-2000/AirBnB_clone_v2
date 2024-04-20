#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City


theREEEALenv = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    if theREEEALenv == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              backref="state", cascade="all, delete,\
                                  delete-orphan")
    else:
        name = ""

    if theREEEALenv != "db":
        @property
        def cities(self):
            """Getter Method."""
            from models import storage
            cities = []
            everyCity = storage.all(City)
            for city in everyCity.values():
                if city.state_id == self.id:
                    cities.append(city)
            return (cities)
