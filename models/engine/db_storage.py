
#!/usr/bin/python3

"""The DBStorage Class."""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.place import Place


class DBstorage:
    __engine = None
    __session = None

    def __init__(self):
        """The method to initialise everything."""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        theDB = getenv('HBNB_MYSQL_DB')
        theEnv = getenv('HBNB_ENV')

        self.__engine = \
            create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{theDB}',
                          pool_pre_ping=True)

        if theEnv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session and return a dictionary."""

        classes = {"City": City,
                   "State": State,
                   "Amenity": Amenity,
                   "User": User,
                   "Review": Review,
                   "Place": Place}

        objects = {}
        for classy in classes:
            if cls is None or cls is classes[classy]:
                laQuestion = self.__session.query(classes[classy]).all()
                for oJ in laQuestion:
                    key = "{}.{}".format(oJ.__class__.__name__, oJ.id)
                    objects[key] = oJ
        return objects

    def new(self, obj):
        """Adds an object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commits all the changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all the tables in the database."""
        Base.metadata.create_all(self.__engine)
        sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesh)
        self.__session = Session()

    def close(self):
        """Call the remove method on the private session attribute."""
        self.__session.remove()

