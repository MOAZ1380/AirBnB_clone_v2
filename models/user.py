#!/usr/bin/python3
""" class"""
from models.base_model import BaseModel


class User(BaseModel):
    """ class """

    email = ''
    password = ''
    first_name = ''
    last_name = ''


# #!/usr/bin/python3
# """ Class User """

# from sqlalchemy import Column, String
# from models.base_model import BaseModel, Base
# from sqlalchemy.orm import relationship
# from os import getenv

# class User(BaseModel, Base):
#     """This class defines a user by various attributes"""
#     __tablename__ = "users"
#     email = Column(String(128), nullable=False)
#     password = Column(String(128), nullable=False)
#     first_name = Column(String(128), nullable=True)
#     last_name = Column(String(128), nullable=True)
#     places = relationship("Place", backref="user", cascade="all, delete-orphan")  ##backkref
#     reviews = relationship("Review", backref="user", cascade="all, delete-orphan") ##backkref
    
    