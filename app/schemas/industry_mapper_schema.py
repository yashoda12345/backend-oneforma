from typing import List
from pydantic import BaseModel


class IndustryMapperCreate(BaseModel):
    industry: List[int]

    class Config:
        orm_mode = True
