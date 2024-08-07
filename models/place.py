#!/usr/bin/python3
""" Class Place """

from sqlalchemy import Column, String, Integer,Table, ForeignKey, Float
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import *

metadata = MetaData()
place_amenity = Table('place_amenity', metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

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
    reviews = relationship('Review',backref='place', cascade='all, delete-orphan')
    amenities = relationship('Amenity', secondary="place_amenity",viewonly=False, overlaps="place_amenities")
    amenity_ids = []
    
    
    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def reviews(self):
            from models import storage
            """getter attribute returns the list of Review instances"""
            all_reviews = list(storage.all(Review).values())
            review_list = [r for r in all_reviews if r.place_id == self.id]
            return review_list
        @property
        def amenities(self):
            return self._amenities

        @amenities.setter
        def amenities(self, value):
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
    