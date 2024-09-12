from typing import List
from pydantic import BaseModel


class ExpertiseMapperCreate(BaseModel):
    expertise: List[int]

    class Config:
        orm_mode = True
