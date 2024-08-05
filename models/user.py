#!/usr/bin/python3
""" class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship



class User(BaseModel, Base):
    """ class """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", back_populates ='user', cascade="all, delete, delete-orphan")
    reviews = relationship("Review" ,back_populates='user' , cascade="all, delete, delete-orphan")