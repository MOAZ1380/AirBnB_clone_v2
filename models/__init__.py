#!/usr/bin/python3
"""__init__ method for models package, or
Module for FileStorage autoinit."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()











# #!/usr/bin/python3
# """This module instantiates an object of class FileStorage"""

# from models.engine.file_storage import FileStorage
# from os import getenv
# from models.engine.db_storage import DBStorage

# if getenv("HBNB_TYPE_STORAGE") == "db":
#     storage = DBStorage()
# else:
#     storage = FileStorage()
# storage.reload()