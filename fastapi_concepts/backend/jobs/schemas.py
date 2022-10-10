from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


# shared properties
class JobBase(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


# Request Payload: #this will be used to validate data while creating a Job
class JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str
    date_posted: date
    is_active: bool


class JobUpdate(JobBase): # Partially update
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    date_posted: Optional[date] = None
    is_active: Optional[bool] = None
    # owner_id: Optional[int] = None


# Response Payload
class Job(JobBase):
    id: str
    title: str
    company: str
    company_url: Optional[str]
    location: str
    date_posted: date
    is_active: bool
    description: Optional[str]


    class Config:   # tells pydantic to convert even non dict obj to json
        orm_mode = True


# Response Payload: this will be used to format the response to not to have id,owner_id etc
class ShowJob(JobBase):
    id: str
    title: str
    company: str
    date_posted: date
    is_active: bool

    class Config:   # tells pydantic to convert even non dict obj to json
        orm_mode = True
