#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ AM """
    name = ""


# from models.base_model import BaseModel, Base
# from sqlalchemy import Column, String, ForeignKey, Table
# from sqlalchemy.orm import relationship


# class Amenity(BaseModel, Base):
#     """ Class Amenity """
#     __tablename__='amenities'
#     name = Column(String(128), nullable=False)
#     place_amenities = relationship("Place", secondary='place_amenity', back_populates="amenities")
    