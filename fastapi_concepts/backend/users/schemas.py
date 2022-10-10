from pydantic import BaseModel
from pydantic import EmailStr
from typing import Optional

# Required Payload: Parent


class UserBase(BaseModel):
    email: EmailStr


# Request Payload
class UserCreate(UserBase):
    username: str
    password: str
    is_superuser: bool


class UserUpdate(UserBase):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None

# Response Payload


class User(UserBase):
    id: int
    username: str
    is_active: bool
    is_superuser: bool
    # jobs: list[Job] = []

    class Config:   # tells pydantic to convert even non dict obj to json
        orm_mode = True


# Response Payload
class ShowUser(UserBase):
    id: int
    username: str
    is_active: bool

    class Config:   # tells pydantic to convert even non dict obj to json
        orm_mode = True
