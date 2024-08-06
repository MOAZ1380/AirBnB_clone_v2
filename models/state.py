from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from models.city import City

class State(BaseModel, Base):
    """Representation of a State"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # DBStorage: relationship
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

    # FileStorage: getter method
    @property
    def cities(self):
        """Return the list of City instances with state_id equals to the current State.id"""
        all_cities = models.storage.all(City)
        return [city for city in all_cities.values() if city.state_id == self.id]
