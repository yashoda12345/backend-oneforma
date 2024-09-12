from pydantic import BaseModel
from datetime import date


class ExperienceCreateBase(BaseModel):
    role: str
    company: str
    start_year: date
    end_year: date
    description: str

    class Config:
        orm_mode = True
