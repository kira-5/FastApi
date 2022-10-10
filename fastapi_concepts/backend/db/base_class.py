from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()


@as_declarative()
class Base:
    id: Any
    __name__: str

    #to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    """
        A model class is the pythonic representation of a database table. Alright, now we are going to create a super grandfather class. Every model will inherit this 'Base' class and we will utilize this base class to create all the database tables. Also, we will keep all common logic related to tables in this 'Base' class. For instance, all our table tables will have an id field. This will be used to uniquely identify each row/record. Lets create this Base class in a file db > base_class.py

        That was a lot, but there is one big thing missing. Think think 😁
        Our app is in main.py file and It has no idea of whatever we are typing in other files! So, we have to tell our app to create our database tables for us. So, add the following code in main.py

    """