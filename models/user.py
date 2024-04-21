#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from hashlib import md5
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

theREEEALenv = getenv('HBNB_TYPE_STORAGE')

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    
    if theREEEALenv == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
    
    def __init__(self, *args, **kwargs):
        """Initialize User."""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """Use md5 encryption to set a password."""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
