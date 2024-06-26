#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

theREEEALenv = getenv('HBNB_TYPE_STORAGE')


class Place(BaseModel, Base):
    """ A place to stay """
    if theREEEALenv == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        # user = relationship("User", back_populates="places")
        # city = relationship("City", back_populates="places")
        reviews = \
            relationship("Review", cascade="all, delete", backref="place")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    # __tablename__ = 'places'

    # if theREEEALenv == "db":
    #     city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    #     user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    #     name = Column(String(128), nullable=False)
    #     description = Column(String(1024), nullable=True)
    #     number_rooms = Column(Integer, default=0, nullable=False)
    #     number_bathrooms = Column(Integer, default=0, nullable=False)
    #     max_guest = Column(Integer, default=0, nullable=False)
    #     price_by_night = Column(Integer, default=0, nullable=False)
    #     latitude = Column(Float, nullable=True)
    #     longitude = Column(Float, nullable=True)
    # else:
    #     city_id = ""
    #     user_id = ""
    #     name = ""
    #     description = ""
    #     number_rooms = 0
    #     number_bathrooms = 0
    #     max_guest = 0
    #     price_by_night = 0
    #     latitude = 0.0
    #     longitude = 0.0

    @property
    def reviews(self):
        """Getter attribute that returns the list of Review instances."""
        from models import storage
        review_list = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list
