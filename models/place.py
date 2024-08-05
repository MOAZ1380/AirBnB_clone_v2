#!/usr/bin/python3
""" Class Place """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey,Integer,Float
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from sqlalchemy import Table
from os import getenv
import models
from models.review import Review

association_table = Table("place_amenity", Base.metadata,
                        Column("place_id", String(60),
                                ForeignKey("places.id"),
                                primary_key=True, nullable=False),
                        Column("amenity_id", String(60),
                                ForeignKey("amenities.id"),
                                primary_key=True, nullable=False))



class Place(BaseModel, Base):
    """ Class Place """
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
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")
    reviews = relationship("Review", back_populates="place", cascade="all, delete, delete-orphan")
    amenities = relationship("Amenity", secondary="place_amenity",viewonly=False)
    
    amenity_ids = []
    
    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
        
        @property
        def amenities(self):
            """Get/set linked Amenities."""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
    
