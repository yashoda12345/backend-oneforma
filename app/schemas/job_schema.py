from pydantic import BaseModel, validator, field_validator
from datetime import date
from .job_category_schema import JobCategoryBase
import datetime


class JobBase(BaseModel):
    recommended: bool
    job_title: str
    job_description: str
    pay: int
    posted_date: date
    category: int

    class Config:
        orm_mode = True


class JobListResponse(BaseModel):
    recommended: bool
    job_title: str
    job_description: str
    pay: int
    posted_date: date
    category_relation: JobCategoryBase
    created_at: datetime.datetime

    @field_validator("created_at")
    def get_created_at(cls, v):
        return v.strftime("%m/%d/%Y, %H:%M:%S")

    @field_validator("category_relation")
    def get_category_relation(cls, v):
        return v.name

    class Config:
        orm_mode = True
