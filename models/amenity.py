from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Class Amenity """
    __tablename__='Amenity'
    name = Column(String(128), nullable=False)
    