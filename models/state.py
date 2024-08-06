#!/usr/bin/python3
""" Class State """

from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models

class State(BaseModel, Base):
    """ Class State """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City", cascade="all, delete,delete-orphan", backref="state")
    else:
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances with state_id equals to the current State.id"""
            city_list = []
            all_cities = models.storage.all(models.City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list