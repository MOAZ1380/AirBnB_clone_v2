#!/usr/bin/python3
""" Place module for the HBNB project """
from os import getenv
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table,Integer,Float
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    
    # amenities = relationship('Amenity', secondary=place_amenity, viewonly=False, backref='place_amenities')
    city = relationship("City", back_populates="places")
    user = relationship("User", back_populates="places")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals to the current Place.id"""
            from models import storage
            review_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
        
        @property
        def amenities(self):
            """Returns the list of Amenity instances based on the attribute amenity_ids"""
            from models import storage
            amenity_list = []
            for amenity_id in self.amenity_ids:
                amenity_list.append(storage.get('Amenity', amenity_id))
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """Handles append method for adding an Amenity.id to the attribute amenity_ids"""
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
