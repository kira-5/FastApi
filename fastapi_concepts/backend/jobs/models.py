from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


# class Job(Base):
#     __tablename__ = "users"
#     __table_args__ = {'extend_existing': True}

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     company = Column(String, nullable=False)
#     company_url = Column(String)
#     location = Column(String, nullable=False)
#     description = Column(String, nullable=False)
#     date_posted = Column(Date)
#     is_active = Column(Boolean(), default=True)
#     owner_id = Column(Integer, ForeignKey("user.id"))
#     owner = relationship("User", back_populates="jobs")


class Job(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    company_url = Column(String, default=None)
    location = Column(String, default=None)
    description = Column(String, default=None)
    date_posted = Column(Date, default=None)
    is_active = Column(Boolean, nullable=False)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="jobs")
