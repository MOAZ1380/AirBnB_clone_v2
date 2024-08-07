#!/usr/bin/python3
""" Class Place """

from sqlalchemy import Column, String, Integer, ForeignKey, Float
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review


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
    reviews = relationship('Review', back_populates='place', cascade='all, delete-orphan')
    amenity_ids = []
    
    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def reviews(self):
            from models import storage
            """getter attribute returns the list of Review instances"""
            all_reviews = list(storage.all(Review).values())
            review_list = [r for r in all_reviews if r.place_id == self.id]
            return review_list
    
    
    
    
    # if getenv('HBNB_TYPE_STORAGE') != "db":
    #     @property
    #     def reviews(self):
    #         """getter attribute returns the list of Review instances"""
    #         list_reviews = []
    #         for city in storage.all(Review).values():
    #             if city.state_id == self.id:
    #                 list_reviews.append(city)
    #         return list_reviews
    # amenity_ids = []

    # # Relationships for DBStorage
    # user = relationship('User', back_populates='places')
    # city = relationship('City', back_populates='places')
    # reviews = relationship('Review', back_populates='place', cascade='all, delete-orphan')

    # # Getter for FileStorage
    # @property
    # def reviews(self):
    #     """Getter for reviews for FileStorage"""
    #     from models import storage
    #     all_reviews = storage.all(Review)
    #     return [review for review in all_reviews.values() if review.place_id == self.id]
    # user = relationship('User', back_populates='places')
    # cities = relationship('City', back_populates='places') 