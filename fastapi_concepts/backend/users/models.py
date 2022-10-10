from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from db.base_class import Base


# class User(Base):
#     __tablename__ = "users"
#     __table_args__ = {'extend_existing': True}

#     id = Column(Integer, primary_key=True, index=True)
#     lname = Column(String)
#     fname = Column(String)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#     jobs = relationship("Job", back_populates="owner",
# cascade="all, delete-orphan")


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    jobs = relationship("Job", back_populates="owner",
                        cascade="all, delete-orphan")
