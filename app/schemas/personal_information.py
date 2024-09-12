from pydantic import BaseModel
from typing import Optional
from datetime import date


class PersonalInformationCreate(BaseModel):
    gender: int
    nationality: int
    ethnicity: int
    street_address: str
    city: str
    state: int
    country_code: int
    postal_code: int
    mobile: str
    date_of_birth: date
    optional_number: Optional[str]

    class Config:
        orm_mode = True
