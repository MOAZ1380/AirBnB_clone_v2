#!/usr/bin/python3
"""__init__ method for models package, or
Module for FileStorage autoinit."""

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
