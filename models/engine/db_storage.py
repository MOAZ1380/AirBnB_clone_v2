from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place

class DBStorage:
    """Interacts with the MySQL database."""
    __engine = None
    __session = None
    
    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db}', pool_pre_ping=True)
        if env == "test":
            self.drop_all()
    
    def all(self, cls=None):
        """Query on the current database session."""
        result = {}
        classes = {"State": State, "City": City, "User": User, "Place": Place,"Amenity": Amenity,"Review": Review}  # Add 

        if cls:
            if isinstance(cls, str):  # Convert string to class
                cls = classes.get(cls)
            if cls in classes.values():
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = f"{type(obj).__name__}.{obj.id}"
                    result[key] = obj
            else:
                raise ValueError(f"Invalid class: {cls}")
        else:
            for class_name in classes.values():
                objs = self.__session.query(class_name).all()
                for obj in objs:
                    key = f"{type(obj).__name__}.{obj.id}"
                    result[key] = obj

        return result
    
    
    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)
    
    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()
    
    
    def delete(self, obj=None):
        """Delete from the current database session obj if not None."""
        if obj:
            self.__session.delete(obj)
    
    
    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
        
    def close(self):
        """Remove session"""
        self.__session.close()
