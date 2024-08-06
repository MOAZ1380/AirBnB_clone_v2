#!/usr/bin/python3
"""Defines all common attributes/methods for other classes."""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
import models

Base = declarative_base()

class BaseModel:
    """A base class for all models."""
    
    id = Column(String(60), primary_key=True, nullable=False, unique=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    
    def __init__(self, *args, **kwargs):
        """Initialize the attributes"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        """Returns a readable string representation of BaseModel instances."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime and saves the instance."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in my_dict:
            del my_dict["_sa_instance_state"]
        return my_dict
    
    def delete(self):
        """Deletes the current instance from the storage."""
        models.storage.delete(self)
