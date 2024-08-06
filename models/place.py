#!/usr/bin/python3
""" Class Place """

from sqlalchemy import Column, String, Integer, ForeignKey, Float
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models import storage

class Place(BaseModel, Base):
    """This class defines a place by various attributes"""
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
    
    if getenv('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship("Review", cascade="all, delete,delete-orphan", backref="user")
    else:
        @property
        def reviews(self):
            all_reviews = storage.all(Review)
            return [review for review in all_reviews.values() if review.place_id == self.id]
    # user = relationship('User', back_populates='places')
    # cities = relationship('City', back_populates='places') #####