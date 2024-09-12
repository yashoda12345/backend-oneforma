from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: str
    username: str
    password: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "first_name": 'BTIN100001',
                "last_name": "Test",
                "password": "test",
                "email": "test@gmail.com",
                "username": "Test",
            }
        }


class UserUpdate(BaseModel):
    role: Optional[int] = None
    linkedin_url: Optional[str] = None
    agreed_nda: Optional[bool] = None


class UserInDBBase(UserBase):
    id: int
    email: str
    logged_in: bool

    class Config:
        orm_mode = True
