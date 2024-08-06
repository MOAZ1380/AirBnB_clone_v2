#!/usr/bin/python3
""" review module"""

from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """This class defines a review by various attributes"""
    __tablename__ = 'reviews'
    
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    
    
    ###################3
    # user = relationship('User', back_populates='reviews')
    # place = relationship('Place', back_populates='reviews')