#!/usr/bin/python3
""" Class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City """

    state_id = ""
    name = ""


# #!/usr/bin/python3
# """ Class City """

# from models.base_model import BaseModel, Base
# from sqlalchemy import Column, String, ForeignKey
# from sqlalchemy.orm import relationship


# class City(BaseModel, Base):
#     """City class"""
#     __tablename__ = "cities"
#     name = Column(String(128), nullable=False)
#     state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
#     places = relationship("Place", backref="cities", cascade="all, delete-orphan")