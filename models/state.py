#!/usr/bin/python3
""" class"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete, delete-orphan")
    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """ returns list of City instances related to state """
            from models import storage
            list_cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities