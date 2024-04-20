#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBstorage
from os import getenv

realllBadEnvironment = getenv("HBNB_TYPE_STORAGE")

if realllBadEnvironment == "db":
    storage = DBstorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
